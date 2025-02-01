import psycopg2
from outfuctions import document_id_validation, phone_number_validation, id_validation, student_code_validation


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

    def login(self, username_input, password_input):
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
    def insert_staff(self, first_name, middle_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthday):

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
    def search_query(self, table, register_id, document_id, student_code):
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
        result = self.cursor.fetchone() + (table,)
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
            self.column_search_results = table_id[result[-1]]
            return result
        else:
            print(f"Record not found in table {table}.")
            return False

    def change_status(self, boolean_flag):
        if boolean_flag not in ['True', 'False']:
            print("Invalid boolean flag. Please use True or False.")
            return False
        
        table = self.table_search_results
        edit_table_id = self.column_search_results
        edit_id = self.id_search_results
        
        query = f'UPDATE {table} SET active = {boolean_flag} WHERE {edit_table_id} = {edit_id}'
        self.cursor.execute(query)
        self.connection.commit()
        print('Updated')


pg = Postgresqueries()
#pg.search_query('staff', None, None, None)
#pg.search_query('student_representative', None, '123-123123-1234K', None)
#datos = pg.search_query('students', 1, None, None)
#print(datos[-1])

#pg.change_status('students', )

pg.search_query('students', 1, None, None)
pg.change_status('True')