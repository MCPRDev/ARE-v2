--Education levels for the institution--
CREATE TABLE public.education_levels (
    education_level_id integer NOT NULL,
    education_level character varying(45)
);

--School grades--
CREATE TABLE public.grades (
    grade_id integer NOT NULL,
    grade character varying(50),
    education_level_id integer,
    bachelor boolean,
    CONSTRAINT grades_education_level_id_fkey FOREIGN KEY (education_level_id) 
        REFERENCES public.education_levels(education_level_id)
);

--Job position for employes
CREATE TABLE public.job_position (
    job_id integer NOT NULL,
    job_position character varying(60) NOT NULL
);

--What staff has access in the software--
CREATE TABLE public.login_access (
    access_id integer NOT NULL,
    staff_id integer,
    log_user character varying(25) NOT NULL,
    log_password character varying(50) NOT NULL,
    access_type integer,
    CONSTRAINT login_access_staff_id_fkey FOREIGN KEY (staff_id) 
        REFERENCES public.staff(staff_id),
    CONSTRAINT fk_access_type FOREIGN KEY (access_type) 
        REFERENCES public.login_access_type(id_access_type)
);

--What kind of perms has--
CREATE TABLE public.login_access_type (
    id_access_type integer NOT NULL,
    access_type character varying(25),
    activity_status boolean
);

--Table for inactive/retired students--
CREATE TABLE public.retired_students (
    retired_id integer NOT NULL,
    register_id integer,
    representative_id integer,
    retired_date date,
    motive character varying(300),
    CONSTRAINT retired_students_register_id_fkey FOREIGN KEY (register_id) 
        REFERENCES public.students(register_id),
    CONSTRAINT retired_students_representative_id_fkey FOREIGN KEY (representative_id) 
        REFERENCES public.student_representative(representative_id)
);

--Here we register the score of each student--
CREATE TABLE public.score_grades (
    score_grade_id integer NOT NULL,
    teacher_id integer,
    register_id integer,
    grade_id integer,
    subject_id integer,
    score_grade numeric NOT NULL,
    entry_date date NOT NULL,
    modified_date date,
    CONSTRAINT score_grades_grade_id_fkey FOREIGN KEY (grade_id) 
        REFERENCES public.grades(grade_id),
    CONSTRAINT score_grades_register_id_fkey FOREIGN KEY (register_id) 
        REFERENCES public.students(register_id),
    CONSTRAINT score_grades_subject_id_fkey FOREIGN KEY (subject_id) 
        REFERENCES public.subjects(subject_id),
    CONSTRAINT score_grades_teacher_id_fkey FOREIGN KEY (teacher_id) 
        REFERENCES public.teachers(teacher_id)
);

--Register all employes in the institution--
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
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT staff_job_id_fkey FOREIGN KEY (job_id) 
        REFERENCES public.job_position(job_id)
);

--Students' tutor register--
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

--Student register--
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
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT students_grade_id_fkey FOREIGN KEY (grade_id) 
        REFERENCES public.grades(grade_id),
    CONSTRAINT students_representative_id_fkey FOREIGN KEY (representative_id) 
        REFERENCES public.student_representative(representative_id)
);

--Subject that impart each teacher--
CREATE TABLE public.subject_teacher (
    subject_teacher_id integer NOT NULL,
    teacher_id integer,
    subject_id integer,
    CONSTRAINT subject_teacher_subject_id_fkey FOREIGN KEY (subject_id) 
        REFERENCES public.subjects(subject_id),
    CONSTRAINT subject_teacher_teacher_id_fkey FOREIGN KEY (teacher_id) 
        REFERENCES public.teachers(teacher_id)
);

--School's subjects--
CREATE TABLE public.subjects (
    subject_id integer NOT NULL,
    subject character varying(50)
);

--What teachers are assined in each grade--
CREATE TABLE public.teacher_grade_assigned (
    tga_id integer NOT NULL,
    teacher_id integer,
    grade_id integer,
    CONSTRAINT teacher_grade_assigned_grade_id_fkey FOREIGN KEY (grade_id) 
        REFERENCES public.grades(grade_id),
    CONSTRAINT teacher_grade_assigned_teacher_id_fkey FOREIGN KEY (teacher_id) 
        REFERENCES public.teachers(teacher_id)
);

--Teacher register--
CREATE TABLE public.teachers (
    teacher_id integer NOT NULL,
    staff_id integer,
    primary_teacher boolean,
    guide_grade_id integer,
    CONSTRAINT teachers_staff_id_fkey FOREIGN KEY (staff_id) 
        REFERENCES public.staff(staff_id),
    CONSTRAINT guide_grade_id FOREIGN KEY (guide_grade_id) 
        REFERENCES public.grades(grade_id)
);

--Teacher time that impart his class--
CREATE TABLE public.impart_time_teacher(
itt_id SERIAL PRIMARY KEY,
subject_teacher_id integer,
teacher_grade_assigned_id integer,
impart_time_start TIME,
impart_time_end TIME,
FOREIGN KEY (subject_teacher_id) REFERENCES subject_teacher(subject_teacher_id),
FOREIGN KEY (teacher_grade_assigned_id) REFERENCES teacher_grade_assigned(tga_id)
);