# Databricks notebook source
import os

base_path = "/Workspace/Users/azuser7400_mml.local@karthikirisoutlook.onmicrosoft.com/Drafts"

print(os.listdir(base_path))

# COMMAND ----------

csv_path = base_path + "/cinema_bookings.csv"
json_path = base_path + "/cinema_master.json"

bookings_df = spark.read.csv(
    csv_path,
    header=True,
    inferSchema=True
)

cinemas_df = spark.read.json(json_path)

display(bookings_df)
display(cinemas_df)

# COMMAND ----------

print("BOOKINGS DATA")
bookings_df.printSchema()
bookings_df.show(10)

print("CINEMA DATA")
cinemas_df.printSchema()
cinemas_df.show(10)

print("Total booking records:", bookings_df.count())
print("Total cinema records:", cinemas_df.count())

# COMMAND ----------

from pyspark.sql import functions as F

confirmed_df = bookings_df.filter(
    F.col("booking_status") == "Confirmed"
)

display(confirmed_df)

# COMMAND ----------

display(
    bookings_df.filter(
        (F.col("tickets") > 3) &
        (F.col("price_per_ticket") > 200)
    )
)

# COMMAND ----------

display(
    bookings_df.filter(
        (F.col("tickets") > 3) &
        (F.col("price_per_ticket") > 200)
    )
)

# COMMAND ----------

bookings_df.select(
    F.count(F.when(F.col("discount_pct").isNull(), 1)).alias("missing_discount"),
    F.count(F.when(F.col("payment_method").isNull(), 1)).alias("missing_payment")
).show()

# COMMAND ----------

cleaned_df = bookings_df.fillna({
    "discount_pct": 0,
    "payment_method": "Unknown"
})

display(cleaned_df)

# COMMAND ----------

gross_df = cleaned_df.withColumn(
    "gross_amount",
    F.col("tickets") * F.col("price_per_ticket")
)

display(gross_df)

# COMMAND ----------

net_df = gross_df.withColumn(
    "net_amount",
    F.col("gross_amount") * (1 - F.col("discount_pct") / 100)
)

display(net_df)

# COMMAND ----------

size_df = net_df.withColumn(
    "booking_size",
    F.when(F.col("tickets") >= 4, "Large")
     .otherwise("Regular")
)

display(size_df)

# COMMAND ----------

display(
    size_df.orderBy(
        F.col("net_amount").desc()
    ).limit(5)
)

# COMMAND ----------

status_count_df = size_df.groupBy(
    "booking_status"
).count()

display(status_count_df)

# COMMAND ----------

movie_revenue_df = size_df.filter(
    F.col("booking_status") == "Confirmed"
).groupBy("movie_title").agg(
    F.sum("tickets").alias("total_tickets"),
    F.sum("net_amount").alias("total_revenue")
)

display(movie_revenue_df)

# COMMAND ----------

cinema_revenue_df = size_df.filter(
    F.col("booking_status") == "Confirmed"
).groupBy("cinema_id").agg(
    F.sum("net_amount").alias("total_revenue")
)

top_cinemas_df = cinema_revenue_df.orderBy(
    F.col("total_revenue").desc()
).limit(3)

display(top_cinemas_df)

# COMMAND ----------

joined_df = size_df.join(
    cinemas_df,
    on="cinema_id",
    how="left"
)

display(joined_df)

# COMMAND ----------

joined_df = size_df.join(
    cinemas_df,
    on="cinema_id",
    how="left"
)

display(joined_df)

# COMMAND ----------

display(
    joined_df.select(
        "cinema_name",
        F.col("location.city").alias("city"),
        "movie_title",
        "booking_status"
    )
)

# COMMAND ----------

city_revenue_df = joined_df.filter(
    F.col("booking_status") == "Confirmed"
).groupBy(
    F.col("location.city").alias("city")
).agg(
    F.sum("net_amount").alias("total_revenue")
)

display(city_revenue_df)

# COMMAND ----------

unmatched_df = joined_df.filter(
    F.col("cinema_name").isNull()
)

display(unmatched_df)

# COMMAND ----------

display(
    cinemas_df.select(
        "cinema_name",
        F.col("location.zone").alias("zone")
    )
)

# COMMAND ----------

facilities_df = cinemas_df.select(
    "cinema_name",
    F.explode("facilities").alias("facility")
)

display(facilities_df)

# COMMAND ----------

dates_df = size_df.withColumn(
    "booking_date",
    F.to_date("booking_date")
).withColumn(
    "show_date",
    F.to_date("show_date")
).withColumn(
    "days_between",
    F.datediff("show_date", "booking_date")
)

display(dates_df)

# COMMAND ----------

duplicate_df = dates_df.groupBy("booking_id").count().filter(
    F.col("count") > 1
)

display(duplicate_df)

# COMMAND ----------

deduplicated_df = dates_df.dropDuplicates(["booking_id"])

print("Original records:", dates_df.count())
print("Records after removing duplicates:", deduplicated_df.count())

display(deduplicated_df)

# COMMAND ----------

from pyspark.sql.window import Window

movie_revenue_df = deduplicated_df.filter(
    F.col("booking_status") == "Confirmed"
).groupBy("movie_title").agg(
    F.sum("net_amount").alias("total_revenue")
)

window_spec = Window.orderBy(
    F.col("total_revenue").desc()
)

ranked_movies_df = movie_revenue_df.withColumn(
    "movie_rank",
    F.rank().over(window_spec)
)

display(ranked_movies_df.orderBy("movie_rank"))

# COMMAND ----------

final_df = deduplicated_df.join(
    cinemas_df,
    on="cinema_id",
    how="left"
)

display(final_df)