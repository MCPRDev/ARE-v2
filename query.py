import psycopg2
from outfuctions import document_id_validation, phone_number_validation


#Esta query es para una base de datos en localhost (como se especifica en host)


class Postgresqueries():
    def __init__(self):
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
            print(f"El registro con document_id {document_id} ya existe. No se insertará un nuevo registro.")
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
     
     def searh_query(self, table, register_id, document_id, ):