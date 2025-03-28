import query
from outfuctions import *

#Every subwidget in staff_administration_panel has their actions

class loggin_gui_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def log_button_action(self, username, password):
        if not clear_entry_data(username) or not clear_entry_data(password):
            return False, None
        
        login_success, access_type = self.query.login(username, password) #We use login from query.py to get the data and log in

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

#There are some queries here that is not from query.py, it is, because is information y need to get at the momment and one time, not like a cycle
#So query.py is for complex queries
class staff_add_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    #Just a fuction to verify if there is no document_id_repeated
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
    #get_status_edit_staff is a fuction to get from the DB if the staff is active, we cannot edit a inactive staff
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
    #Here we the information depends on what user enter, if the search is by id or document id
    def entry_data_search_query(self, search_id, search_document_id):
        if not isinstance(search_id, (int, type(None))) or not isinstance(search_document_id, (str, type(None))):
            print(search_document_id)
            return False
        
        results = self.query.search_query("staff", search_id, search_document_id, None) #Using this query because this query depends other ones like edit_record
        
        if not results:
            return False
        status = self.get_status_edit_staff(results[0])
        if status == "Activo":
            return results
        else:
            return False
    #Here gets the job position and transformit in a text to show it in the gui
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
    #Get main subject and grade assigned from a specific teacher
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
    #subjects assigned
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
    #grades assigned
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
    #Here we'll obtain the teacher primary_bool but in the gui works differents, in the gui we want to know if th teacher is change to elementary or high school teacher
    def primary_teacher_bool(self, staff_id):
        query = "SELECT primary_teacher FROM teachers WHERE staff_id = %s"
        self.query.cursor.execute(query, (staff_id,))
        result = self.query.cursor.fetchone()
        
        if result and result[0] is not None:
            primary_teacher_bool = result[0]
            if primary_teacher_bool == True: #So in the BD --> are_v2 --> teachers --> primary_teacher // if its true so its false that it is a high school teacher
                return False #So, to work with that we change and return false to send that signal that IT'S NOT A HIGH SCHOOL TEACHER
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
    #job_position_get_lds is just to show it in the GUI and the user watchs what is, because we can show numbers like 1, 2 or 3 without knowing what it means
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
                            AND itt.active = true
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

    def set_null_grade_guide_lds(self, staff_id):
        query = f"UPDATE teachers SET guide_grade_id = NULL WHERE staff_id = %s"
        try:
                self.query.cursor.execute(query,(staff_id,))
                self.query.connection.commit()
        except Exception as e:
            print(f"Error LDS: set_null_grade_guide_lds: {e}")
            self.query.connection.rollback()

    def logical_delete_staff_action(self, staff_id, active_change):
        if not active_change:
            if not self.detect_current_active_lds(staff_id, active_change):
                return
            
            query = f"SELECT deactivate_staff_and_teachers(%s)"
            try:
                self.query.cursor.execute(query,(staff_id,))
                self.query.connection.commit()
                self.set_null_grade_guide_lds(staff_id)
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

class search_staff_widget():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def load_staff_table(self):
        query = """ 
                    SELECT
                    s.staff_id,
                    CONCAT_WS(' ', s.first_name, s.middle_name, s.first_surname, s.second_surname) AS staff_full_name,
                    s.document_id,
                    s.address,
                    s.phone_number,
                    s.birthday,
                    j.job_position
                    FROM staff s
                    INNER JOIN job_position j ON s.job_id = j.job_id
                    ORDER BY s.staff_id ASC;
                """
        try:
            self.query.cursor.execute(query)
            results = self.query.cursor.fetchall()
            if results and results is not None:
                new_results = list()
                job_position_translate = ["Administrador", "Profesor", "Tecnico en Mantenimiento"]
                for values in results:
                    values = list(values)
                    if values[5] is not None:
                        birthdate = values[5]
                        age = calculate_age_edited(birthdate)
                        values.insert(6, age)
                        status = self.get_status(values[0])
                        values.insert(len(values), status)

                        values = [job_position_translate[0] if x == 'Administrator' else x for x in values]
                        values = [job_position_translate[1] if x == 'Teacher' else x for x in values]
                        values = [job_position_translate[2] if x == 'Technical Maintenance' else x for x in values]
                        
                        new_results.append(values)

                return new_results
            else:
                return None
        except Exception as e:
            print(f"Error SSW: load_staff_table: {e}")
            return None
        
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
    
    def get_job_id(self, staff_id):
        query = f"SELECT job_id FROM staff WHERE staff_id = %s"
        try:
            self.query.cursor.execute(query,(staff_id,))
            results = self.query.cursor.fetchone()
            if results and results[0]:
                results = results[0]
                return results
            else:
                return None
        except Exception as e:
            print(f"Error ssw: get_job_id: {e}")
            return None
    
    def get_schedule_impart_time(self, staff_id):
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
                            AND itt.active = true
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
    
    def get_main_subject_guide_grade(self, staff_id):
        query = f""" 
                SELECT
                g.grade,
                sb.subject
                FROM teachers t
                LEFT JOIN grades g ON t.guide_grade_id = g.grade_id
                LEFT JOIN subjects sb ON t.main_subject = sb.subject_id
                WHERE staff_id = %s
                """
        try:
            self.query.cursor.execute(query,(staff_id,))
            results = self.query.cursor.fetchone()
            print(results)
            if results[0] is not None:
                grade_result = results[0]
            else: 
                grade_result = None
            
            if results[1] is not None:
                main_subject = results[1]
            else:
                main_subject = None
            
            return grade_result, main_subject
        except Exception as e:
            print(f"Error ssw: get_main_subject_guide_grade: {e}")
            return "Error", "Error"
    
    def get_grades_assigned(self, staff_id):
        query = f"""
                SELECT 
                g.grade
                FROM teacher_grade_assigned tga
                INNER JOIN grades g ON tga.grade_id = g.grade_id
                WHERE teacher_id = (SELECT teacher_id FROM teachers WHERE staff_id = %s) AND active = true;
                """
        try:
            self.query.cursor.execute(query,(staff_id,))
            results = self.query.cursor.fetchone()
            if results and results is not None:
                return results
            else:
                return ["Sin Asignar",]
        except Exception as e:
            print(f"Error ssw: get_grades_assigned: {e}")
            return ["Error",]
    
    def get_subjects_assigned(self, staff_id):
        query = f"""
                SELECT 
                sb.subject
                FROM subject_teacher sbt
                INNER JOIN subjects sb ON sbt.subject_id = sb.subject_id
                WHERE sbt.teacher_id = (SELECT teacher_id FROM teachers WHERE staff_id = %s) AND sbt.active = true;
                """
        try:
            self.query.cursor.execute(query,(staff_id,))
            results = self.query.cursor.fetchall()
            if results and results is not None:
                return results
            else:
                return ["Sin asignar",]
        except Exception as e:
            print(f"Error ssw: get_subject_assigned: {e}")
            return ["Error",]
    
    def get_date_registered_and_last_update(self, staff_id):
        query = f""" 
                SELECT
                registered_at,
                updated_at
                FROM staff
                WHERE staff_id = %s AND active = true;
                """
        try:
            self.query.cursor.execute(query,(staff_id,))
            results = self.query.cursor.fetchone()
            print(results)
            if results and results is not None:
                registered_date = results[0]
                updated_date = results[1]
                return registered_date, updated_date
            else:
                return "Sin Asignar", "Sin Asignar"
        except Exception as e:
            print(f"Error ssw: get_date_regis_upd: {e}")
            return "Error", "Error"

class assign_impart_time_teacher():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def load_impart_time_table(self, Order):
        query = f"""SELECT * FROM teacher_assigned_and_not_assigned_impart_time""" #We select the information from the view and just order by
        match Order:
            case 0:
                pre_order = "ORDER BY teacher_id ASC;"
            case 1: #A specific order by for the grades, with the view a can't get the id of every grade because it changes the view a lot and don't get the information I wanted to show in the gui
                pre_order = """ 
                                ORDER BY 
                                    CASE 
                                        WHEN teacher_grade_assigned = 'Primer Grado' THEN 1
                                        WHEN teacher_grade_assigned = 'Segundo Grado' THEN 2
                                        WHEN teacher_grade_assigned = 'Tercero Grado' THEN 3
                                        WHEN teacher_grade_assigned = 'Cuarto Grado' THEN 4
                                        WHEN teacher_grade_assigned = 'Quinto Grado' THEN 5
                                        WHEN teacher_grade_assigned = 'Sexto Grado' THEN 6
                                        WHEN teacher_grade_assigned = 'Septimo Grado' THEN 7
                                        WHEN teacher_grade_assigned = 'Octavo Grado' THEN 8
                                        WHEN teacher_grade_assigned = 'Noveno Grado' THEN 9
                                        WHEN teacher_grade_assigned = 'Decimo Grado' THEN 10
                                        WHEN teacher_grade_assigned = 'Undecimo Grado' THEN 11
                                        ELSE 99
                                    END ASC;
                            """
            case 2:
                pre_order = """
                                ORDER BY impart_time_start ASC;
                            """
            case 3:
                pre_order = """
                                ORDER BY impart_time_end DESC NULLS LAST;
                            """
            case 4:
                pre_order = """ 
                                ORDER BY 
                                    CASE 
                                        WHEN impart_time_start IS NULL THEN 0 
                                        ELSE 1 
                                    END ASC;
                            """
            case 5:
                pre_order = """ 
                                ORDER BY 
                                    CASE 
                                        WHEN impart_time_end IS NULL THEN 0 
                                        ELSE 1 
                                    END ASC;
                            """
            case _:
                pre_order = ";"
        final_query = query + " " + pre_order
        try:
            self.query.cursor.execute(final_query)
            results = self.query.cursor.fetchall()
            if results and results is not None:
                return results
            else:
                return None
        except Exception as e:
            print(f"Error aitt: load_impart_time_table: {e}")

    def get_staff_id_w_teacher_id(self, teacher_id):
        query = f"SELECT staff_id FROM teachers WHERE teacher_id = %s"
        try:
            self.query.cursor.execute(query,(teacher_id,))
            result = self.query.cursor.fetchone()
            if result and result is not None:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Error aitt: get_staff_id_w_teacher_id: {e}")
    
    def unassign_impart_time_action(self, teacher_id, grade, subject, time_starts, time_ends):
        query = f"""
                    WITH target_records AS (
                        SELECT 
                            itt.itt_id  -- Selecciona el ID de la tabla que deseas actualizar
                        FROM 
                            impart_time_teacher itt
                        INNER JOIN 
                            teacher_grade_assigned tga 
                            ON tga.tga_id = itt.teacher_grade_assigned_id
                        INNER JOIN 
                            grades g 
                            ON g.grade_id = tga.grade_id
                        INNER JOIN 
                            subject_teacher sbt 
                            ON sbt.subject_teacher_id = itt.subject_teacher_id
                        INNER JOIN 
                            subjects sb 
                            ON sb.subject_id = sbt.subject_id
                        INNER JOIN 
                            teachers th 
                            ON th.teacher_id = tga.teacher_id
                        WHERE 
                            th.teacher_id = %s
                            AND g.grade = %s
                            AND sb.subject = %s
                            AND itt.impart_time_start = %s
                            AND itt.impart_time_end = %s
                    )
                    UPDATE 
                        impart_time_teacher
                    SET 
                        active = false 
                    WHERE 
                        itt_id IN (SELECT itt_id FROM target_records);
                """
        try:
            self.query.cursor.execute(query,(teacher_id, grade, subject, time_starts, time_ends,))
            self.query.connection.commit()
        except Exception as e:
            print(f"Error aitt: unassign_impart_time_action: {e}")
            self.query.connection.rollback()
    
    def verify_teacher_time_assign(self, teacher_id ,grade, subject, time_starts, time_ends): #With this functions we verify if there is any teacher already assign with a specific grade and times or if that times are already assign and the teacher cannot impart in that time
        query = f""" 
                    SELECT 'conflict' AS result
                    FROM vw_itt_to_verify_data
                    WHERE (
                        teacher_id = %s 
                        AND grade = %s
                        AND subject = %s
                        AND impart_time_start = %s 
                        AND impart_time_end = %s 
                        AND active = true) 
                    UNION 
                    SELECT 'conflict' AS result
                    FROM vw_itt_to_verify_data
                    WHERE(
                        teacher_id = %s
                        AND impart_time_start = %s 
                        AND impart_time_end = %s
                    )
                """
        try:
            self.query.cursor.execute(query, (teacher_id, grade, subject, time_starts, time_ends, teacher_id, time_starts, time_ends))
            results = self.query.cursor.fetchone()

            return results is None
        except Exception as e:
            print(f"Error aitt: verify_teacher_time_assign: {e}")
            return False
    
    def load_subjects(self, teacher_id):
        query = f"""
                    SELECT
                    sb.subject
                    FROM subject_teacher sbt
                    INNER JOIN teachers th ON sbt.teacher_id = th.teacher_id
                    INNER JOIN subjects sb ON sbt.subject_id = sb.subject_id
                    WHERE th.teacher_id = %s AND sbt.active = true;
                """
        try:
            self.query.cursor.execute(query,(teacher_id,))
            results = self.query.cursor.fetchall()
            if results and results is not None:
                return results
            else:
                return [('Sin Asignar',),]
        except Exception as e:
            print(f"Error aitt: load_subjects: {e}")
            return None
    
    def load_grades(self, teacher_id):
        query = f"""
                    SELECT
                    g.grade
                    FROM teacher_grade_assigned tga
                    INNER JOIN teachers th ON tga.teacher_id = th.teacher_id
                    INNER JOIN grades g ON tga.grade_id = g.grade_id
                    WHERE th.teacher_id = %s AND tga.active = true;
                """
        try:
            self.query.cursor.execute(query,(teacher_id,))
            results = self.query.cursor.fetchall()
            if results and results is not None:
                return results
            else:
                return [('Sin Asignar',),]
        except Exception as e:
            print(f"Error aitt: load_subjects: {e}")
            return None

    def get_id_tga_and_sbt_existing(self, grade, subject, teacher_id):
        query = f"""
                    SELECT
                    tga.tga_id,
                    sbt.subject_teacher_id
                    FROM teachers th
                    INNER JOIN teacher_grade_assigned tga ON th.teacher_id = tga.teacher_id
                    INNER JOIN subject_teacher sbt ON th.teacher_id = sbt.teacher_id

                    INNER JOIN grades g ON tga.grade_id = g.grade_id
                    INNER JOIN subjects sb ON sbt.subject_id = sb.subject_id

                    WHERE g.grade = %s AND sb.subject = %s AND th.teacher_id = %s AND th.active = true;
                """
        try:
            self.query.cursor.execute(query,(grade, subject, teacher_id,))
            results = self.query.cursor.fetchone()
            if results and results is not None:
                return results
            else:
                return None
        except Exception as e:
            print(f"Error aitt: get_id_tga_and_sbt_existing: {e}")
            return None
    
    def get_subject_id(self, subject):
        query = "SELECT subject_id FROM subjects WHERE subject = %s"
        try:
            self.query.cursor.execute(query,(subject,))
            result = self.query.cursor.fetchone()
            if result and result is not None:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Error aitt: get_subject_id: {e}")
            return None

    def get_grade_id(self, grade):
        query = "SELECT grade_id FROM grades WHERE grade = %s"
        try:
            self.query.cursor.execute(query,(grade,))
            result = self.query.cursor.fetchone()
            if result and result is not None:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Error aitt: get_grade_id: {e}")
            return None

    def assign_impart_time_action(self, teacher_id, grade, subject, time_starts, time_ends, action):
        if not self.verify_teacher_time_assign(teacher_id, grade, subject, time_starts, time_ends):
            return
        match action:
            case "UPDATE": #This is an update action, here the teacher already has the grade and subject assigned
                results = self.get_id_tga_and_sbt_existing(grade, subject, teacher_id)
                grade_id = results[0]
                subject_id = results[1]
                query = f"""
                            INSERT INTO 
                                impart_time_teacher (subject_teacher_id, teacher_grade_assigned_id, impart_time_start, impart_time_end)
                            VALUES
                                (%s, %s, %s, %s);
                        """
                try:
                    self.query.cursor.execute(query,(subject_id, grade_id, time_starts, time_ends,))
                    self.query.connection.commit()
                except Exception as e:
                    print(f"Error aitt: assign_impart_time_action: {e}")
                    self.query.connection.rollback()
            
            case "INSERT": #This is an insert action, if the teacher has not the grade and subject assigned, we need to assign it
                grade_id = self.get_grade_id(grade)
                subject_id = self.get_subject_id(subject)
                if subject_id is None or grade_id is None:
                    return
                
                query_insert_teacher_grade = f"""
                                                INSERT INTO teacher_grade_assigned (teacher_id, grade_id)
                                                VALUES (%s, %s)
                                                RETURNING tga_id;
                                            """
                try:
                    self.query.cursor.execute(query_insert_teacher_grade,(teacher_id, grade_id,))
                    results = self.query.cursor.fetchone()
                    tga_id = results[0]
                except Exception as e:
                    print(f"Error aitt: assign_impart_time_action: {e}")
                    self.query.connection.rollback()
                
                query_insert_subject_teacher = f"""
                                                INSERT INTO subject_teacher (teacher_id, subject_id)
                                                VALUES (%s, %s)
                                                RETURNING subject_teacher_id;
                                                """
                try:
                    self.query.cursor.execute(query_insert_subject_teacher,(teacher_id, subject_id,))
                    results = self.query.cursor.fetchone()
                    sbt_id = results[0]
                except Exception as e:
                    print(f"Error aitt: assign_impart_time_action: {e}")
                    self.query.connection.rollback()
                
                query_insert_impart_time = f"""
                                            INSERT INTO impart_time_teacher (subject_teacher_id, teacher_grade_assigned_id, impart_time_start, impart_time_end)
                                            VALUES (%s, %s, %s, %s);
                                            """
                try:
                    self.query.cursor.execute(query_insert_impart_time,(sbt_id, tga_id, time_starts, time_ends,))
                    self.query.connection.commit()
                except Exception as e:
                    print(f"Error aitt: assign_impart_time_action: {e}")
                    self.query.connection.rollback()
                
            case _:
                return

    def unassing_all_impart_time(self):
        query = "UPDATE impart_time_teacher SET active = false"
        try:
            self.query.cursor.execute(query)
            self.query.connection.commit()
        except Exception as e:
            print(f"Error aitt: unassing_all_impart_time: {e}")
            self.query.connection.rollback()

class access_login_software():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def get_data_table(self):
        query = f"""
                    SELECT
                    st.staff_id,
                    CONCAT_WS(' ', st.first_name, st.middle_name, st.first_surname, st.second_surname) as full_name,
                    lg.log_user,
                    lg.updated_at,
                    lgt.access_type,
                    lg.active
                    FROM login_access lg
                    INNER JOIN staff st ON st.staff_id = lg.staff_id
                    INNER JOIN login_access_type lgt ON lgt.id_access_type = lg.access_type
                """
        try:
            self.query.cursor.execute(query)
            results = self.query.cursor.fetchall()
            if results and results is not None:
                return results
            else:
                return None
        except Exception as e:
            print(f"Error als: get_data_table: {e}")
            return None
    
    def verify_active_login_access(self, staff_id):
        query = "SELECT active FROM staff WHERE staff_id = %s"
        try:
            self.query.cursor.execute(query,(staff_id,))
            result = self.query.cursor.fetchone()
            if result and result[0]:
                if result[0] == True:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(f"Error als: verify_active_login_access: {e}")
            return False

    def add_login_access(self, staff_id, user, password):
        query = "SELECT job_id FROM staff WHERE staff_id = %s"
        self.query.cursor.execute(query, (staff_id,))
        job_id = self.query.cursor.fetchone()
        job_id = job_id[0]

        match job_id:
            case 1:
                access_type = 1
            case 2:
                access_type = 2
        
        query = "SELECT COUNT(*) FROM login_access WHERE staff_id = %s"
        self.query.cursor.execute(query, (staff_id,))
        result = self.query.cursor.fetchone()
        if result[0] > 0:
            update_query = "UPDATE login_access SET log_user = %s, log_password = %s WHERE staff_id = %s"
            try:
                self.query.login_update(staff_id, user, password)
            except Exception as e:
                print(f"Error als: add_login_access: {e}")
        else:
            insert_query = "INSERT INTO login_access (staff_id, log_user, log_password, access_type) VALUES (%s, %s, %s, %s)"
            try:
                self.query.login_insert(staff_id, user, password, access_type,)
            except Exception as e:
                print(f"Error als: add_login_access: {e}")
    
    def deactivate_login_access(self, staff_id, document_id):
        if staff_id is not None:
            query = "UPDATE login_access SET active = false WHERE staff_id = %s"
            try:
                self.query.cursor.execute(query, (staff_id,))
                self.query.connection.commit()
            except Exception as e:
                print(f"Error als: deactivate_login_access: {e}")
                self.query.connection.rollback()
        
        else:
            query = "UPDATE login_access SET active = false WHERE staff_id = (SELECT staff_id FROM staff WHERE document_id = %s)"
            try:
                self.query.cursor.execute(query, (document_id,))
                self.query.connection.commit()
            except Exception as e:
                print(f"Error als: deactivate_login_access: {e}")
                self.query.connection.rollback()

    def verify_id_or_document_id(self, staff_id, document_id):
        if staff_id is not None:
            query = "SELECT staff_id FROM staff WHERE staff_id = %s"
            self.query.cursor.execute(query, (staff_id,))
            result = self.query.cursor.fetchone()
            if result and result[0] is not None:
                return True
            else:
                return False
        else:
            query = "SELECT staff_id FROM staff WHERE document_id = %s"
            self.query.cursor.execute(query, (document_id,))
            result = self.query.cursor.fetchone()
            if result and result[0] is not None:
                return True
            else:
                return False

    def verify_if_login_access_exists(self, staff_id, document_id):
        if staff_id is not None:
            query = "SELECT COUNT(*) FROM login_access WHERE staff_id = %s"
            self.query.cursor.execute(query, (staff_id,))
            result = self.query.cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False
        else:
            query = "SELECT COUNT(*) FROM login_access WHERE staff_id = (SELECT staff_id FROM staff WHERE document_id = %s)"
            self.query.cursor.execute(query, (document_id,))
            result = self.query.cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False

    def get_staff_id_w_document_id(self, document_id):
        query = "SELECT staff_id FROM staff WHERE document_id = %s"
        try:
            self.query.cursor.execute(query, (document_id,))
            result = self.query.cursor.fetchone()
            if result and result is not None:
                return result[0]
            else:
                return " "
        except Exception as e:
            print(f"Error als: get_staff_id_w_document_id: {e}")
            return " "
    
    def verify_if_staff_exists(self, staff_id):
        query = "SELECT COUNT(*) FROM staff WHERE staff_id = %s"
        self.query.cursor.execute(query, (staff_id,))
        result = self.query.cursor.fetchone()
        if result[0] > 0:
            return True
        else:
            return False