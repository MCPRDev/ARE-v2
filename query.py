import psycopg2
import threading
import select
import time
from outfuctions import *


class Postgresqueries():
    def __init__(self, update_callback=None): 
        connection = psycopg2.connect(host="localhost", 
                              port=5432, 
                              dbname="are_v2",
                              user="postgres", 
                              password="1234")
        self.cursor = connection.cursor()
        self.connection = connection

        self.connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

        self.update_callback = update_callback 

        self.listen_thread = threading.Thread(target=self.listen_for_changes_subject_changes, daemon=True)
        self.listen_thread.start()
    
    def reconnect(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port=5432,
                dbname="are_v2",
                user="postgres",
                password="1234"
            )
            self.cursor = self.connection.cursor()
            self.connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor.execute("LISTEN subject_changes;")
            print("✅ Reconecting...")
        except Exception as e:
            print(f"❌ Error trying to reconnect: {e}")

    def listen_for_changes_subject_changes(self):
        self.cursor.execute("LISTEN subject_changes;")
        print("📡 Recieving changes...")

        while True:
            if self.connection.closed:
                print("⚠️ The connection has lost...")
                self.reconnect()
            
            try:
                self.connection.poll()
                while self.connection.notifies:
                    notify = self.connection.notifies.pop(0)
                    print(f"🔄 Update detected in DB: {notify.payload}")

                    if self.update_callback:
                        self.update_callback()

            except Exception as e:
                print(f"❌ Error while listening: {e}")

            time.sleep(1)


    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def __del__(self):
        self.close_connection()

    def login(self, username_input, password_input): #Login fuctions to check password and username registered on the table --- This must be upgraded with authentication tokens
            query_username = "SELECT * FROM login_access"
            self.cursor.execute(query_username)
            rows = self.cursor.fetchall()

            if not is_valid_username(username_input) or not is_valid_password(password_input):
                print("Invalid username or password format. Please try again.")
                return False, None

            query = "SELECT log_password, access_type FROM login_access WHERE log_user = %s"
            self.cursor.execute(query, (username_input,))
            row = self.cursor.fetchone()

            if row and row[0] == password_input:
                print("Login successful!")
                return True, row[1]
            else:
                print("Invalid username or password.")
                return False, None
            
    def insert_staff(self, first_name, middle_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthday): #Custom staff insert on the table

        if document_id_validation(document_id):
             pass
        else:
             print("Invalid document id. Please try again.")
             return
        
        if phone_number_validation(phone_number):
             pass
        else:
             print("Invalid phone number. Please try again.")
             return
        

        query_check_document_id = "SELECT COUNT(*) FROM staff WHERE document_id = %s"
        self.cursor.execute(query_check_document_id, (document_id,))
        count = self.cursor.fetchone()[0]

        if count > 0:
            print(f"The register with the document id {document_id} already exist.")
            return 
        
        middle_name = middle_name if middle_name else None
        second_surname = second_surname if second_surname else None

        query_insert_staff = "INSERT INTO staff (first_name, middle_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        try:
            self.cursor.execute(query_insert_staff, (first_name, middle_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthday))
            self.connection.commit()
            print("Staff record inserted successfully!")

        except psycopg2.errors.ForeignKeyViolation as e:
             self.connection.rollback()
             print(f"Error: {e}")

        except Exception as e:
             self.connection.rollback()
             print(f'Error: {e}')
    def search_query(self, table, register_id, document_id, student_code): #Search query to get any information and use it for other functions
        table_columns = {
            'staff': ('staff_id', 'document_id'),
            'student_representative': ('representative_id', 'representative_document_id'),
            'students': ('register_id', 'student_code')
        }

        if table not in table_columns:
            print("The table you are trying to access is not available.")
            return False

        id_column, doc_column = table_columns[table]

        if register_id:
            if not id_validation(register_id):
                print("Invalid register id. Please try again.")
                return False
            query = f"SELECT * FROM {table} WHERE {id_column} = %s"
            params = (register_id,)
        elif document_id:
            if not document_id_validation(document_id):
                print("Invalid document id. Please try again.")
                return False
            query = f"SELECT * FROM {table} WHERE {doc_column} = %s"
            params = (document_id,)
        elif student_code:
            if not student_code_validation(student_code):
                print("Invalid student code. Please try again.")
                return False
            query = f"SELECT * FROM {table} WHERE student_code = %s"
            params = (student_code,)
        else:
            print("You must specify a registration id, document id, or student code.")
            return False

        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
       
        if result: # it's solve the problem when you add the table you are serching on the tuple you need to use in the other functions
            result = result + (table,)
        else:
            print(f"Record not found in table {table}.")
            return False
        
        if result:
            print(f"Query result: {result}")
            self.query_search_results = result
            self.table_search_results = result[-1]
            self.id_search_results = result[0]
            table_id = {
                 'staff': 'staff_id',
                 'student_representative':'representative_id',
                 'students':'register_id'
            }
            self.column_search_id_result = table_id[result[-1]]
            return result
        else:
            print(f"Record not found in table {table}.")
            return False
        
    def search_results_validator(self): #This fuction could detect search, if not detech any search results it will return False instead of returning True
        if not hasattr(self, 'query_search_results') or not hasattr(self, 'query_search_results') or not hasattr(self, 'query_search_results'):
            print("No search results available. Please perform a search first.")
            return False
        else:
            return True
    
    def get_editable_columns(self, table): #Here we get the column names that are editable, this works with edit_record a and therefore with edit_multiple_columns
        if not self.search_results_validator():
            print("search_results_validator didn't detect a search")
            return False

        editable_columns_by_table = {
            'staff': ['first_name', 'middle_name', 'first_surname', 'second_surname', 'document_id', 'address', 'job_id', 'phone_number', 'birthday'],
            'students': ['student_code', 'first_name', 'middle_name', 'first_surname', 'second_surname', 'birthday', 'grade_id', 'representative_id'],
            'student_representative': ['first_name', 'middle_name', 'first_surname', 'second_surname', 'representative_document_id', 'residential_address', 'phone_number']
        }
        self.column_search = editable_columns_by_table.get(table, [])
        return editable_columns_by_table.get(table, [])

    def validate_value(self, table, column, value): #Validate the entry value in the other fuctions

        if value is None or value == "":
            print("The value cannot be empty.")
            return False

        if column == 'document_id' and not document_id_validation(value):
            print("The document is not valid.")
            return False

        if column == 'phone_number' and not phone_number_validation(value):
            print("The phone number is not valid.")
            return False

        if column == 'birthday' and not validate_date(value):
            print("The date of birth is not valid.")
            return False
        
        if column == 'student_code' and not student_code_validation(value):
            print("The student code is not valid.")
            return False
        
        if column == 'representative_document_id' and not document_id_validation(value):
            print("The representative's document is not valid.")
            return False
        
        return True
    
    def edit_record(self, table, record_id, column_to_edit, new_value): #This function works with edit_multi_record, validate_value, get_editable_columns and search query
        if not self.search_results_validator():
            print("search_results_validator didn't detect a search")
            return False
        
        editable_columns = self.get_editable_columns(table)

        if not editable_columns:
            print(f"You cannot edit records in the {table} table.")
            return False

        if column_to_edit not in editable_columns:
            print(f"The column '{column_to_edit}' is not editable in the table {table}.")
            return False

        if not self.validate_value(table, column_to_edit, new_value):
            print(f"The value '{new_value}' is not valid for the column '{column_to_edit}'.")
            return False
        
        id_search = self.column_search_id_result
        query = f"UPDATE {table} SET {column_to_edit} = %s WHERE {id_search} = %s"
        try:
            self.cursor.execute(query, (new_value, record_id))
            self.connection.commit()
            print(f"Record correctly updated in the {table} table.")
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating the registry: {e}")
            return False
        
    def edit_multiple_columns(self, updates): #This function depends: edit_record.
        if not self.search_results_validator():
            print("search_results_validator didn't detect a search")
            return False
        
        table = self.table_search_results
        record_id = self.id_search_results

        for column, new_value in updates.items():
            success = self.edit_record(table, record_id, column, new_value)
            if not success:
                print(f"Error updating column '{column}'. No further updates were performed.")
                return False
        print("All updates were performed correctly.")
        return True
    
    def get_table_columns(self): #With this we can get all the columns depending what table we want to...
        if not self.search_results_validator():
            print("search_results_validator didn't detect a search")
            return False
        
        table = self.table_search_results
        query = f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = %s
        """

        self.cursor.execute(query, (table,))
        columns = self.cursor.fetchall()
        self.column_search_id_result = columns
        return [column[0] for column in columns]

    def change_status(self, boolean_flag): #This function is like delete data from the database/table, only changin the status of the registered value
        if not self.search_results_validator(): #change_status works for staff, students and representative_students
            print("search_results_validator didn't detect a search")
            return False
    
        if boolean_flag not in ['True', 'False']:
            print("Invalid boolean flag. Please use True or False.")
            return False
        
        table = self.table_search_results
        edit_table_id = self.column_search_id_result
        edit_id = self.id_search_results

        query = f'UPDATE {table} SET active = {boolean_flag} WHERE {edit_table_id} = {edit_id}'
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print('Status updated successfully!')
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating status: {e}")
            return False
    
    def show_table_record(self, table, number_results): #Here we can get the records in the table but we can limit the number of results
        tables = ['staff', 'student_representative', 'students']
        if table not in tables:
            print(f'Invalid table. Choose from: {tables}')
            return False
        
        query = f"SELECT * FROM {table} LIMIT {number_results}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print(f"Query result: {results}")
        return results
    
    def query_total_records_by_table(self, table): #With this function we get the total number of records
        try:
            query = f"SELECT COUNT(*) FROM {table}"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            print(f"Total records in {table}: {result[0]}")
            if result is not None:
                return result[0]
            else:
                print('No records found')
                return None
        except Exception as e:
            print(f'Error querying total records: {e}')
            return None

    def query_insert_student(self, student_code, first_name, middle_name, first_surname, second_surname, birthday, grade_id, representative_id): #Custom query to insert students on the table
        if not student_code_validation(student_code):
            print('Invalid student code')
            return False
        
        if not validate_date(birthday):
            print('Invalid birthday')
            return False
        
        total_students = self.query_total_records_by_table('students')
        unique_code_center = code_center_generator(student_code, total_students)

        middle_name = middle_name if middle_name else None
        second_surname = second_surname if second_surname else None

        data_entry = (student_code, first_name, middle_name, first_surname, second_surname, birthday, grade_id, representative_id)
        
        if not data_entry:
            print('There is something wrong with the data you are trying to insert.')
            return False
        
        data_insert = (student_code, unique_code_center, first_name, middle_name, first_surname, second_surname, birthday, grade_id, representative_id)
        query = """
        INSERT INTO students (student_code, student_center_code, first_name, middle_name, first_surname, second_surname, birthday, grade_id, representative_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            self.cursor.execute(query, data_insert)
            self.connection.commit()
            print('Student inserted successfully.')
        except Exception as e:
            self.connection.rollback()
            print(f'Error inserting student: {e}')
    
    def query_students_by_grade(self, grade_id):
        if not validate_grade(grade_id):
            print('Invalid grade ID')
            return False
        
        try:
            query = f"SELECT * FROM students WHERE grade_id = %s"
            self.cursor.execute(query, (grade_id,))
            results = self.cursor.fetchall()
            if results is not None:
                if len(results) > 0:
                    print(f'Query result: {results}')
                    return results
                else:
                    print('No students found for this grade.')
                    return None
            else:
                print('No students found for this grade or could be an error.')
                return None
        except Exception as e:
            print(f'Error querying students by grade: {e}')
            return None
    
    def query_insert_student_representative(self, first_name, middle_name, first_surname, second_surname, representative_document_id, residential_address, phone_number):
        if not document_id_validation(representative_document_id):
            print('Invalid representative document ID')
            return False
        
        if not phone_number_validation(phone_number):
            print('Invalid phone number')
            return False
        
        middle_name = middle_name if middle_name else None
        second_surname = second_surname if second_surname else None

        query_check_document_id = "SELECT COUNT(*) FROM student_representative WHERE representative_document_id = %s"
        self.cursor.execute(query_check_document_id, (representative_document_id,))
        count = self.cursor.fetchone()[0]

        if count > 0:
            print(f"The register with the document id {representative_document_id} already exist.")
            return 
        
        data_entry = (first_name, middle_name, first_surname, second_surname, representative_document_id, residential_address, phone_number)
        
        if not data_entry:
            print('There is something wrong with the data you are trying to insert.')
            return False
        
        query = """
        INSERT INTO student_representative (first_name, middle_name, first_surname, second_surname, representative_document_id, residential_address, phone_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, data_entry)
            self.connection.commit()
            print('Student representative inserted successfully.')
        except Exception as e:
            self.connection.rollback()
            print(f'Error inserting student representative: {e}')
    def show_data_subjects(self):
        try:
            self.cursor.execute("SELECT subject_id, subject FROM subjects WHERE active = true")
            
            rows = self.cursor.fetchall()
            return rows if rows else []
        except Exception as e:
            print(f'Error fetching data subjects: {e}')
            return []
    
    def show_data_grades(self, high_school_teacher):
        if high_school_teacher == True:
            query = """SELECT grade FROM grades WHERE education_level_id = 2"""
            try:
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows if rows else []
            except Exception as e:
                print(f'Error fetching data grades high school teacher: {e}')
                return []
        else:
            try:
                    self.cursor.execute("SELECT grade FROM grades WHERE education_level_id = 1")
                    
                    rows = self.cursor.fetchall()
                    return rows if rows else []
            except Exception as e:
                    print(f'Error fetching data grades: {e}')
                    return []
        
    def show_students_by_guide_teacher(self, id_teacher):
        if not id_validation(id_teacher):
            print('Invalid ID teacher')
            return False
        
        query = f"""SELECT 
                    CONCAT_WS(' ', s.first_name, s.first_surname) AS teacher_name,
                    st.register_id AS id_register_student,
                    g.grade AS current_grade,
                    CONCAT_WS(' ', st.first_name, st.middle_name, st.first_surname, st.second_surname) AS student_name
                    FROM teachers t
                    JOIN staff s ON t.staff_id = s.staff_id
                    JOIN students st ON t.guide_grade_id = st.grade_id
                    JOIN grades g ON st.grade_id = g.grade_id
                    WHERE t.guide_grade_id = %s;"""
        try:
            self.cursor.execute(query, (id_teacher,))
            results = self.cursor.fetchall()
            if results is not None:
                if len(results) > 0:
                    print(f'Query result: {results}')
                    return results
                else:
                    print('No students found for this guide teacher.')
                    return None
            else:
                print('No students found for this guide teacher or could be an error.')
                return None
        except Exception as e:
            print(f'Error querying students by guide teacher: {e}')
            return None
    
    def insert_subject(self, subject):
        if not validate_and_clean_subject_entry_query(subject):
            print('Invalid subject')
            return False
        
        self.cursor.execute("SELECT subject FROM subjects")
        subjects_added = [row[0] for row in self.cursor.fetchall()]

        if not validate_data_entry_no_repeted(subject, subjects_added):
            query_active = f"SELECT active FROM subjects WHERE subject = %s"
            self.cursor.execute(query_active, (subject,))
            activity = self.cursor.fetchone()
            if activity[0] == False:
                query = f"UPDATE subjects SET active = %s WHERE subject = %s"
                self.cursor.execute(query, (True, subject))
                print(f'Already exits, subject {subject} activated.')
                return True
            else:
                print(f'Subject {subject} already exists.')
                return False


        
        query = f"INSERT INTO subjects(subject) VALUES (%s)"
        try:
            self.cursor.execute(query, (subject,))
            self.connection.commit()
            print('Subject inserted successfully.')
        except Exception as e:
            self.connection.rollback()
            print(f'Error inserting subject: {e}')
            return False
    
    def edit_subject_name(self, id_subject, new_name_subject):
        if not validate_and_clean_subject_entry_query(new_name_subject):
            print('Invalid new subject name')
            return False
        
        if not id_validation(id_subject):
            print('Invalid ID subject')
            return False
        
        self.cursor.execute("SELECT subject FROM subjects")
        subjects_added = [row[0] for row in self.cursor.fetchall()]

        if not validate_data_entry_no_repeted(new_name_subject, subjects_added):
            print("Error, this subject already exists")
            return False
        
            

        try:
            query = f"UPDATE subjects SET subject = %s WHERE subject_id = %s"
            self.cursor.execute(query, (new_name_subject, id_subject))
            self.connection.commit()
            print('Subject edited successfully.')
            return True
        except Exception as e:
            self.connection.rollback()
            print(f'Error editing subject: {e}')
            return False
    def get_subject_id_already_exists(self, subject):
        self.cursor.execute(f"SELECT subject_id FROM subjects WHERE subject = '{subject}'")
        subjects_ids = [row[0] for row in self.cursor.fetchall()]
        return subjects_ids
    
    def delete_data_from_table(self, table, entry_id):
        tables = [
            'impart_time_teacher',
            'login_access',
            'login_access_type',
            'staff',
            'student_representative',
            'students',
            'subject_teacher',
            'subjects',
            'teacher_grade_assigned',
            'teachers'
        ]
        position_table = tables.index(table)

        id_tables = {
            'impart_time_teacher' : 'itt_id',
            'login_access' : 'access_id',
            'login_access_type' : 'id_access_type',
            'staff' : 'staff_id',
            'student_representative' : 'representative_id',
            'students' : 'register_id',
            'subject_teacher' : 'subject_teacher_id',
            'subjects' : 'subject_id',
            'teacher_grade_assigned' : 'tga_id',
            'teachers' : 'teacher_id'
        }

        table = tables[position_table]
        id_change_status = id_tables[table]

        query = f"UPDATE {table} SET active = false WHERE {id_change_status} = {entry_id}"

        try:
            self.cursor.execute(query)
            self.connection.commit()
            print('Data deleted successfully.')
        except Exception as e:
            self.connection.rollback()
            print(f'Error deleting data: {e}')
            return False
        


#########################CONSOLE TEST#########################
#pg = Postgresqueries()
#print(pg.show_data_subjects())
#pg.insert_subject('Matematica Oratoria')
#pg.login('admin_basic_log_in_user', 'admin_basic_log_in_password')
#pg.search_query('staff', None, None, None)
#pg.search_query('student_representative', None, '123-123123-1234K', None)
#datos = pg.search_query('students', 1, None, None)
#print(datos[-1])

#pg.change_status('students', )

#pg.search_query('staff', 2, '', None)
#pg.get_table_columns()
#pg.edit_registered_values()
#pg.change_status('False')
#update = {
#    'phone_number': '1231-1233'
#    }
#
#pg.edit_multiple_columns(update)

#pg.show_table_record('students', 5)
#code = 'MC-021205-1234567'
#pg.query_insert_student(code, 'John', '', 'John', '', '1990-01-01', 1, 1)
#pg.query_insert_student_representative('Yoquese', '', 'Perez', '', '123-654321-1234A', 'Main ST 534' ,'0000-0000')
#print(type(pg.query_students_by_grade(1)))

#pg.login('admin_basic_log_in_user','admin_basic_log_in_password')