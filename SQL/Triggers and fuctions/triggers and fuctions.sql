--Trigger--
CREATE TRIGGER update_students_timestamp BEFORE UPDATE ON public.students FOR EACH ROW EXECUTE FUNCTION update_timestamp()

CREATE TRIGGER update_staffs_timestamp BEFORE UPDATE ON public.staff FOR EACH ROW EXECUTE FUNCTION update_timestamp()

CREATE TRIGGER update_student_representatives_timestamp BEFORE UPDATE ON public.student_representative FOR EACH ROW EXECUTE FUNCTION update_timestamp()

CREATE OR REPLACE FUNCTION public.update_timestamp()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$function$

--This allow to get the update time when its update this tables:--
--students
--staffs
--student_representatives