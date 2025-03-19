-- Tabla: education_levels
-- Descripción: Almacena los niveles educativos.
CREATE TABLE public.education_levels (
    education_level_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    education_level character varying(45)
);

-- Tabla: grades
-- Descripción: Almacena los grados educativos.
CREATE TABLE public.grades (
    grade_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    grade character varying(50),
    education_level_id integer,
    bachelor boolean,
    FOREIGN KEY (education_level_id) REFERENCES public.education_levels(education_level_id)  -- Foreign Key
);

-- Tabla: job_position
-- Descripción: Almacena los puestos de trabajo.
CREATE TABLE public.job_position (
    job_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    job_position character varying(60) NOT NULL
);

-- Tabla: staff
-- Descripción: Almacena la información del personal.
CREATE TABLE public.staff (
    staff_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    first_name character varying(50) NOT NULL,
    middle_name character varying(50),
    first_surname character varying(50) NOT NULL,
    second_surname character varying(50),
    document_id character varying(20) NOT NULL UNIQUE,
    address character varying(250) NOT NULL,
    job_id integer,
    active boolean DEFAULT true,
    phone_number character varying(15),
    birthday date,
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES public.job_position(job_id)  -- Foreign Key
);

-- Tabla: login_access
-- Descripción: Almacena la información de acceso de los usuarios.
CREATE TABLE public.login_access (
    access_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    staff_id integer,
    log_user character varying(25) NOT NULL UNIQUE,
    log_password character varying(255) NOT NULL UNIQUE,
    access_type integer,
    active boolean DEFAULT true,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES public.staff(staff_id),  -- Foreign Key
    FOREIGN KEY (access_type) REFERENCES public.login_access_type(id_access_type)  -- Foreign Key
);

-- Tabla: login_access_type
-- Descripción: Almacena los tipos de acceso.
CREATE TABLE public.login_access_type (
    id_access_type SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    access_type character varying(25),
    active boolean
);

-- Tabla: student_representative
-- Descripción: Almacena la información de los representantes de los estudiantes.
CREATE TABLE public.student_representative (
    representative_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    first_name character varying(50) NOT NULL,
    middle_name character varying(50),
    first_surname character varying(50) NOT NULL,
    second_surname character varying(50),
    representative_document_id character varying(25) UNIQUE,
    residential_address character varying(250),
    phone_number character varying(15),
    active boolean DEFAULT true,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: students
-- Descripción: Almacena la información de los estudiantes.
CREATE TABLE public.students (
    register_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
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
    FOREIGN KEY (grade_id) REFERENCES public.grades(grade_id),  -- Foreign Key
    FOREIGN KEY (representative_id) REFERENCES public.student_representative(representative_id)  -- Foreign Key
);

-- Tabla: retired_students
-- Descripción: Almacena la información de los estudiantes retirados.
CREATE TABLE public.retired_students (
    retired_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    register_id integer,
    representative_id integer,
    retired_date date,
    motive character varying(300),
    FOREIGN KEY (register_id) REFERENCES public.students(register_id),  -- Foreign Key
    FOREIGN KEY (representative_id) REFERENCES public.student_representative(representative_id)  -- Foreign Key
);

-- Tabla: subjects
-- Descripción: Almacena las materias o asignaturas.
CREATE TABLE public.subjects (
    subject_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    subject character varying(50),
    active boolean DEFAULT true
);

-- Tabla: teachers
-- Descripción: Almacena la información de los profesores.
CREATE TABLE public.teachers (
    teacher_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    staff_id integer,
    primary_teacher boolean DEFAULT false,
    guide_grade_id integer,
    active boolean DEFAULT true,
    main_subject integer,
    FOREIGN KEY (staff_id) REFERENCES public.staff(staff_id),  -- Foreign Key
    FOREIGN KEY (guide_grade_id) REFERENCES public.grades(grade_id),  -- Foreign Key
    FOREIGN KEY (main_subject) REFERENCES public.subjects(subject_id)  -- Foreign Key
);

-- Tabla: subject_teacher
-- Descripción: Relaciona profesores con materias.
CREATE TABLE public.subject_teacher (
    subject_teacher_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    teacher_id integer,
    subject_id integer,
    active boolean DEFAULT true,
    FOREIGN KEY (teacher_id) REFERENCES public.teachers(teacher_id),  -- Foreign Key
    FOREIGN KEY (subject_id) REFERENCES public.subjects(subject_id),  -- Foreign Key
    UNIQUE (teacher_id, subject_id)  -- Unique constraint
);

-- Tabla: teacher_grade_assigned
-- Descripción: Relaciona profesores con grados.
CREATE TABLE public.teacher_grade_assigned (
    tga_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    teacher_id integer,
    grade_id integer,
    active boolean DEFAULT true,
    FOREIGN KEY (teacher_id) REFERENCES public.teachers(teacher_id),  -- Foreign Key
    FOREIGN KEY (grade_id) REFERENCES public.grades(grade_id),  -- Foreign Key
    UNIQUE (teacher_id, grade_id)  -- Unique constraint
);

-- Tabla: impart_time_teacher
-- Descripción: Almacena los horarios de los profesores.
CREATE TABLE public.impart_time_teacher (
    itt_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    subject_teacher_id integer,
    teacher_grade_assigned_id integer,
    impart_time_start time without time zone,
    impart_time_end time without time zone,
    active boolean DEFAULT true,
    FOREIGN KEY (subject_teacher_id) REFERENCES public.subject_teacher(subject_teacher_id),  -- Foreign Key
    FOREIGN KEY (teacher_grade_assigned_id) REFERENCES public.teacher_grade_assigned(tga_id)  -- Foreign Key
);

-- Tabla: score_grades
-- Descripción: Almacena las calificaciones de los estudiantes.
CREATE TABLE public.score_grades (
    score_grade_id SERIAL PRIMARY KEY,  -- Primary Key (SERIAL)
    tga_id integer,
    register_student_id integer,
    subject_teacher_id integer,
    score_grade numeric(3,2),
    registered_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);