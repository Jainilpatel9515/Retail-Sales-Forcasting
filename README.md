# 📊 Retail Sales Forecasting System

A Streamlit-based web application for analyzing, forecasting, and visualizing retail sales performance. This interactive dashboard enables users to sign up, log in, and access sales insights using dynamic visualizations and data science techniques.

---

## 🔧 Features

- 🔐 **User Authentication** (Sign Up / Sign In system with CSV-based credential storage)
- 📘 **Project Overview Section**
- 📂 **Dataset Explorer** with summary, structure, and statistics
- 📊 **Interactive Dashboard** with multiple tabs and predictive form placeholders
- 📈 **Insights via Plotly Visualizations** for:
  - Yearly, Monthly, Quarterly & Seasonal Sales
  - Profit Analysis
  - Product & Customer Insights
  - Sales Trends and Correlations

---

## 🎯 Project Objectives

- Analyze retail sales data and identify trends over time.
- Forecast future sales using historical patterns and seasonality.
- Visualize key business metrics through interactive dashboards.
- Extract actionable insights for inventory and marketing strategies.

---

## 🧰 Technologies Used

- **Python**, **Pandas**, **Plotly**, **Streamlit**
- **Streamlit Option Menu** for sidebar navigation
- **CSV-based storage** for login credentials and dataset
- **Session State & Query Params** for login persistence
- **Data Wrangling** for cleaned and accurate insights

---

## 🚀 Key Highlights

- **📊 Trend Analysis & Visualization** – Yearly, Monthly, Seasonal, and Quarterly breakdowns
- **💰 Profit Analysis** – Revenue and margin evaluation
- **📦 Product & Category Insights** – Identify top-selling and underperforming segments
- **🙋‍♂️ Customer Analytics** – Discover key customer contributions
- **🔍 Anomaly Detection** – Identify unexpected sales spikes/drops

---

## 📂 Dataset Overview

The dataset is loaded from `cleaned_data.csv` and includes columns such as:

- `Order Date`, `Total`, `Profit Margin`, `Product Category`, `Customer Name`, etc.

You can view:
- 📊 DataFrame preview
- 🔍 Missing values
- 📄 Descriptive statistics

---

## 📊 Dashboard Tabs & Forms

1. **📈 Retail Price Prediction** *(placeholder form)*
2. **💵 Total Cost Prediction** *(placeholder form)*
3. **📉 Profit Margin Prediction** *(placeholder form)*
4. **📊 Insights Tab** *(includes 11 types of charts)*:
   - Yearly Sales
   - Monthly Sales
   - Yearly Profit
   - Monthly Profit
   - Seasonal & Quarterly Sales
   - Top Products
   - Category-wise Sales
   - Top Customers
   - Sales Trend Over Time
   - Profit vs Sales (scatter plot)

