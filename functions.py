import query
from outfuctions import *

class loggin_gui_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def log_button_action(self, username, password):
        if not clear_entry_data(username) or not clear_entry_data(password):
            return False, None
        
        login_success, access_type = self.query.login(username, password)

        if login_success:
            return True, access_type
        
        return False, None
    

class subject_gui_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    def add_subject_button_action(self, subject):
        if not validate_and_clean_subject_entry_query(subject):
            return False
        
        if self.query.insert_subject(subject) == False:
            return False
        
        self.query.show_data_subjects()
        return True

class staff_add_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def validate_document_id_repeated(self, document):
        query_check_document_id = "SELECT COUNT(*) FROM staff WHERE document_id = %s"
        self.query.cursor.execute(query_check_document_id, (document,))
        result = self.query.cursor.fetchone()
        
        if result[0] > 0:
            return False
        
        return True

class staff_edit_gui_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def get_status_edit_staff(self, staff_id):
        query = f"SELECT active FROM staff WHERE staff_id = %s"
        try:
            self.query.cursor.execute(query,(staff_id,))
            result = self.query.cursor.fetchone()
            result = result[0]
            if result:
                return "Activo"
            else:
                return "Inactivo"
        except Exception as e:
            print(f"Error lds: get_status: {e}")

    def entry_data_search_query(self, search_id, search_document_id):
        if not isinstance(search_id, (int, type(None))) or not isinstance(search_document_id, (str, type(None))):
            print(search_document_id)
            return False
        
        results = self.query.search_query("staff", search_id, search_document_id, None)
        
        if not results:
            return False
        status = self.get_status_edit_staff(results[0])
        if status == "Activo":
            return results
        else:
            return False

    
    def job_position_get(self, staff_id_registered):
        self.query.cursor.execute(f"SELECT jp.job_id FROM staff st INNER JOIN job_position jp ON st.job_id = jp.job_id WHERE staff_id = {staff_id_registered}")
        result = self.query.cursor.fetchone()
        if result and result[0] is not None:
            job_position = result[0]
            match job_position:
                case 1:
                    return "Administrador"
                case 2:
                    return "Profesor"
                case 3:
                    return "Tecnico en mantenimiento"
                case _:
                    return "Sin registro"
        else:
            return "Sin Asignar"

    def main_teacher_has(self, staff_id):
        self.query.cursor.execute(f"SELECT s.subject FROM teachers t INNER JOIN subjects s ON t.main_subject = s.subject_id WHERE staff_id = {staff_id}")
        result = self.query.cursor.fetchone()
        if result and result[0] is not None:
            main_subject = result[0].capitalize()
        else:
            main_subject = "Sin Asignar"

        self.query.cursor.execute(f"SELECT g.grade FROM teachers t INNER JOIN grades g ON t.guide_grade_id = g.grade_id WHERE staff_id = {staff_id}")
        result = self.query.cursor.fetchone()
        if result and result[0] is not None:
            main_grade = result[0].capitalize()
        else:
            main_grade = "Sin Asignar"
        
        return main_subject, main_grade
    
    def impart_subjects(self, staff_id):
        self.query.cursor.execute(f"""
        SELECT
        sb.subject
        FROM subject_teacher sbt
        INNER JOIN teachers tc ON sbt.teacher_id = tc.teacher_id
        INNER JOIN subjects sb ON sbt.subject_id = sb.subject_id
        INNER JOIN staff s ON s.staff_id = tc.staff_id
        WHERE tc.staff_id = {staff_id} and sbt.active = true;
        """)
        result = self.query.cursor.fetchall()

        if result and result[0] is not None:
            subjects_imparted = [subject[0].capitalize() for subject in result]
            return subjects_imparted
        else:
            return ["Sin Asignar",]
    
    def grades_assigned(self, staff_id):
        self.query.cursor.execute(f"""
        SELECT
        g.grade
        FROM teacher_grade_assigned tha
        INNER JOIN teachers t ON tha.teacher_id = t.teacher_id
        INNER JOIN grades g ON tha.grade_id = g.grade_id
        INNER JOIN staff st ON st.staff_id = t.staff_id
        WHERE st.staff_id = {staff_id} and tha.active = true;
        """)
        result = self.query.cursor.fetchall()
        
        if result and result[0] is not None:
            grades_assigned = [grade[0].capitalize() for grade in result]
            return grades_assigned
        else:
            return ["Sin Asignar",]
    
    def primary_teacher_bool(self, staff_id):
        query = "SELECT primary_teacher FROM teachers WHERE staff_id = %s"
        self.query.cursor.execute(query, (staff_id,))
        result = self.query.cursor.fetchone()
        
        if result and result[0] is not None:
            primary_teacher_bool = result[0]
            if primary_teacher_bool == True:
                return False
            else:
                return True
        else:
            return ["No Results Found"]
    
    def change_primary_teacher_state(self, bool, staff_id):
        if bool:
            query = f"UPDATE teachers SET primary_teacher = false WHERE staff_id = %s"
            try:
                self.query.cursor.execute(query,(staff_id,))
                self.query.connection.commit()
            except Exception as e:
                print(f"Error changing bool primary_teacher: {e}")
                self.query.connection.rollback()
        else:
            query = f"UPDATE teachers SET primary_teacher = false WHERE staff_id = %s"
            try:
                self.query.cursor.execute(query,(staff_id,))
                self.query.connection.commit()
            except Exception as e:
                print(f"Error changing bool primary_teacher: {e}")
                self.query.connection.rollback()
    
    def get_bool_primary_teacher(self, staff_id): #For the design of the table in the database I had to change te result 
        query = f"SELECT primary_teacher FROM teachers WHERE staff_id = %s"#the column "primary_teacher" must be high_school_teacher to avoid confussions
        try:
            self.query.cursor.execute(query,(staff_id,))
            self.query.connection.commit()
            result = self.query.cursor.fetchone()
            if result[0] == True: #This means in the table "teachers" is a primary_teacher
                result = False #so the result must be false to put in the checkbox in "staff_administration_panels" to show the grades associates with
                return result #high school grades
            else:
                result = True 
                return result
        except Exception as e:
            print(f"Error changing bool primary_teacher: {e}")
            self.query.connection.rollback()
    
    def get_bool_primary_teacher_compare(self, staff_id): 
        query = f"SELECT primary_teacher FROM teachers WHERE staff_id = %s"
        try:
            self.query.cursor.execute(query,(staff_id,))
            self.query.connection.commit()
            result = self.query.cursor.fetchone()
            return result[0]
        except Exception as e:
            print(f"Error changing bool primary_teacher: {e}")
            self.query.connection.rollback()

    def verify_and_change_primary_teacher_bool(self, primary_bool, staff_id):
        default_bool = self.get_bool_primary_teacher_compare(staff_id)
        if primary_bool != default_bool:
            query = f"UPDATE teachers SET primary_teacher = %s WHERE staff_id = %s"
            try:
                self.query.cursor.execute(query,(primary_bool, staff_id,))
                self.query.connection.commit()
            except Exception as e:
                print(f"Error in functions: verify_and_change_primary_teacher_bool: {e}")

class logical_delete_staff():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def entry_data_search_query_lds(self, search_id, search_document_id):
        if not isinstance(search_id, (int, type(None))) or not isinstance(search_document_id, (str, type(None))):
            print(search_document_id)
            return False
        
        results = self.query.search_query("staff", search_id, search_document_id, None)
        if not results:
            return False
        
        return results
    
    def job_position_get_lds(self, staff_id_registered):
        self.query.cursor.execute(f"SELECT jp.job_id FROM staff st INNER JOIN job_position jp ON st.job_id = jp.job_id WHERE staff_id = {staff_id_registered}")
        result = self.query.cursor.fetchone()
        if result and result[0] is not None:
            job_position = result[0]
            match job_position:
                case 1:
                    return "Administrador"
                case 2:
                    return "Profesor"
                case 3:
                    return "Tecnico en mantenimiento"
                case _:
                    return "Sin registro"
        else:
            return "Sin Asignar"
    
    def get_status(self, staff_id):
        query = f"SELECT active FROM staff WHERE staff_id = %s"
        try:
            self.query.cursor.execute(query,(staff_id,))
            result = self.query.cursor.fetchone()
            result = result[0]
            if result:
                return "Activo"
            else:
                return "Inactivo"
        except Exception as e:
            print(f"Error lds: get_status: {e}")
    
    def get_grade_guide(self, staff_id):
        query = f"""SELECT 
                    g.grade 
                    FROM teachers th 
                    INNER JOIN grades g ON th.guide_grade_id = g.grade_id 
                    WHERE staff_id = %s"""
        try:
            self.query.cursor.execute(query,(staff_id,))
            result = self.query.cursor.fetchone()
            if result and result is not None:
                return result[0]
            else:
                return "Sin Asignar"
        except Exception as e:
            print(f"Error lsd: get_grade_guide: {e}")
    
    def get_info_impart_time_teacher(self, staff_id):
        query = f"""
                    SELECT
                        g.grade,
                        sb.subject,
                        itt.impart_time_start,
                        itt.impart_time_end
                    FROM impart_time_teacher itt
                    INNER JOIN teacher_grade_assigned tga ON itt.teacher_grade_assigned_id = tga.tga_id
                    INNER JOIN subject_teacher sbt ON itt.subject_teacher_id = sbt.subject_teacher_id

                    INNER JOIN grades g ON tga.grade_id = g.grade_id
                    INNER JOIN subjects sb ON sbt.subject_id = sb.subject_id

                    WHERE 
                        EXISTS (
                            SELECT 1 
                            FROM teacher_grade_assigned tga2 
                            INNER JOIN subject_teacher sbt2 
                                ON tga2.teacher_id = sbt2.teacher_id
                            WHERE tga2.teacher_id = (SELECT teacher_id FROM teachers WHERE staff_id = %s)
                            AND tga2.tga_id = itt.teacher_grade_assigned_id
                            AND sbt2.subject_teacher_id = itt.subject_teacher_id
                        );
                       """
        try:
            self.query.cursor.execute(query,(staff_id,))
            results = self.query.cursor.fetchall()
            if results and results is not None:
                return results
            else:
                return [("Sin asignar","Sin asignar","Sin asignar","Sin asignar")]
        except Exception as e:
            print(f"Error lds: get_info_impart_time_teacher: {e}")
            return ["Error", "Error", "Error", "Error"]
    
    def detect_current_active_lds(self, staff_id, active_change):
        query = f"SELECT active FROM staff WHERE staff_id = %s"
        try:
            self.query.cursor.execute(query,(staff_id,))
            active = self.query.cursor.fetchone()
            if active[0] != active_change:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error lds: detect_current_active_lds: {e}")

    def logical_delete_staff_action(self, staff_id, active_change):
        if not active_change:
            if not self.detect_current_active_lds(staff_id, active_change):
                return
            
            query = f"SELECT deactivate_staff_and_teachers(%s)"
            try:
                self.query.cursor.execute(query,(staff_id,))
                self.query.connection.commit()
            except Exception as e:
                print(f"Error LDS: logical_delete_staff_deactivate: {e}")
                self.query.connection.rollback()
       
        if active_change:
            if not self.detect_current_active_lds(staff_id, active_change):
                return
            
            query = f"SELECT activate_staff_and_teachers(%s)"
            try:
                self.query.cursor.execute(query,(staff_id,))
                self.query.connection.commit()
            except Exception as e:
                print(f"Error LDS: logical_delete_staff_deactivate: {e}")
                self.query.connection.rollback()