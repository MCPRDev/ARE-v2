--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2025-03-17 23:50:06

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 270 (class 1255 OID 114717)
-- Name: activate_staff_and_teachers(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.activate_staff_and_teachers(ast_staff_id integer) OWNER TO postgres;

--
-- TOC entry 254 (class 1255 OID 114697)
-- Name: clear_guide_grade_and_grades_assigned(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.clear_guide_grade_and_grades_assigned(cgg_staff_id integer) OWNER TO postgres;

--
-- TOC entry 252 (class 1255 OID 114696)
-- Name: clear_main_subject_and_subjects_assigned(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.clear_main_subject_and_subjects_assigned(cm_staff_id integer) OWNER TO postgres;

--
-- TOC entry 271 (class 1255 OID 114718)
-- Name: deactivate_staff_and_teachers(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.deactivate_staff_and_teachers(dst_staff_id integer) OWNER TO postgres;

--
-- TOC entry 266 (class 1255 OID 114708)
-- Name: insert_update_teacher_if_job_id_change_to_2(); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.insert_update_teacher_if_job_id_change_to_2() OWNER TO postgres;

--
-- TOC entry 249 (class 1255 OID 98315)
-- Name: notify_subject_change(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.notify_subject_change() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    PERFORM pg_notify('subject_changes', 'update');
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.notify_subject_change() OWNER TO postgres;

--
-- TOC entry 250 (class 1255 OID 114751)
-- Name: update_login_access_on_active_change(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_login_access_on_active_change() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF OLD.active IS DISTINCT FROM NEW.active AND (NEW.job_id = 1 OR NEW.job_id = 2) THEN
        UPDATE public.login_access
        SET active = NEW.active
        WHERE staff_id = NEW.staff_id;
    END IF;
	
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_login_access_on_active_change() OWNER TO postgres;

--
-- TOC entry 272 (class 1255 OID 114749)
-- Name: update_login_access_on_job_change(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_login_access_on_job_change() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Verificar si el job_id ha cambiado de 1 a 2 o de 2 a 1
    IF (OLD.job_id = 1 AND NEW.job_id = 2) OR (OLD.job_id = 2 AND NEW.job_id = 1) THEN
        -- Actualizar el access_type en login_access
        UPDATE public.login_access
        SET access_type = NEW.job_id,
            active = true
        WHERE staff_id = NEW.staff_id;
    ELSIF NEW.job_id = 3 THEN
        -- Si el job_id es 3, desactivar el acceso
        UPDATE public.login_access
        SET access_type = NULL,
            active = false
        WHERE staff_id = NEW.staff_id;
    END IF;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_login_access_on_job_change() OWNER TO postgres;

--
-- TOC entry 251 (class 1255 OID 114692)
-- Name: update_related_tables_changing_active_teacher(); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.update_related_tables_changing_active_teacher() OWNER TO postgres;

--
-- TOC entry 267 (class 1255 OID 114703)
-- Name: update_teacher_grade_assigned_active(); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.update_teacher_grade_assigned_active() OWNER TO postgres;

--
-- TOC entry 253 (class 1255 OID 114705)
-- Name: update_teachers_active_related_job_id_staff(); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.update_teachers_active_related_job_id_staff() OWNER TO postgres;

--
-- TOC entry 268 (class 1255 OID 114713)
-- Name: update_teachers_if_staff_active(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.update_teachers_if_staff_active(utsa_staff_id integer) OWNER TO postgres;

--
-- TOC entry 269 (class 1255 OID 114714)
-- Name: update_teachers_if_staff_inactive(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

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


ALTER FUNCTION public.update_teachers_if_staff_inactive(utsi_staff_id integer) OWNER TO postgres;

--
-- TOC entry 248 (class 1255 OID 49157)
-- Name: update_timestamp(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_timestamp() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_timestamp() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 24637)
-- Name: education_levels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.education_levels (
    education_level_id integer NOT NULL,
    education_level character varying(45)
);


ALTER TABLE public.education_levels OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 24636)
-- Name: education_levels_education_level_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.education_levels_education_level_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.education_levels_education_level_id_seq OWNER TO postgres;

--
-- TOC entry 4990 (class 0 OID 0)
-- Dependencies: 225
-- Name: education_levels_education_level_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.education_levels_education_level_id_seq OWNED BY public.education_levels.education_level_id;


--
-- TOC entry 228 (class 1259 OID 32773)
-- Name: grades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.grades (
    grade_id integer NOT NULL,
    grade character varying(50),
    education_level_id integer,
    bachelor boolean
);


ALTER TABLE public.grades OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 32772)
-- Name: grades_grade_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.grades_grade_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.grades_grade_id_seq OWNER TO postgres;

--
-- TOC entry 4991 (class 0 OID 0)
-- Dependencies: 227
-- Name: grades_grade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.grades_grade_id_seq OWNED BY public.grades.grade_id;


--
-- TOC entry 243 (class 1259 OID 73733)
-- Name: impart_time_teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.impart_time_teacher (
    itt_id integer NOT NULL,
    subject_teacher_id integer,
    teacher_grade_assigned_id integer,
    impart_time_start time without time zone,
    impart_time_end time without time zone,
    active boolean DEFAULT true
);


ALTER TABLE public.impart_time_teacher OWNER TO postgres;

--
-- TOC entry 242 (class 1259 OID 73732)
-- Name: impart_time_teacher_itt_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.impart_time_teacher_itt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.impart_time_teacher_itt_id_seq OWNER TO postgres;

--
-- TOC entry 4992 (class 0 OID 0)
-- Dependencies: 242
-- Name: impart_time_teacher_itt_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.impart_time_teacher_itt_id_seq OWNED BY public.impart_time_teacher.itt_id;


--
-- TOC entry 218 (class 1259 OID 24582)
-- Name: job_position; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.job_position (
    job_id integer NOT NULL,
    job_position character varying(60) NOT NULL
);


ALTER TABLE public.job_position OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 24581)
-- Name: job_position_job_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.job_position_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.job_position_job_id_seq OWNER TO postgres;

--
-- TOC entry 4993 (class 0 OID 0)
-- Dependencies: 217
-- Name: job_position_job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.job_position_job_id_seq OWNED BY public.job_position.job_id;


--
-- TOC entry 222 (class 1259 OID 24614)
-- Name: login_access; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_access (
    access_id integer NOT NULL,
    staff_id integer,
    log_user character varying(25) NOT NULL,
    log_password character varying(255) NOT NULL,
    access_type integer,
    active boolean DEFAULT true,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.login_access OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24613)
-- Name: login_access_access_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_access_access_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.login_access_access_id_seq OWNER TO postgres;

--
-- TOC entry 4994 (class 0 OID 0)
-- Dependencies: 221
-- Name: login_access_access_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_access_access_id_seq OWNED BY public.login_access.access_id;


--
-- TOC entry 237 (class 1259 OID 57348)
-- Name: login_access_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_access_type (
    id_access_type integer NOT NULL,
    access_type character varying(25),
    active boolean
);


ALTER TABLE public.login_access_type OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 41020)
-- Name: retired_students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.retired_students (
    retired_id integer NOT NULL,
    register_id integer,
    representative_id integer,
    retired_date date,
    motive character varying(300)
);


ALTER TABLE public.retired_students OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 41019)
-- Name: retired_students_retired_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.retired_students_retired_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.retired_students_retired_id_seq OWNER TO postgres;

--
-- TOC entry 4995 (class 0 OID 0)
-- Dependencies: 235
-- Name: retired_students_retired_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.retired_students_retired_id_seq OWNED BY public.retired_students.retired_id;


--
-- TOC entry 245 (class 1259 OID 106510)
-- Name: score_grades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.score_grades (
    score_grade_id integer NOT NULL,
    tga_id integer,
    register_student_id integer,
    subject_teacher_id integer,
    score_grade numeric(3,2),
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.score_grades OWNER TO postgres;

--
-- TOC entry 244 (class 1259 OID 106509)
-- Name: score_grades_score_grade_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.score_grades_score_grade_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.score_grades_score_grade_id_seq OWNER TO postgres;

--
-- TOC entry 4996 (class 0 OID 0)
-- Dependencies: 244
-- Name: score_grades_score_grade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.score_grades_score_grade_id_seq OWNED BY public.score_grades.score_grade_id;


--
-- TOC entry 220 (class 1259 OID 24589)
-- Name: staff; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.staff (
    staff_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    middle_name character varying(50),
    first_surname character varying(50) NOT NULL,
    second_surname character varying(50),
    document_id character varying(20) NOT NULL,
    address character varying(250) NOT NULL,
    job_id integer,
    active boolean DEFAULT true,
    phone_number character varying(15),
    birthday date,
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.staff OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 24588)
-- Name: staff_staff_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.staff_staff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.staff_staff_id_seq OWNER TO postgres;

--
-- TOC entry 4997 (class 0 OID 0)
-- Dependencies: 219
-- Name: staff_staff_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.staff_staff_id_seq OWNED BY public.staff.staff_id;


--
-- TOC entry 232 (class 1259 OID 40965)
-- Name: student_representative; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_representative (
    representative_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    middle_name character varying(50),
    first_surname character varying(50) NOT NULL,
    second_surname character varying(50),
    representative_document_id character varying(25),
    residential_address character varying(250),
    phone_number character varying(15),
    active boolean DEFAULT true,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.student_representative OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 40964)
-- Name: student_representative_representative_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_representative_representative_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.student_representative_representative_id_seq OWNER TO postgres;

--
-- TOC entry 4998 (class 0 OID 0)
-- Dependencies: 231
-- Name: student_representative_representative_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_representative_representative_id_seq OWNED BY public.student_representative.representative_id;


--
-- TOC entry 234 (class 1259 OID 40974)
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    register_id integer NOT NULL,
    student_code character varying(50) NOT NULL,
    student_center_code character varying(50),
    first_name character varying(50) NOT NULL,
    middle_name character varying(50),
    first_surname character varying(50) NOT NULL,
    second_surname character varying(50),
    birthday date NOT NULL,
    grade_id integer,
    representative_id integer,
    active boolean DEFAULT true,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.students OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 40973)
-- Name: students_register_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.students_register_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.students_register_id_seq OWNER TO postgres;

--
-- TOC entry 4999 (class 0 OID 0)
-- Dependencies: 233
-- Name: students_register_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_register_id_seq OWNED BY public.students.register_id;


--
-- TOC entry 239 (class 1259 OID 65541)
-- Name: subject_teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subject_teacher (
    subject_teacher_id integer NOT NULL,
    teacher_id integer,
    subject_id integer,
    active boolean DEFAULT true
);


ALTER TABLE public.subject_teacher OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 65540)
-- Name: subject_teacher_subject_teacher_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subject_teacher_subject_teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subject_teacher_subject_teacher_id_seq OWNER TO postgres;

--
-- TOC entry 5000 (class 0 OID 0)
-- Dependencies: 238
-- Name: subject_teacher_subject_teacher_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subject_teacher_subject_teacher_id_seq OWNED BY public.subject_teacher.subject_teacher_id;


--
-- TOC entry 224 (class 1259 OID 24630)
-- Name: subjects; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subjects (
    subject_id integer NOT NULL,
    subject character varying(50),
    active boolean DEFAULT true
);


ALTER TABLE public.subjects OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 24629)
-- Name: subjects_subject_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subjects_subject_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subjects_subject_id_seq OWNER TO postgres;

--
-- TOC entry 5001 (class 0 OID 0)
-- Dependencies: 223
-- Name: subjects_subject_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subjects_subject_id_seq OWNED BY public.subjects.subject_id;


--
-- TOC entry 241 (class 1259 OID 65565)
-- Name: teacher_grade_assigned; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher_grade_assigned (
    tga_id integer NOT NULL,
    teacher_id integer,
    grade_id integer,
    active boolean DEFAULT true
);


ALTER TABLE public.teacher_grade_assigned OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 32797)
-- Name: teachers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teachers (
    teacher_id integer NOT NULL,
    staff_id integer,
    primary_teacher boolean DEFAULT false,
    guide_grade_id integer,
    active boolean DEFAULT true,
    main_subject integer
);


ALTER TABLE public.teachers OWNER TO postgres;

--
-- TOC entry 247 (class 1259 OID 114736)
-- Name: teacher_assigned_and_not_assigned_impart_time; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.teacher_assigned_and_not_assigned_impart_time AS
 SELECT th.teacher_id,
    initcap(concat_ws(' '::text, st.first_name, st.middle_name, st.first_surname, st.second_surname)) AS full_name,
    g.grade AS guide_grade,
    sb.subject AS main_subject,
    g2.grade AS teacher_grade_assigned,
    sb2.subject AS subject_teacher_assigned,
    itt.impart_time_start,
    itt.impart_time_end
   FROM ((((((((public.impart_time_teacher itt
     JOIN public.teacher_grade_assigned tga ON ((tga.tga_id = itt.teacher_grade_assigned_id)))
     JOIN public.subject_teacher sbt ON ((sbt.subject_teacher_id = itt.subject_teacher_id)))
     JOIN public.teachers th ON ((th.teacher_id = sbt.teacher_id)))
     LEFT JOIN public.grades g ON ((g.grade_id = th.guide_grade_id)))
     JOIN public.grades g2 ON ((g2.grade_id = tga.grade_id)))
     LEFT JOIN public.subjects sb ON ((sb.subject_id = th.main_subject)))
     JOIN public.subjects sb2 ON ((sb2.subject_id = sbt.subject_id)))
     JOIN public.staff st ON ((st.staff_id = th.staff_id)))
  WHERE (itt.active = true)
UNION
 SELECT th.teacher_id,
    initcap(concat_ws(' '::text, st.first_name, st.middle_name, st.first_surname, st.second_surname)) AS full_name,
    g.grade AS guide_grade,
    sb.subject AS main_subject,
    g2.grade AS teacher_grade_assigned,
    sb2.subject AS subject_teacher_assigned,
    itt.impart_time_start,
    itt.impart_time_end
   FROM ((((((((public.teachers th
     LEFT JOIN public.grades g ON ((g.grade_id = th.guide_grade_id)))
     LEFT JOIN public.subjects sb ON ((sb.subject_id = th.main_subject)))
     JOIN public.staff st ON ((st.staff_id = th.staff_id)))
     LEFT JOIN public.subject_teacher sbt ON (((sbt.teacher_id = th.teacher_id) AND (sbt.active = true))))
     LEFT JOIN public.subjects sb2 ON ((sb2.subject_id = sbt.subject_id)))
     LEFT JOIN public.teacher_grade_assigned tga ON (((tga.teacher_id = th.teacher_id) AND (tga.active = true))))
     LEFT JOIN public.grades g2 ON ((g2.grade_id = tga.grade_id)))
     LEFT JOIN public.impart_time_teacher itt ON (((itt.teacher_grade_assigned_id = tga.tga_id) AND (itt.subject_teacher_id = sbt.subject_teacher_id) AND (itt.active = true))))
  WHERE ((th.active = true) AND (tga.tga_id IS NOT NULL) AND (sbt.subject_teacher_id IS NOT NULL) AND ((itt.impart_time_start IS NULL) OR (itt.impart_time_end IS NULL)));


ALTER VIEW public.teacher_assigned_and_not_assigned_impart_time OWNER TO postgres;

--
-- TOC entry 240 (class 1259 OID 65564)
-- Name: teacher_grade_assigned_tga_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teacher_grade_assigned_tga_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.teacher_grade_assigned_tga_id_seq OWNER TO postgres;

--
-- TOC entry 5002 (class 0 OID 0)
-- Dependencies: 240
-- Name: teacher_grade_assigned_tga_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teacher_grade_assigned_tga_id_seq OWNED BY public.teacher_grade_assigned.tga_id;


--
-- TOC entry 229 (class 1259 OID 32796)
-- Name: teachers_teacher_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teachers_teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.teachers_teacher_id_seq OWNER TO postgres;

--
-- TOC entry 5003 (class 0 OID 0)
-- Dependencies: 229
-- Name: teachers_teacher_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teachers_teacher_id_seq OWNED BY public.teachers.teacher_id;


--
-- TOC entry 246 (class 1259 OID 114731)
-- Name: vw_itt_to_verify_data; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.vw_itt_to_verify_data AS
 SELECT itt.itt_id,
    th.teacher_id,
    g.grade,
    sb.subject,
    itt.impart_time_start,
    itt.impart_time_end,
    itt.active
   FROM (((((public.impart_time_teacher itt
     JOIN public.subject_teacher sbt ON ((itt.subject_teacher_id = sbt.subject_teacher_id)))
     JOIN public.teacher_grade_assigned tga ON ((tga.tga_id = itt.teacher_grade_assigned_id)))
     JOIN public.subjects sb ON ((sb.subject_id = sbt.subject_id)))
     JOIN public.grades g ON ((g.grade_id = tga.grade_id)))
     JOIN public.teachers th ON ((th.teacher_id = tga.teacher_id)))
  WHERE (itt.active = true);


ALTER VIEW public.vw_itt_to_verify_data OWNER TO postgres;

--
-- TOC entry 4742 (class 2604 OID 24640)
-- Name: education_levels education_level_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.education_levels ALTER COLUMN education_level_id SET DEFAULT nextval('public.education_levels_education_level_id_seq'::regclass);


--
-- TOC entry 4743 (class 2604 OID 32776)
-- Name: grades grade_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grades ALTER COLUMN grade_id SET DEFAULT nextval('public.grades_grade_id_seq'::regclass);


--
-- TOC entry 4760 (class 2604 OID 73736)
-- Name: impart_time_teacher itt_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.impart_time_teacher ALTER COLUMN itt_id SET DEFAULT nextval('public.impart_time_teacher_itt_id_seq'::regclass);


--
-- TOC entry 4732 (class 2604 OID 24585)
-- Name: job_position job_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_position ALTER COLUMN job_id SET DEFAULT nextval('public.job_position_job_id_seq'::regclass);


--
-- TOC entry 4737 (class 2604 OID 24617)
-- Name: login_access access_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_access ALTER COLUMN access_id SET DEFAULT nextval('public.login_access_access_id_seq'::regclass);


--
-- TOC entry 4755 (class 2604 OID 41023)
-- Name: retired_students retired_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.retired_students ALTER COLUMN retired_id SET DEFAULT nextval('public.retired_students_retired_id_seq'::regclass);


--
-- TOC entry 4762 (class 2604 OID 106513)
-- Name: score_grades score_grade_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.score_grades ALTER COLUMN score_grade_id SET DEFAULT nextval('public.score_grades_score_grade_id_seq'::regclass);


--
-- TOC entry 4733 (class 2604 OID 24592)
-- Name: staff staff_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff ALTER COLUMN staff_id SET DEFAULT nextval('public.staff_staff_id_seq'::regclass);


--
-- TOC entry 4747 (class 2604 OID 40968)
-- Name: student_representative representative_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_representative ALTER COLUMN representative_id SET DEFAULT nextval('public.student_representative_representative_id_seq'::regclass);


--
-- TOC entry 4751 (class 2604 OID 40977)
-- Name: students register_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN register_id SET DEFAULT nextval('public.students_register_id_seq'::regclass);


--
-- TOC entry 4756 (class 2604 OID 65544)
-- Name: subject_teacher subject_teacher_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_teacher ALTER COLUMN subject_teacher_id SET DEFAULT nextval('public.subject_teacher_subject_teacher_id_seq'::regclass);


--
-- TOC entry 4740 (class 2604 OID 24633)
-- Name: subjects subject_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subjects ALTER COLUMN subject_id SET DEFAULT nextval('public.subjects_subject_id_seq'::regclass);


--
-- TOC entry 4758 (class 2604 OID 65568)
-- Name: teacher_grade_assigned tga_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_grade_assigned ALTER COLUMN tga_id SET DEFAULT nextval('public.teacher_grade_assigned_tga_id_seq'::regclass);


--
-- TOC entry 4744 (class 2604 OID 32800)
-- Name: teachers teacher_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers ALTER COLUMN teacher_id SET DEFAULT nextval('public.teachers_teacher_id_seq'::regclass);


--
-- TOC entry 4780 (class 2606 OID 24642)
-- Name: education_levels education_levels_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.education_levels
    ADD CONSTRAINT education_levels_pkey PRIMARY KEY (education_level_id);


--
-- TOC entry 4782 (class 2606 OID 32778)
-- Name: grades grades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grades
    ADD CONSTRAINT grades_pkey PRIMARY KEY (grade_id);


--
-- TOC entry 4806 (class 2606 OID 73738)
-- Name: impart_time_teacher impart_time_teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.impart_time_teacher
    ADD CONSTRAINT impart_time_teacher_pkey PRIMARY KEY (itt_id);


--
-- TOC entry 4766 (class 2606 OID 24587)
-- Name: job_position job_position_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_position
    ADD CONSTRAINT job_position_pkey PRIMARY KEY (job_id);


--
-- TOC entry 4772 (class 2606 OID 114746)
-- Name: login_access login_access_log_password_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_access
    ADD CONSTRAINT login_access_log_password_key UNIQUE (log_password);


--
-- TOC entry 4774 (class 2606 OID 24621)
-- Name: login_access login_access_log_user_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_access
    ADD CONSTRAINT login_access_log_user_key UNIQUE (log_user);


--
-- TOC entry 4776 (class 2606 OID 24619)
-- Name: login_access login_access_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_access
    ADD CONSTRAINT login_access_pkey PRIMARY KEY (access_id);


--
-- TOC entry 4794 (class 2606 OID 57352)
-- Name: login_access_type login_access_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_access_type
    ADD CONSTRAINT login_access_type_pkey PRIMARY KEY (id_access_type);


--
-- TOC entry 4792 (class 2606 OID 41025)
-- Name: retired_students retired_students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.retired_students
    ADD CONSTRAINT retired_students_pkey PRIMARY KEY (retired_id);


--
-- TOC entry 4808 (class 2606 OID 106517)
-- Name: score_grades score_grades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.score_grades
    ADD CONSTRAINT score_grades_pkey PRIMARY KEY (score_grade_id);


--
-- TOC entry 4768 (class 2606 OID 24596)
-- Name: staff staff_document_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_document_id_key UNIQUE (document_id);


--
-- TOC entry 4770 (class 2606 OID 24594)
-- Name: staff staff_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (staff_id);


--
-- TOC entry 4786 (class 2606 OID 40970)
-- Name: student_representative student_representative_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_representative
    ADD CONSTRAINT student_representative_pkey PRIMARY KEY (representative_id);


--
-- TOC entry 4788 (class 2606 OID 40972)
-- Name: student_representative student_representative_representative_document_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_representative
    ADD CONSTRAINT student_representative_representative_document_id_key UNIQUE (representative_document_id);


--
-- TOC entry 4790 (class 2606 OID 40979)
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (register_id);


--
-- TOC entry 4796 (class 2606 OID 65546)
-- Name: subject_teacher subject_teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_teacher
    ADD CONSTRAINT subject_teacher_pkey PRIMARY KEY (subject_teacher_id);


--
-- TOC entry 4798 (class 2606 OID 65548)
-- Name: subject_teacher subject_teacher_teacher_id_subject_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_teacher
    ADD CONSTRAINT subject_teacher_teacher_id_subject_id_key UNIQUE (teacher_id, subject_id);


--
-- TOC entry 4778 (class 2606 OID 24635)
-- Name: subjects subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (subject_id);


--
-- TOC entry 4802 (class 2606 OID 65570)
-- Name: teacher_grade_assigned teacher_grade_assigned_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_grade_assigned
    ADD CONSTRAINT teacher_grade_assigned_pkey PRIMARY KEY (tga_id);


--
-- TOC entry 4784 (class 2606 OID 32802)
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (teacher_id);


--
-- TOC entry 4804 (class 2606 OID 114701)
-- Name: teacher_grade_assigned unique_teacher_grade_assigned; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_grade_assigned
    ADD CONSTRAINT unique_teacher_grade_assigned UNIQUE (teacher_id, grade_id);


--
-- TOC entry 4800 (class 2606 OID 114699)
-- Name: subject_teacher unique_teacher_subject; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_teacher
    ADD CONSTRAINT unique_teacher_subject UNIQUE (teacher_id, subject_id);


--
-- TOC entry 4826 (class 2620 OID 114752)
-- Name: staff staff_active_change_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER staff_active_change_trigger AFTER UPDATE OF active ON public.staff FOR EACH ROW EXECUTE FUNCTION public.update_login_access_on_active_change();


--
-- TOC entry 4827 (class 2620 OID 114750)
-- Name: staff staff_job_id_change_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER staff_job_id_change_trigger AFTER UPDATE OF job_id ON public.staff FOR EACH ROW EXECUTE FUNCTION public.update_login_access_on_job_change();


--
-- TOC entry 4828 (class 2620 OID 114709)
-- Name: staff trigger_insert_update_teacher_if_job_id_change_to_2; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_insert_update_teacher_if_job_id_change_to_2 AFTER UPDATE OF job_id ON public.staff FOR EACH ROW EXECUTE FUNCTION public.insert_update_teacher_if_job_id_change_to_2();


--
-- TOC entry 4832 (class 2620 OID 98317)
-- Name: subjects trigger_subject_change; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_subject_change AFTER INSERT OR DELETE OR UPDATE ON public.subjects FOR EACH ROW EXECUTE FUNCTION public.notify_subject_change();


--
-- TOC entry 4833 (class 2620 OID 114693)
-- Name: teachers trigger_update_related_tables_changing_active_teacher; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_update_related_tables_changing_active_teacher AFTER UPDATE ON public.teachers FOR EACH ROW EXECUTE FUNCTION public.update_related_tables_changing_active_teacher();


--
-- TOC entry 4834 (class 2620 OID 114704)
-- Name: teachers trigger_update_teacher_grade_assigned; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_update_teacher_grade_assigned AFTER UPDATE OF primary_teacher ON public.teachers FOR EACH ROW EXECUTE FUNCTION public.update_teacher_grade_assigned_active();


--
-- TOC entry 4829 (class 2620 OID 114707)
-- Name: staff trigger_update_teachers_active_related_job_id_staff; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_update_teachers_active_related_job_id_staff AFTER UPDATE OF job_id ON public.staff FOR EACH ROW EXECUTE FUNCTION public.update_teachers_active_related_job_id_staff();


--
-- TOC entry 4831 (class 2620 OID 114748)
-- Name: login_access update_login_access_timestamp; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_login_access_timestamp BEFORE UPDATE ON public.login_access FOR EACH ROW EXECUTE FUNCTION public.update_timestamp();


--
-- TOC entry 4837 (class 2620 OID 106518)
-- Name: score_grades update_score_grades_timestamp; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_score_grades_timestamp BEFORE UPDATE ON public.score_grades FOR EACH ROW EXECUTE FUNCTION public.update_timestamp();


--
-- TOC entry 4830 (class 2620 OID 49158)
-- Name: staff update_staffs_timestamp; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_staffs_timestamp BEFORE UPDATE ON public.staff FOR EACH ROW EXECUTE FUNCTION public.update_timestamp();


--
-- TOC entry 4835 (class 2620 OID 49162)
-- Name: student_representative update_student_representatives_timestamp; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_student_representatives_timestamp BEFORE UPDATE ON public.student_representative FOR EACH ROW EXECUTE FUNCTION public.update_timestamp();


--
-- TOC entry 4836 (class 2620 OID 49160)
-- Name: students update_students_timestamp; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_students_timestamp BEFORE UPDATE ON public.students FOR EACH ROW EXECUTE FUNCTION public.update_timestamp();


--
-- TOC entry 4810 (class 2606 OID 57353)
-- Name: login_access fk_access_type; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_access
    ADD CONSTRAINT fk_access_type FOREIGN KEY (access_type) REFERENCES public.login_access_type(id_access_type);


--
-- TOC entry 4812 (class 2606 OID 32779)
-- Name: grades grades_education_level_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grades
    ADD CONSTRAINT grades_education_level_id_fkey FOREIGN KEY (education_level_id) REFERENCES public.education_levels(education_level_id);


--
-- TOC entry 4813 (class 2606 OID 65559)
-- Name: teachers guide_grade_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT guide_grade_id FOREIGN KEY (guide_grade_id) REFERENCES public.grades(grade_id);


--
-- TOC entry 4824 (class 2606 OID 73739)
-- Name: impart_time_teacher impart_time_teacher_subject_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.impart_time_teacher
    ADD CONSTRAINT impart_time_teacher_subject_teacher_id_fkey FOREIGN KEY (subject_teacher_id) REFERENCES public.subject_teacher(subject_teacher_id);


--
-- TOC entry 4825 (class 2606 OID 73744)
-- Name: impart_time_teacher impart_time_teacher_teacher_grade_assigned_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.impart_time_teacher
    ADD CONSTRAINT impart_time_teacher_teacher_grade_assigned_id_fkey FOREIGN KEY (teacher_grade_assigned_id) REFERENCES public.teacher_grade_assigned(tga_id);


--
-- TOC entry 4811 (class 2606 OID 24624)
-- Name: login_access login_access_staff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_access
    ADD CONSTRAINT login_access_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.staff(staff_id);


--
-- TOC entry 4818 (class 2606 OID 41026)
-- Name: retired_students retired_students_register_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.retired_students
    ADD CONSTRAINT retired_students_register_id_fkey FOREIGN KEY (register_id) REFERENCES public.students(register_id);


--
-- TOC entry 4819 (class 2606 OID 41031)
-- Name: retired_students retired_students_representative_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.retired_students
    ADD CONSTRAINT retired_students_representative_id_fkey FOREIGN KEY (representative_id) REFERENCES public.student_representative(representative_id);


--
-- TOC entry 4809 (class 2606 OID 24597)
-- Name: staff staff_job_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_job_id_fkey FOREIGN KEY (job_id) REFERENCES public.job_position(job_id);


--
-- TOC entry 4816 (class 2606 OID 40980)
-- Name: students students_grade_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_grade_id_fkey FOREIGN KEY (grade_id) REFERENCES public.grades(grade_id);


--
-- TOC entry 4817 (class 2606 OID 40985)
-- Name: students students_representative_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_representative_id_fkey FOREIGN KEY (representative_id) REFERENCES public.student_representative(representative_id);


--
-- TOC entry 4820 (class 2606 OID 65554)
-- Name: subject_teacher subject_teacher_subject_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_teacher
    ADD CONSTRAINT subject_teacher_subject_id_fkey FOREIGN KEY (subject_id) REFERENCES public.subjects(subject_id);


--
-- TOC entry 4821 (class 2606 OID 65549)
-- Name: subject_teacher subject_teacher_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_teacher
    ADD CONSTRAINT subject_teacher_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES public.teachers(teacher_id);


--
-- TOC entry 4822 (class 2606 OID 65576)
-- Name: teacher_grade_assigned teacher_grade_assigned_grade_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_grade_assigned
    ADD CONSTRAINT teacher_grade_assigned_grade_id_fkey FOREIGN KEY (grade_id) REFERENCES public.grades(grade_id);


--
-- TOC entry 4823 (class 2606 OID 65571)
-- Name: teacher_grade_assigned teacher_grade_assigned_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_grade_assigned
    ADD CONSTRAINT teacher_grade_assigned_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES public.teachers(teacher_id);


--
-- TOC entry 4814 (class 2606 OID 106504)
-- Name: teachers teachers_main_subject_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_main_subject_fkey FOREIGN KEY (main_subject) REFERENCES public.subjects(subject_id);


--
-- TOC entry 4815 (class 2606 OID 32803)
-- Name: teachers teachers_staff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.staff(staff_id);


-- Completed on 2025-03-17 23:50:07

--
-- PostgreSQL database dump complete
--

