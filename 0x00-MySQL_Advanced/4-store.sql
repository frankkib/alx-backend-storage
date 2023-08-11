-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
DELIMITER //
CREATE TRIGGER update_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_quantity INT;
    SELECT quantity INTO item_quantity FROM items WHERE name = NEW.item_name;
    IF item_quantity >= NEW.number THEN
        UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
    END IF;
END;
//
DELIMITER ;

