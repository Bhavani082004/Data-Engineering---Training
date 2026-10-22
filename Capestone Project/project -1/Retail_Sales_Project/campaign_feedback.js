use retail_sales

db.campaign_feedback.insertMany([
    {
        campaign_id: 101,
        store_region: "Chennai",
        product_name: "Laptop",
        customer_feedback: "Good promotional offer",
        rating: 5
    },
    {
        campaign_id: 102,
        store_region: "Bangalore",
        product_name: "Headphones",
        customer_feedback: "Please offer more discounts",
        rating: 4
    },
    {
        campaign_id: 103,
        store_region: "Hyderabad",
        product_name: "Keyboard",
        customer_feedback: "The offer was useful",
        rating: 5
    }
]);


db.campaign_feedback.find();


db.campaign_feedback.createIndex({ product_name: 1 });
db.campaign_feedback.createIndex({ store_region: 1 });


db.campaign_feedback.getIndexes();