<h1 align="center">📊  Olist E-Commerce Analysis </h1>

<br>
# Olist Ecommerce Analysis

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vicksdev2/olist-ecommerce-analysis/blob/main/proyect_olist.ipynb)

<br>
<p align="center">
  <img width="1400" height="294" alt="1_1k72mg1_CZvLptX77zzKTg" src="https://github.com/user-attachments/assets/72f40c72-cd16-4a3c-93b9-2cb16267099d" />
</p>

<br>
<p align="center">
  <img width="800" height="400" alt="{240A4128-74E6-4D66-87D1-356E7D442CA1}" src="https://github.com/user-attachments/assets/7ad459dc-ff0e-4505-ab9d-6526030f4bde" />
</p>



<br>
<p align="center">
  <img width="800" height="400" alt="{7B22EA2A-2ABE-4B69-966E-92E9ED6EF766}" src="https://github.com/user-attachments/assets/d72991eb-aa9e-4a66-b879-1323abc8524d" />

</p>








<h2>📑 Index </h2>

1. [🪪 About the Project](#about)
2. [🛠️ Technical Stack and Methodology](#tech)
3. [⛓️‍💥 Main question](#question)
4. [🔍 Key Findings](#findings)
5. [🚩 Locations](#locations)
6. [🚐 Deliveries](#deliveries)
7. [🪠🧻🫧 Most recurring products](#products)
8. [📈 Sales Forecast](#forecast)
9. [📈 Life Cycle and Sales](#lifecycle)
10. [⚙️ Technologies used](#technologies)
11. [⌨️ Data](#data)

<h1 align="center">📊 Olist E-Commerce Analysis</h1>

<p align="center">
  Exploratory Data Analysis of the Olist e-commerce dataset using Python, with a focus on sales performance, logistics, customer behavior, retention, and review patterns.
</p>

<p align="center">
  <img src="public/cover.png" width="1400" alt="Olist E-Commerce Analysis Banner" />
</p>

## Table of Contents

1. [About the Project](#about-the-project)
2. [Business Objective](#business-objective)
3. [Tools and Methodology](#tools-and-methodology)
4. [Main Findings](#main-findings)
5. [Sales Analysis](#sales-analysis)
6. [Customer Spending and Value](#customer-spending-and-value)
7. [Delivery Performance](#delivery-performance)
8. [Reviews and Sentiment](#reviews-and-sentiment)
9. [Payment Methods](#payment-methods)
10. [Customer Retention](#customer-retention)
11. [Key Takeaways](#key-takeaways)
12. [Technologies Used](#technologies-used)

---

## About the Project

This project explores the public Olist e-commerce dataset to understand how the business performs across sales, logistics, customer behavior, and review quality.

The analysis focuses on identifying patterns that help answer questions such as:
- Which states generate the most sales and customers?
- What is the average spending per customer?
- How often do customers return to purchase again?
- Which payment methods are most commonly used?
- Are negative reviews more related to products or logistics?

---

## Business Objective

The goal of this analysis is to transform raw transactional data into actionable business insights.

Rather than building a predictive model, this project focuses on exploratory analysis to uncover:
- sales trends,
- customer value,
- retention behavior,
- late delivery patterns,
- and review drivers.

---

## Tools and Methodology

The analysis was developed using:
- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**

Methodology included:
- data cleaning and preparation,
- merging multiple datasets,
- calculating customer-level metrics,
- analyzing delivery delays,
- classifying review complaints by keyword,
- and visualizing trends across time, geography, and behavior.

---

## Main Findings

### Sales are concentrated in a few states
Most revenue and order volume come from a small number of states, especially **São Paulo** and **Rio de Janeiro**. This suggests that Olist’s strongest commercial activity is concentrated in Brazil’s largest economic centers.

### Customer spending is highly skewed
Most customers spend relatively little, while a smaller segment drives much higher total spending. The customer spending distribution is right-skewed, with a long tail of high-value buyers.

### Credit cards dominate payment behavior
**Credit card** is by far the most used payment method, followed by **boleto**. Other methods such as voucher and debit card represent a much smaller share of transactions.

### Product complaints are more common than logistics complaints
Negative review analysis shows that complaints related to **products** are more frequent than those related to **delivery or logistics**.

- Logistics-related mentions: **4,306**
- Product-related mentions: **8,804**

This indicates that, overall, product experience appears to be a bigger source of dissatisfaction than shipping performance.

### Retention is a major challenge
A very large share of customers purchase only once. Repeat buyers exist, but they represent a much smaller group compared to one-time customers. This makes retention and reactivation a critical opportunity.

---

## Sales Analysis

The business shows a strong upward sales trend over time, with visible seasonality across the months.

<p align="center">
  <img src="public/monthly_sales.png" width="1000" alt="Monthly Sales Evolution" />
</p>

Revenue grows steadily across the observed period, with some clear seasonal peaks. This suggests that the business is scaling, but also that performance is influenced by calendar effects and shopping cycles.

---

## Customer Spending and Value

The total spending per customer shows that most buyers are concentrated in the lower spending ranges, while a smaller group of customers generates higher lifetime value.

<p align="center">
  <img src="public/total_spending_per_customer.png" width="1000" alt="Total Spending per Customer" />
</p>

This distribution is important because it shows that customer value is not uniform. A relatively small number of customers contribute disproportionately to revenue, which makes value-based segmentation useful for future retention actions.

---

## Delivery Performance

Delivery delays are not uniform across Brazil. Some states show significantly higher late-order rates than others.

<p align="center">
  <img src="public/delivery_delays_by_state.png" width="1000" alt="Late Deliveries by State" />
</p>

States in the Northeast tend to show higher delay rates, which suggests regional logistics constraints. On average, this kind of pattern points to fulfillment and distribution challenges rather than a single nationwide issue.

---

## Reviews and Sentiment

The review analysis shows a clear difference between positive and negative experiences. While many customers leave favorable reviews, the negative feedback is dominated by product-related issues rather than logistics-related issues.

### Complaint focus in negative reviews
- Product-related mentions: **8,804**
- Logistics-related mentions: **4,306**

This means that when customers are unhappy, the issue is more often tied to product quality, description mismatch, defects, or expectations than to delivery alone.

### Categories with weaker reviews
Some product categories appear more frequently in lower-rated feedback, which can help identify where quality control, supplier reliability, or product presentation may need attention.

---

## Payment Methods

The most used payment method is credit card, followed by boleto.

<p align="center">
  <img src="public/payment_methods.png" width="1000" alt="Payment Methods Distribution" />
</p>

This suggests that Olist’s customer base is strongly oriented toward card-based checkout, while boleto still plays an important role in the Brazilian market.

---

## Customer Retention

Customer repurchase behavior shows a very important pattern: many repeat customers return quickly, but most customers still do not come back.

### Repurchase cycle statistics
- Mean: **78.78 days**
- Median: **29 days**
- Minimum: **0 days**
- Maximum: **608 days**

Half of repeat customers make another purchase within about one month. However, the average is much higher than the median because a smaller number of customers return after very long gaps.

<p align="center">
  <img src="public/repurchase_cycle.png" width="1000" alt="Repurchase Cycle" />
</p>

This indicates that retention is highly uneven. Some customers buy repeatedly in short cycles, while many others make only one purchase and never return.

---

## Key Takeaways

- Sales are concentrated in a few high-performing states.
- Credit card is the dominant payment method.
- Customer spending is heavily skewed toward a smaller high-value segment.
- Product-related complaints are more common than logistics complaints.
- Late deliveries are more concentrated in specific states.
- Retention is the biggest business opportunity in this analysis.

### Data-driven implications
If this were to inform business priorities, the analysis suggests focusing on:
- improving product quality and catalog accuracy,
- strengthening retention campaigns for one-time buyers,
- studying high-value customers to replicate repeat-purchase behavior,
- and reducing regional delivery delays.

These are not direct recommendations from a consultant perspective, but rather logical implications derived from the data.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## Project Artifacts

Charts used in this README:
- `public/total_spending_per_customer.png`
- `public/payment_methods.png`
- `public/delivery_delays_by_state.png`
- `public/monthly_sales.png`
- `public/repurchase_cycle.png`

---

## Author

Created as part of an exploratory data analysis project on the Olist e-commerce dataset.

**Developed by:** Barbara V. Cedeño A.
