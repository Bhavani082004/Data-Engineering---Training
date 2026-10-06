CREATE TABLE vehicles (
 vehicle_id INT PRIMARY KEY,
 vehicle_name VARCHAR(100),
 vehicle_type VARCHAR(50),
 daily_rate DECIMAL(10,2),
 available_status VARCHAR(20)
);
INSERT INTO vehicles VALUES
(1, 'Honda City', 'Car', 2500, 'Available'),
(2, 'Toyota Innova', 'Car', 3500, 'Available'),
(3, 'Royal Enfield', 'Bike', 1200, 'Rented'),
(4, 'Activa', 'Scooter', 700, 'Available'),
(5, 'Mahindra Thar', 'SUV', 4500, 'Rented'),
(6, 'Hyundai Creta', 'SUV', 3200, 'Available'),
(7, 'KTM Duke', 'Bike', 1500, 'Available');
DELIMITER //

CREATE PROCEDURE GetAllVehicles()
BEGIN
    SELECT * FROM vehicles;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE GetAvailableVehicles()
BEGIN
    SELECT *
    FROM vehicles
    WHERE available_status = 'Available';
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE GetVehiclesByType(
    IN p_vehicle_type VARCHAR(50)
)
BEGIN
    SELECT *
    FROM vehicles
    WHERE vehicle_type = p_vehicle_type;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE GetVehiclesByMaxRate(
    IN p_max_rate DECIMAL(10,2)
)
BEGIN
    SELECT *
    FROM vehicles
    WHERE daily_rate <= p_max_rate;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE UpdateVehicleRate(
    IN p_vehicle_id INT,
    IN p_new_rate DECIMAL(10,2)
)
BEGIN
    UPDATE vehicles
    SET daily_rate = p_new_rate
    WHERE vehicle_id = p_vehicle_id;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE UpdateVehicleStatus(
    IN p_vehicle_id INT,
    IN p_status VARCHAR(20)
)
BEGIN
    UPDATE vehicles
    SET available_status = p_status
    WHERE vehicle_id = p_vehicle_id;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE IncreaseRateByPercentage(
    IN p_percentage DECIMAL(5,2)
)
BEGIN
    UPDATE vehicles
    SET daily_rate = daily_rate +
                     (daily_rate * p_percentage / 100);
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE DeleteVehicle(
    IN p_vehicle_id INT
)
BEGIN
    DELETE FROM vehicles
    WHERE vehicle_id = p_vehicle_id;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE GetVehiclesBetweenRates(
    IN p_min_rate DECIMAL(10,2),
    IN p_max_rate DECIMAL(10,2)
)
BEGIN
    SELECT *
    FROM vehicles
    WHERE daily_rate BETWEEN p_min_rate AND p_max_rate;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE CountVehiclesByType(
    IN p_vehicle_type VARCHAR(50)
)
BEGIN
    SELECT COUNT(*) AS vehicle_count
    FROM vehicles
    WHERE vehicle_type = p_vehicle_type;
END //

DELIMITER ;







