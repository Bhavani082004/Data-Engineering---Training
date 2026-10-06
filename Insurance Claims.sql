CREATE TABLE insurance_claims (
 claim_id INT PRIMARY KEY,
 customer_name VARCHAR(100),
 insurance_type VARCHAR(50),
 claim_amount DECIMAL(12,2),
 branch VARCHAR(50)
);
INSERT INTO insurance_claims VALUES
(1, 'Ajay Kumar', 'Health', 75000, 'Hyderabad'),
(2, 'Meena Shah', 'Motor', 45000, 'Mumbai'),
(3, 'Rohit Jain', 'Health', 125000, 'Hyderabad'),
(4, 'Sara Ali', 'Travel', 30000, 'Delhi'),
(5, 'Vikas Rao', 'Motor', 85000, 'Mumbai'),
(6, 'Nisha Singh', 'Health', 60000, 'Delhi'),
(7, 'Imran Khan', 'Travel', 55000, 'Hyderabad'),
(8, 'Pooja Patel', 'Motor', 40000, 'Delhi'),
(9, 'Karan Mehta', 'Health', 150000, 'Mumbai'),
(10, 'Farah Ahmed', 'Travel', 35000, 'Hyderabad');
WITH InsuranceTypeClaims AS
(
    SELECT insurance_type,
           SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY insurance_type
)
SELECT *
FROM InsuranceTypeClaims;
WITH BranchClaims AS
(
    SELECT branch,
           SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY branch
)
SELECT *
FROM BranchClaims;
WITH InsuranceTypeClaims AS
(
    SELECT insurance_type,
           SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY insurance_type
)
SELECT *
FROM InsuranceTypeClaims
WHERE total_claims > 200000;
WITH AvgClaim AS
(
    SELECT AVG(claim_amount) AS avg_claim_amount
    FROM insurance_claims
)
SELECT i.*
FROM insurance_claims i
JOIN AvgClaim a
ON i.claim_amount > a.avg_claim_amount;
WITH InsuranceTypeClaims AS
(
    SELECT insurance_type,
           SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY insurance_type
)
SELECT *,
       RANK() OVER (ORDER BY total_claims DESC) AS claim_rank
FROM InsuranceTypeClaims;
WITH InsuranceTypeClaims AS
(
    SELECT insurance_type,
           SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY insurance_type
),
BranchClaims AS
(
    SELECT branch,
           SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY branch
)

SELECT insurance_type AS category,
       total_claims
FROM InsuranceTypeClaims

UNION ALL

SELECT branch,
       total_claims
FROM BranchClaims;
SELECT branch,
       total_claims,
       DENSE_RANK() OVER (ORDER BY total_claims DESC) AS branch_rank
FROM
(
    SELECT branch,
           SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY branch
) BranchClaims;
SELECT *
FROM insurance_claims ic
WHERE claim_amount >
(
    SELECT AVG(claim_amount)
    FROM insurance_claims
    WHERE insurance_type = ic.insurance_type
);
SELECT *
FROM insurance_claims ic
WHERE claim_amount >
(
    SELECT AVG(claim_amount)
    FROM insurance_claims
    WHERE branch = ic.branch
);
SELECT *
FROM insurance_claims ic
WHERE claim_amount =
(
    SELECT MAX(claim_amount)
    FROM insurance_claims
    WHERE insurance_type = ic.insurance_type
);
SELECT customer_name,
       branch,
       claim_amount
FROM insurance_claims ic
WHERE claim_amount >
(
    SELECT AVG(claim_amount)
    FROM insurance_claims
    WHERE branch = ic.branch
);