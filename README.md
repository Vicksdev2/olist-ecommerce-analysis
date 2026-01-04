<h1 align="center">📊  Olist E-Commerce Analysis </h1>

<br>

  I am sharing my Exploratory Data Analysis (EDA) and data visualization using Python. The goal is to audit
business performance by quantifying patterns in sales seasonality, logistics efficiency, and customer behavior.

<br>
<p align="center">
  <img width="1400" height="294" alt="1_1k72mg1_CZvLptX77zzKTg" src="https://github.com/user-attachments/assets/72f40c72-cd16-4a3c-93b9-2cb16267099d" />
</p>

<br>
<h2>🪪 About the Project </h2>

  Olist is a leading Brazilian e-commerce platform that connects small businesses with the country's main marketplaces. Operating as a
  SaaS technology company, it facilitates the sale of products from thousands of sellers to millions of customers.
This project consisted of an Olist performance audit (2016-2018) using real public data. Although the company shows a **strong positive trend in sales**, it
faces a critical **retention** challenge, the percentage of one-time purchases is 96.99% of customers who only buy once.

<br>
<h2>🛠️ Technical Stack and Methodology</h2>

- **Data cleaning:**  Management of null values, conversion of data types (timestamps), and merging of eight relational data sets.
- **Geospatial analysis:**  Mapping of customer distribution and calculation of delay rates by state (comparison between SLA and actual delivery).
- **Customer segmentation:** Identification of repeat users and purchasing patterns using advanced aggregation operations (`groupby`, `nunique`).
- **Logistics optimization:** Detection of critical states (AL, MA, SE) with delay rates above 15%, suggesting the need for regional distribution centers.

<br>
<h2>⛓️‍💥 Main question:</h2>
How can we optimize the customer experience to maximize retention and lifetime value?

<br>
<br>
<h2>🔍 Key Findings </h2>
 Types of customers and their rankings.

- **What do they buy?** Their main categories are **Furniture and Decor** and **Bed, Bath, and Tableware**.
- **Reviews:** In negative reviews (1-2 stars), we found that complaints about the product (quality, defects, differences from the description) are twice as frequent as complaints about Logistics.
  - **Product Complaints:** ~8,800 mentions.
  - **Logistics complaints:** ~4,300 mentions.

The problem is not loyal customers, it is that the furniture products have quality/shipping issues.

<br>
<h2> Locations </h2>

***Who are our best customers and where are they located?***

- Customers usually only buy once, representing 89.5% of sales. Most customers are in Sao Paulo and Rio de Janeiro.
- Spending per customer: approximately $20 to $60.



<p align="center">
  <img src="public/states_customers.png" alt="Análisis de clientes por estado" width="800">
</p>