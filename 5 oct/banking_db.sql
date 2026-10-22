CREATE DATABASE banking_db;

USE banking_db;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    account_type VARCHAR(30),
    balance DECIMAL(10,2),
    city VARCHAR(50)
);

INSERT INTO accounts VALUES
(101, 'Arun Kumar', 'Savings', 45000, 'Hyderabad'),
(102, 'Meera Shah', 'Current', 85000, 'Mumbai'),
(103, 'Ravi Reddy', 'Savings', 32000, 'Hyderabad'),
(104, 'Priya Nair', 'Savings', 67000, 'Bangalore'),
(105, 'Sameer Khan', 'Current', 120000, 'Pune'),
(106, 'Neha Gupta', 'Savings', 28000, 'Delhi'),
(107, 'Vikram Rao', 'Current', 95000, 'Hyderabad'),
(108, 'Anjali Singh', 'Savings', 54000, 'Mumbai');

-- Check the data
SELECT * FROM accounts;

-- Stored Procedure Exercises
DELIMITER $$

-- 1. Display all account records
CREATE PROCEDURE GetAllAccounts()
BEGIN
    SELECT * FROM accounts;
END $$

-- 2. Display savings accounts
CREATE PROCEDURE GetSavingsAccounts()
BEGIN
    SELECT *
    FROM accounts
    WHERE account_type = 'Savings';
END $$

-- 3. Display accounts by city
CREATE PROCEDURE GetAccountsByCity(IN p_city VARCHAR(50))
BEGIN
    SELECT *
    FROM accounts
    WHERE city = p_city;
END $$

-- 4. Display accounts above a specified balance
CREATE PROCEDURE GetAccountsAboveBalance(IN p_balance DECIMAL(10,2))
BEGIN
    SELECT *
    FROM accounts
    WHERE balance > p_balance;
END $$

-- 5. Update an account balance
CREATE PROCEDURE UpdateAccountBalance(
    IN p_account_id INT,
    IN p_new_balance DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = p_new_balance
    WHERE account_id = p_account_id;
END $$

-- 6. Deposit an amount into an account
CREATE PROCEDURE DepositAmount(
    IN p_account_id INT,
    IN p_deposit_amount DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = balance + p_deposit_amount
    WHERE account_id = p_account_id;
END $$

-- 7. Withdraw an amount from an account
CREATE PROCEDURE WithdrawAmount(
    IN p_account_id INT,
    IN p_withdrawal_amount DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = balance - p_withdrawal_amount
    WHERE account_id = p_account_id;
END $$

-- 8. Delete an account
CREATE PROCEDURE DeleteAccount(IN p_account_id INT)
BEGIN
    DELETE FROM accounts
    WHERE account_id = p_account_id;
END $$

DELIMITER ;


