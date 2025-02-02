import psycopg2
from outfuctions import document_id_validation, phone_number_validation, id_validation, student_code_validation, validate_date


#Esta query es para una base de datos en localhost (como se especifica en host)


class Postgresqueries():
    def __init__(self): #
        connection = psycopg2.connect(host="localhost", 
                              port=5432, 
                              dbname="are_v2",
                              user="postgres", 
                              password="1234")
        self.cursor = connection.cursor()
        self.connection = connection

    def login(self, username_input, password_input): #Login fuctions to check password and username registered on the table
            query_username = "SELECT * FROM login_access"
            self.cursor.execute(query_username)
            rows = self.cursor.fetchall()

            for row in rows:
                if row[2] == username_input and row[3] == password_input:
                    print("Login successful!")
                    return True
                elif row[2] != username_input:
                     print("Incorrect username. Please try again.")
                     return False
                elif row[3]!= password_input:
                     print("Incorrect password. Please try again.")
                     return False
                else:
                     print("An error occurred during login.")
                     return False
    def insert_staff(self, first_name, middle_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthday): #SQL INSERT just for staff

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
    
    def get_editable_columns(self, table):
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

    def validate_value(self, table, column, value):

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
        
    def edit_multiple_columns(self, updates):
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
    
    def get_table_columns(self):
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
        if not self.search_results_validator():
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
        



pg = Postgresqueries()
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
