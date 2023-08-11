-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student
CREATE PROCEDURE AddBonus(
	IN p_user_name VARCHAR(255),
        IN p_project_name VARCHAR(255),
        IN p_score INT
)
BEGIN
        DECLARE user_id INT;
        DECLARE project_id INT;
        
        SELECT id INTO user_id FROM users WHERE name = p_user_name LIMIT 1;
        
        IF user_id IS NULL THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'User not found';
        END IF;
        
        SELECT id INTO project_id FROM projects WHERE name = p_project_name LIMIT 1;
        
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, project_id, p_score);
        
        SELECT CONCAT('Correction added for user ', p_user_name, ' in project ', p_project_name, ' with a score of ', p_score) AS message;
END;
