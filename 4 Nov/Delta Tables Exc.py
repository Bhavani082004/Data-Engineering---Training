# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE fitness_memberships_demo (
# MAGIC     member_id INT,
# MAGIC     member_name STRING,
# MAGIC     city STRING,
# MAGIC     membership_plan STRING,
# MAGIC     monthly_fee INT,
# MAGIC     duration_months INT,
# MAGIC     status STRING
# MAGIC )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO fitness_memberships_demo VALUES
# MAGIC (101, 'Arjun', 'Hyderabad', 'Premium', 3000, 12, 'Active'),
# MAGIC (102, 'Sneha', 'Pune', 'Basic', 1000, 3, 'Active'),
# MAGIC (103, 'Kiran', 'Chennai', 'Standard', 2000, 6, 'Expired'),
# MAGIC (104, 'Meera', 'Hyderabad', 'Basic', 1000, 6, 'Active'),
# MAGIC (105, 'Vikram', 'Delhi', 'Premium', 3000, 12, 'Active'),
# MAGIC (106, 'Anjali', 'Pune', 'Standard', 2000, 3, 'Cancelled'),
# MAGIC (107, 'Rohit', 'Mumbai', 'Basic', 1000, 3, 'Active'),
# MAGIC (108, 'Divya', 'Chennai', 'Premium', 3000, 6, 'Expired'),
# MAGIC (109, 'Sanjay', 'Hyderabad', 'Standard', 2000, 12, 'Active'),
# MAGIC (110, 'Pooja', 'Delhi', 'Basic', 1000, 3, 'Cancelled'),
# MAGIC (111, 'Nikhil', 'Mumbai', 'Premium', 3000, 12, 'Active'),
# MAGIC (112, 'Kavya', 'Pune', 'Standard', 2000, 6, 'Active'),
# MAGIC (113, 'Manoj', 'Chennai', 'Basic', 1000, 3, 'Expired'),
# MAGIC (114, 'Riya', 'Hyderabad', 'Premium', 3000, 12, 'Active'),
# MAGIC (115, 'Deepak', 'Delhi', 'Standard', 2000, 6, 'Active'),
# MAGIC (116, 'Neha', 'Mumbai', 'Basic', 1000, 3, 'Cancelled'),
# MAGIC (117, 'Tarun', 'Pune', 'Premium', 3000, 12, 'Active'),
# MAGIC (118, 'Aisha', 'Chennai', 'Standard', 2000, 6, 'Active'),
# MAGIC (119, 'Harish', 'Hyderabad', 'Basic', 1000, 3, 'Expired'),
# MAGIC (120, 'Simran', 'Delhi', 'Premium', 3000, 12, 'Active');

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM fitness_memberships_demo;

# COMMAND ----------

# MAGIC %md
# MAGIC **Part A**

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT member_name, city, membership_plan
# MAGIC FROM fitness_memberships_demo;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC WHERE city = 'Hyderabad';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC WHERE monthly_fee > 2000;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT DISTINCT city
# MAGIC FROM fitness_memberships_demo;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC WHERE membership_plan IN ('Premium', 'Standard');

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC WHERE monthly_fee BETWEEN 1000 AND 2000;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC WHERE member_name LIKE 'S%';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC WHERE city = 'Hyderabad'
# MAGIC AND status = 'Active';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC WHERE city = 'Pune'
# MAGIC OR city = 'Chennai';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     member_name AS Name,
# MAGIC     monthly_fee AS Fee
# MAGIC FROM fitness_memberships_demo;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo AS f
# MAGIC WHERE f.membership_plan = 'Premium';

# COMMAND ----------

# MAGIC %md
# MAGIC **Part B**

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO fitness_memberships_demo
# MAGIC VALUES (121, 'Farhan', 'Jaipur', 'Premium', 3000, 6, 'Active');

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE fitness_memberships_demo
# MAGIC SET monthly_fee = 1500
# MAGIC WHERE member_name = 'Sneha';

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE fitness_memberships_demo
# MAGIC SET monthly_fee = monthly_fee + 500
# MAGIC WHERE membership_plan = 'Premium';

# COMMAND ----------

# MAGIC %sql DELETE FROM fitness_memberships_demo
# MAGIC WHERE status = 'Cancelled';

# COMMAND ----------

# MAGIC %sql DELETE FROM fitness_memberships_demo
# MAGIC WHERE member_id = 113;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo
# MAGIC ORDER BY member_id;

# COMMAND ----------

# MAGIC %md
# MAGIC **Part C**

# COMMAND ----------

# MAGIC %sql DESCRIBE HISTORY fitness_memberships_demo;

# COMMAND ----------

# MAGIC %sql DESCRIBE HISTORY fitness_memberships_demo;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM fitness_memberships_demo VERSION AS OF 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 'Current' AS table_version, COUNT(*) AS total_records
# MAGIC FROM fitness_memberships_demo
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'Previous' AS table_version, COUNT(*) AS total_records
# MAGIC FROM fitness_memberships_demo VERSION AS OF 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_remaining_members
# MAGIC FROM fitness_memberships_demo;