-- Inserts education_levels
INSERT INTO public.education_levels (education_level_id, education_level) VALUES (1, 'Educacion Basica');
INSERT INTO public.education_levels (education_level_id, education_level) VALUES (2, 'Educacion Secundaria');

-- Inserts grades
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (1, 'Primer Grado', 1, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (2, 'Segundo Grado', 1, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (3, 'Tercer Grado', 1, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (4, 'Cuarto Grado', 1, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (5, 'Quinto Grado', 1, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (6, 'Sexto Grado', 1, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (7, 'Septimo Grado', 2, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (8, 'Octavo Grado', 2, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (9, 'Noveno Grado', 2, false);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (10, 'Decimo Grado', 2, true);
INSERT INTO public.grades (grade_id, grade, education_level_id, bachelor) VALUES (11, 'Undecimo Grado', 2, true);

-- Inserts job_position
INSERT INTO public.job_position (job_id, job_position) VALUES (1, 'Administrator');
INSERT INTO public.job_position (job_id, job_position) VALUES (2, 'Teacher');
INSERT INTO public.job_position (job_id, job_position) VALUES (3, 'Technical Maintenance');

-- Inserts staff
INSERT INTO public.staff (staff_id, first_name, middle_name, first_surname, second_surname, document_id, address, job_id, active, phone_number, birthday, registered_at, updated_at) VALUES (0, 'administrator_access', NULL, 'administrator_access', NULL, '000-0000-0000K', 'administrator_access', 1, true, NULL, NULL, '2025-01-31 17:12:58.075764', '2025-03-17 10:21:53.129082');

-- Inserts login_access_type
INSERT INTO public.login_access_type (id_access_type, access_type, active) VALUES (0, 'ALLPERMS', true);
INSERT INTO public.login_access_type (id_access_type, access_type, active) VALUES (1, 'Administrative', true);
INSERT INTO public.login_access_type (id_access_type, access_type, active) VALUES (2, 'Staff', true);

-- Inserts login_access
INSERT INTO public.login_access (access_id, staff_id, log_user, log_password, access_type, active, updated_at) VALUES (0, 0, 'admin_basic_log_in_user', '$2b$12$NC/5Q9tQaZl9gt/fuLUasuNJ6pg.kDKm/8.T0we1Y13fOw6Ap7sye', 0, true, '2025-03-17 23:38:18.539901');