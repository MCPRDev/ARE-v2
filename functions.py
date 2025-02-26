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
    
    def entry_data_search_query(self, search_id, search_document_id):
        if not isinstance(search_id, int) or not isinstance(search_document_id, (str, type(None))):
            return False
        
        results = self.query.search_query("staff", search_id, search_document_id, None)
        if not results:
            return False
        
        return results
    
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