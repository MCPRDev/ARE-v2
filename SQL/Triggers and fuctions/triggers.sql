-- Trigger: trigger_insert_update_teacher_if_job_id_change_to_2
-- Descripción: Se ejecuta después de actualizar el job_id en la tabla staff. Si el job_id es 2, inserta o actualiza un registro en la tabla teachers.
CREATE TRIGGER trigger_insert_update_teacher_if_job_id_change_to_2 
AFTER UPDATE OF job_id ON public.staff 
FOR EACH ROW 
EXECUTE FUNCTION public.insert_update_teacher_if_job_id_change_to_2();

-- Trigger: trigger_subject_change
-- Descripción: Se ejecuta después de insertar, eliminar o actualizar registros en la tabla subjects. Notifica cambios mediante pg_notify.
CREATE TRIGGER trigger_subject_change 
AFTER INSERT OR DELETE OR UPDATE ON public.subjects 
FOR EACH ROW 
EXECUTE FUNCTION public.notify_subject_change();

-- Trigger: trigger_update_related_tables_changing_active_teacher
-- Descripción: Se ejecuta después de actualizar el campo active en la tabla teachers. Actualiza las tablas relacionadas (teacher_grade_assigned, subject_teacher, impart_time_teacher) si el profesor se desactiva.
CREATE TRIGGER trigger_update_related_tables_changing_active_teacher 
AFTER UPDATE ON public.teachers 
FOR EACH ROW 
EXECUTE FUNCTION public.update_related_tables_changing_active_teacher();

-- Trigger: trigger_update_teacher_grade_assigned
-- Descripción: Se ejecuta después de actualizar el campo primary_teacher en la tabla teachers. Actualiza el estado activo de los grados asignados según si el profesor es de primaria o secundaria.
CREATE TRIGGER trigger_update_teacher_grade_assigned 
AFTER UPDATE OF primary_teacher ON public.teachers 
FOR EACH ROW 
EXECUTE FUNCTION public.update_teacher_grade_assigned_active();

-- Trigger: trigger_update_teachers_active_related_job_id_staff
-- Descripción: Se ejecuta después de actualizar el job_id en la tabla staff. Actualiza el estado activo de los profesores según el job_id.
CREATE TRIGGER trigger_update_teachers_active_related_job_id_staff 
AFTER UPDATE OF job_id ON public.staff 
FOR EACH ROW 
EXECUTE FUNCTION public.update_teachers_active_related_job_id_staff();

-- Trigger: update_score_grades_timestamp
-- Descripción: Se ejecuta antes de actualizar un registro en la tabla score_grades. Actualiza el campo updated_at con la fecha y hora actuales.
CREATE TRIGGER update_score_grades_timestamp 
BEFORE UPDATE ON public.score_grades 
FOR EACH ROW 
EXECUTE FUNCTION public.update_timestamp();

-- Trigger: update_staffs_timestamp
-- Descripción: Se ejecuta antes de actualizar un registro en la tabla staff. Actualiza el campo updated_at con la fecha y hora actuales.
CREATE TRIGGER update_staffs_timestamp 
BEFORE UPDATE ON public.staff 
FOR EACH ROW 
EXECUTE FUNCTION public.update_timestamp();

-- Trigger: update_student_representatives_timestamp
-- Descripción: Se ejecuta antes de actualizar un registro en la tabla student_representative. Actualiza el campo updated_at con la fecha y hora actuales.
CREATE TRIGGER update_student_representatives_timestamp 
BEFORE UPDATE ON public.student_representative 
FOR EACH ROW 
EXECUTE FUNCTION public.update_timestamp();

-- Trigger: update_students_timestamp
-- Descripción: Se ejecuta antes de actualizar un registro en la tabla students. Actualiza el campo updated_at con la fecha y hora actuales.
CREATE TRIGGER update_students_timestamp 
BEFORE UPDATE ON public.students 
FOR EACH ROW 
EXECUTE FUNCTION public.update_timestamp();

-- Trigger: update_subjects_timestamp
-- Descripción: Se ejecuta antes de actualizar un registro en la tabla login_access. Actualiza el campo updated_at con la fecha y hora actuales.

CREATE TRIGGER update_login_access_timestamp
BEFORE UPDATE ON public.login_access
FOR EACH ROW
EXECUTE FUNCTION public.update_timestamp();

-- Trigger: staff_job_id_change_trigger
-- Descripción: Se ejecuta después de actualizar el job_id en la tabla staff. Actualiza el acceso a la plataforma según el job_id.
CREATE TRIGGER staff_job_id_change_trigger
AFTER UPDATE OF job_id ON public.staff
FOR EACH ROW
EXECUTE FUNCTION public.update_login_access_on_job_change();

-- Trigger: staff_active_change_trigger
-- Descripción: Se ejecuta después de actualizar el campo active en la tabla staff. Actualiza el acceso a la plataforma según el estado activo.
CREATE TRIGGER staff_active_change_trigger
AFTER UPDATE OF active ON public.staff
FOR EACH ROW
EXECUTE FUNCTION update_login_access_on_active_change();