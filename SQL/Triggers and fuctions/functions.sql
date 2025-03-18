-- Función: activate_staff_and_teachers
-- Descripción: Activa un miembro del staff y, si su job_id es 2 (profesor), también activa su registro en la tabla teachers.
CREATE FUNCTION public.activate_staff_and_teachers(ast_staff_id integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Verificar si el staff tiene job_id = 2
    IF EXISTS (
        SELECT 1
        FROM staff
        WHERE staff.staff_id = ast_staff_id
          AND job_id = 2  -- Solo si job_id = 2
    ) THEN
        -- Actualizar la tabla staff (active = true)
        UPDATE staff
        SET active = true
        WHERE staff_id = ast_staff_id;

        -- Actualizar la tabla teachers (active = true)
        UPDATE teachers
        SET active = true
        WHERE staff_id = ast_staff_id;

    ELSE
        -- Si job_id es diferente a 2, solo actualizar la tabla staff
        UPDATE staff
        SET active = true
        WHERE staff_id = ast_staff_id;

    END IF;
END;
$$;

-- Función: clear_guide_grade_and_grades_assigned
-- Descripción: Limpia la guía de grado y las calificaciones asignadas a un profesor.
CREATE FUNCTION public.clear_guide_grade_and_grades_assigned(cgg_staff_id integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    UPDATE teachers
    SET guide_grade_id = NULL
    WHERE teacher_id = (
        SELECT teacher_id
        FROM teachers
        WHERE staff_id = cgg_staff_id
    );

    UPDATE teacher_grade_assigned
    SET active = false
    WHERE teacher_id = (
        SELECT teacher_id
        FROM teachers
        WHERE staff_id = cgg_staff_id
    );

    UPDATE impart_time_teacher
    SET active = false
    WHERE teacher_grade_assigned_id = (
        SELECT tga.tga_id
        FROM teacher_grade_assigned tga
        INNER JOIN teachers t ON tga.teacher_id = t.teacher_id
        INNER JOIN staff s ON s.staff_id = t.staff_id
        WHERE t.staff_id = cgg_staff_id
    ) 
    OR 
    subject_teacher_id = (
        SELECT st.subject_teacher_id
        FROM subject_teacher st
        INNER JOIN teachers t ON st.teacher_id = t.teacher_id
        INNER JOIN staff s ON s.staff_id = t.staff_id
        WHERE t.staff_id = cgg_staff_id
    );
END;
$$;

-- Función: clear_main_subject_and_subjects_assigned
-- Descripción: Limpia la materia principal y las materias asignadas a un profesor.
CREATE FUNCTION public.clear_main_subject_and_subjects_assigned(cm_staff_id integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    UPDATE teachers
    SET main_subject = NULL
    WHERE teacher_id = (
        SELECT teacher_id
        FROM teachers
        WHERE staff_id = cm_staff_id
    );

    UPDATE subject_teacher
    SET active = false
    WHERE teacher_id = (
        SELECT teacher_id
        FROM teachers
        WHERE staff_id = cm_staff_id
    );
END;
$$;

-- Función: deactivate_staff_and_teachers
-- Descripción: Desactiva un miembro del staff y, si su job_id es 2 (profesor), también desactiva su registro en la tabla teachers.
CREATE FUNCTION public.deactivate_staff_and_teachers(dst_staff_id integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Verificar si el staff tiene job_id = 2
    IF EXISTS (
        SELECT 1
        FROM staff
        WHERE staff.staff_id = dst_staff_id
          AND job_id = 2  -- Solo si job_id = 2
    ) THEN
        -- Actualizar la tabla staff (active = false)
        UPDATE staff
        SET active = false
        WHERE staff_id = dst_staff_id;

        -- Actualizar la tabla teachers (active = false)
        UPDATE teachers
        SET active = false
        WHERE staff_id = dst_staff_id;

    ELSE
        -- Si job_id es diferente a 2, solo actualizar la tabla staff
        UPDATE staff
        SET active = false
        WHERE staff_id = dst_staff_id;
    END IF;
END;
$$;

-- Función: insert_update_teacher_if_job_id_change_to_2
-- Descripción: Inserta o actualiza un registro en la tabla teachers si el job_id cambia a 2 (profesor).
CREATE FUNCTION public.insert_update_teacher_if_job_id_change_to_2() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Verificar si job_id es 2
    IF NEW.job_id = 2 THEN
        -- Verificar si el staff_id ya existe en teachers
        IF NOT EXISTS (SELECT 1 FROM teachers WHERE staff_id = NEW.staff_id) THEN
            -- Insertar un nuevo registro en teachers con valores predeterminados
            INSERT INTO teachers (staff_id, primary_teacher, guide_grade_id, main_subject)
            VALUES (NEW.staff_id, false, NULL, NULL);  -- Puedes cambiar NULL por valores predeterminados
        END IF;
    END IF;

    RETURN NEW;
END;
$$;

-- Función: notify_subject_change
-- Descripción: Notifica cambios en la tabla subjects mediante pg_notify.
CREATE FUNCTION public.notify_subject_change() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    PERFORM pg_notify('subject_changes', 'update');
    RETURN NEW;
END;
$$;

-- Función: update_related_tables_changing_active_teacher
-- Descripción: Actualiza las tablas relacionadas cuando se cambia el estado activo de un profesor.
CREATE FUNCTION public.update_related_tables_changing_active_teacher() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF NEW.active = FALSE THEN
        -- Actualizar la tabla "teacher_grade_assigned"
        UPDATE teacher_grade_assigned
        SET active = false
        WHERE teacher_id = NEW.teacher_id;

        -- Actualizar la tabla "subject_teacher"
        UPDATE subject_teacher
        SET active = false
        WHERE teacher_id = NEW.teacher_id;

        -- Actualizar la tabla "impart_time_teacher" basado en las tablas relacionadas
        UPDATE impart_time_teacher
        SET active = false
        WHERE subject_teacher_id IN (
            SELECT subject_teacher_id FROM subject_teacher WHERE teacher_id = NEW.teacher_id
        )
        OR teacher_grade_assigned_id IN (
            SELECT tga_id FROM teacher_grade_assigned WHERE teacher_id = NEW.teacher_id
        );
    END IF;

    RETURN NEW;
END;
$$;

-- Función: update_teacher_grade_assigned_active
-- Descripción: Actualiza el estado activo de los grados asignados a un profesor según si es profesor de primaria o secundaria.
CREATE FUNCTION public.update_teacher_grade_assigned_active() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Si primary_teacher es TRUE, activar grados de nivel 1 y desactivar grados de nivel 2
    IF NEW.primary_teacher = TRUE THEN
        -- Activar grados de nivel 1 (primaria)
        UPDATE teacher_grade_assigned tga
        SET active = FALSE
        FROM grades g
        WHERE tga.grade_id = g.grade_id
          AND g.education_level_id = 1
          AND tga.teacher_id = NEW.teacher_id;

        -- Desactivar grados de nivel 2 (secundaria)
        UPDATE teacher_grade_assigned tga
        SET active = FALSE
        FROM grades g
        WHERE tga.grade_id = g.grade_id
          AND g.education_level_id = 2
          AND tga.teacher_id = NEW.teacher_id;
    END IF;

    -- Si primary_teacher es FALSE, activar grados de nivel 2 y desactivar grados de nivel 1
    IF NEW.primary_teacher = FALSE THEN
        -- Activar grados de nivel 2 (secundaria)
        UPDATE teacher_grade_assigned tga
        SET active = FALSE
        FROM grades g
        WHERE tga.grade_id = g.grade_id
          AND g.education_level_id = 2
          AND tga.teacher_id = NEW.teacher_id;

        -- Desactivar grados de nivel 1 (primaria)
        UPDATE teacher_grade_assigned tga
        SET active = FALSE
        FROM grades g
        WHERE tga.grade_id = g.grade_id
          AND g.education_level_id = 1
          AND tga.teacher_id = NEW.teacher_id;
    END IF;

    RETURN NEW;
END;
$$;

-- Función: update_teachers_active_related_job_id_staff
-- Descripción: Actualiza el estado activo de los profesores según el job_id del staff.
CREATE FUNCTION public.update_teachers_active_related_job_id_staff() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Si job_position es diferente de 2, desactivar en teachers
    IF NEW.job_id <> 2 THEN
        UPDATE teachers
        SET active = FALSE
        WHERE staff_id = NEW.staff_id;
    END IF;

    -- Si job_position es 2, activar en teachers
    IF NEW.job_id = 2 THEN
        UPDATE teachers
        SET active = TRUE
        WHERE staff_id = NEW.staff_id;
    END IF;

    RETURN NEW;
END;
$$;

-- Función: update_teachers_if_staff_active
-- Descripción: Actualiza el estado activo de los profesores si el staff está activo.
CREATE FUNCTION public.update_teachers_if_staff_active(utsa_staff_id integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM staff
        WHERE staff.staff_id = utsa_staff_id
          AND active = true
    ) THEN
        UPDATE teachers
        SET active = true
        WHERE teachers.staff_id = utsa_staff_id;
    END IF;
END;
$$;

-- Función: update_teachers_if_staff_inactive
-- Descripción: Actualiza el estado activo de los profesores si el staff está inactivo.
CREATE FUNCTION public.update_teachers_if_staff_inactive(utsi_staff_id integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM staff
        WHERE staff.staff_id = utsi_staff_id
          AND active = false
    ) THEN
        UPDATE teachers
        SET teachers.active = false
        WHERE staff_id = utsi_staff_id;
    END IF;
END;
$$;

-- Función: update_timestamp
-- Descripción: Actualiza el campo updated_at con la fecha y hora actuales.
CREATE FUNCTION public.update_timestamp() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

-- Función: update_login_access_on_job_change
-- Descripción: Actualiza el acceso de un usuario según el cambio de job_id.
CREATE OR REPLACE FUNCTION update_login_access_on_job_change()
RETURNS TRIGGER AS $$
BEGIN

    IF (OLD.job_id = 1 AND NEW.job_id = 2) OR (OLD.job_id = 2 AND NEW.job_id = 1) THEN

        UPDATE public.login_access
        SET access_type = NEW.job_id,
            active = true
        WHERE staff_id = NEW.staff_id;
    ELSIF NEW.job_id = 3 THEN

        UPDATE public.login_access
        SET access_type = NULL,
            active = false
        WHERE staff_id = NEW.staff_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- función: update_login_access_on_active_change
-- Descripción: Actualiza el acceso de un usuario según el cambio de estado activo, si esta active = false, se removera el acceso, de caso contrario se activara y tendra su acceso
CREATE OR REPLACE FUNCTION update_login_access_on_active_change()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.active IS DISTINCT FROM NEW.active AND (NEW.job_id = 1 OR NEW.job_id = 2) THEN
        UPDATE public.login_access
        SET active = NEW.active
        WHERE staff_id = NEW.staff_id;
    END IF;
	
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;