# Databricks notebook source
base_path = "/Volumes/workspace/retail_capstone/retail_sales_volume/"

display(dbutils.fs.ls(base_path))

# COMMAND ----------

sales_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(base_path + "cleaned_sales.csv")
)

display(sales_df)

# COMMAND ----------

products_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(base_path + "products.csv")
)

display(products_df)

# COMMAND ----------

print("SALES DATA")
sales_df.printSchema()

print("PRODUCT DATA")
products_df.printSchema()

# COMMAND ----------

print("Sales records:", sales_df.count())
print("Product records:", products_df.count())

print("Sales columns:", sales_df.columns)
print("Product columns:", products_df.columns)

# COMMAND ----------

sales_df = sales_df.withColumn(
    "product_id",
    sales_df["product_id"].cast("string")
)

products_df = products_df.withColumn(
    "product_id",
    products_df["product_id"].cast("string")
)

joined_df = sales_df.join(
    products_df,
    on="product_id",
    how="inner"
)

display(joined_df)

# COMMAND ----------

from pyspark.sql.functions import (
    col,
    sum as spark_sum,
    round as spark_round,
    when
)

sales_metrics = joined_df.withColumn(
    "total_revenue",
    col("quantity") * col("price")
).withColumn(
    "total_cost",
    col("quantity") * col("cost")
).withColumn(
    "profit",
    col("total_revenue") - col("total_cost")
)

display(sales_metrics)

# COMMAND ----------

from pyspark.sql.functions import col, sum as spark_sum, round as spark_round, when

sales_metrics = joined_df.drop(products_df["category"])

sales_metrics = sales_metrics.withColumn(
    "total_revenue",
    col("quantity") * col("price")
).withColumn(
    "total_cost",
    col("quantity") * col("cost")
).withColumn(
    "profit",
    col("total_revenue") - col("total_cost")
)

category_metrics = (
    sales_metrics
    .groupBy("category")
    .agg(
        spark_sum("quantity").alias("total_quantity_sold"),
        spark_round(spark_sum("total_revenue"), 2).alias("total_revenue"),
        spark_round(spark_sum("total_cost"), 2).alias("total_cost"),
        spark_round(spark_sum("profit"), 2).alias("total_profit")
    )
    .withColumn(
        "profit_margin",
        when(
            col("total_revenue") != 0,
            spark_round(
                col("total_profit") / col("total_revenue") * 100, 2
            )
        ).otherwise(0)
    )
    .orderBy(col("total_profit").desc())
)

display(category_metrics)
   

# COMMAND ----------

category_metrics.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.retail_capstone.retail_category_metrics")

# COMMAND ----------

saved_metrics = spark.table(
    "workspace.retail_capstone.retail_category_metrics"
)

display(saved_metrics)

# COMMAND ----------

sales_metrics = joined_df.drop(
    products_df["category"]
).drop(
    products_df["product_name"]
)

sales_metrics = sales_metrics.withColumn(
    "total_revenue",
    col("quantity") * col("price")
).withColumn(
    "total_cost",
    col("quantity") * col("cost")
).withColumn(
    "profit",
    col("total_revenue") - col("total_cost")
)

product_metrics = (
    sales_metrics
    .groupBy("product_id", "product_name")
    .agg(
        spark_sum("quantity").alias("total_quantity_sold"),
        spark_round(spark_sum("total_revenue"), 2).alias("total_revenue"),
        spark_round(spark_sum("profit"), 2).alias("total_profit")
    )
)

display(product_metrics)

# COMMAND ----------

product_metrics.createOrReplaceTempView("product_metrics")

print("Product metrics view created successfully!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     product_id,
# MAGIC     product_name,
# MAGIC     total_quantity_sold,
# MAGIC     total_revenue
# MAGIC FROM product_metrics
# MAGIC ORDER BY total_quantity_sold DESC
# MAGIC LIMIT 3;

# COMMAND ----------

product_metrics.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.retail_capstone.retail_product_metrics")

print("Product metrics saved successfully!")