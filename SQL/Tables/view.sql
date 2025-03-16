-- This view was made to a specific function to verify if the teacher is already registered with the same grade,subject,time starts, time ends
-- and verify if the teacher is already registered with the same time starts and end
CREATE OR REPLACE VIEW vw_itt_to_verify_data
AS
SELECT
	itt.itt_id,
	th.teacher_id,
	g.grade,
	sb.subject,
	itt.impart_time_start,
	itt.impart_time_end,
	itt.active
FROM impart_time_teacher itt
INNER JOIN subject_teacher sbt 
	ON itt.subject_teacher_id = sbt.subject_teacher_id
INNER JOIN teacher_grade_assigned tga
	ON tga.tga_id = itt.teacher_grade_assigned_id

INNER JOIN subjects sb
	ON sb.subject_id = sbt.subject_id
INNER JOIN grades g
	ON g.grade_id = tga.grade_id

INNER JOIN teachers th
	ON th.teacher_id = tga.teacher_id
WHERE itt.active = true;


--This View is for load data in the table teacher_assigned_and_not_assigned_impart_time
--This view was made to show the teachers that are already assigned to a grade and subject and the teachers that are not assigned to a grade and subject
CREATE OR REPLACE VIEW teacher_assigned_and_not_assigned_impart_time
AS
SELECT
    th.teacher_id,
    INITCAP(CONCAT_WS(' ', st.first_name, st.middle_name, st.first_surname, st.second_surname)) AS full_name,
    g.grade AS guide_grade,
    sb.subject AS main_subject,
    g2.grade AS teacher_grade_assigned,
    sb2.subject AS subject_teacher_assigned,
    itt.impart_time_start,
    itt.impart_time_end
FROM impart_time_teacher itt
INNER JOIN teacher_grade_assigned tga 
    ON tga.tga_id = itt.teacher_grade_assigned_id
INNER JOIN subject_teacher sbt 
    ON sbt.subject_teacher_id = itt.subject_teacher_id
INNER JOIN teachers th 
    ON th.teacher_id = sbt.teacher_id
LEFT JOIN grades g
    ON g.grade_id = th.guide_grade_id
INNER JOIN grades g2 
    ON g2.grade_id = tga.grade_id
LEFT JOIN subjects sb
    ON sb.subject_id = th.main_subject
INNER JOIN subjects sb2 
    ON sb2.subject_id = sbt.subject_id
INNER JOIN staff st 
    ON st.staff_id = th.staff_id
WHERE itt.active = true

UNION

SELECT
    th.teacher_id,
    INITCAP(CONCAT_WS(' ', st.first_name, st.middle_name, st.first_surname, st.second_surname)) AS full_name,
    g.grade AS guide_grade,
    sb.subject AS main_subject,
    g2.grade AS teacher_grade_assigned,
    sb2.subject AS subject_teacher_assigned,
    itt.impart_time_start,
    itt.impart_time_end
FROM teachers th

LEFT JOIN grades g 
    ON g.grade_id = th.guide_grade_id
    
LEFT JOIN subjects sb 
    ON sb.subject_id = th.main_subject
    
INNER JOIN staff st 
    ON st.staff_id = th.staff_id
    
LEFT JOIN subject_teacher sbt 
    ON sbt.teacher_id = th.teacher_id 
    AND sbt.active = true
    
LEFT JOIN subjects sb2 
    ON sb2.subject_id = sbt.subject_id
    
LEFT JOIN teacher_grade_assigned tga 
    ON tga.teacher_id = th.teacher_id 
    AND tga.active = true
    
LEFT JOIN grades g2 
    ON g2.grade_id = tga.grade_id
    
LEFT JOIN impart_time_teacher itt 
    ON itt.teacher_grade_assigned_id = tga.tga_id 
    AND itt.subject_teacher_id = sbt.subject_teacher_id
    AND itt.active = true

WHERE 
    th.active = true
    AND tga.tga_id IS NOT NULL
    AND sbt.subject_teacher_id IS NOT NULL
    AND (
        itt.impart_time_start IS NULL 
        OR itt.impart_time_end IS NULL
    );