import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
import plotly.express as px

st.set_page_config(page_title="Retail Sales App", layout="wide")

USER_FILE = "users.csv"

if not os.path.exists(USER_FILE):
    df = pd.DataFrame(columns=["email", "password"])
    df.to_csv(USER_FILE, index=False)

users = pd.read_csv(USER_FILE, usecols=["email", "password"], dtype=str)
users = users.applymap(lambda x: x.strip())

if "email" in st.query_params:
    st.session_state["logged_in"] = True
    st.session_state["email"] = st.query_params["email"]
    st.session_state["authenticated"] = True
    st.session_state["user_email"] = st.query_params["email"]

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["authenticated"] = False
    st.session_state["email"] = ""
    st.session_state["user_email"] = ""

with st.sidebar:
    st.title("🔐 Login / Sign Up")

    if not st.session_state["logged_in"]:
        choice = st.radio("Choose an option:", ["Sign In", "Sign Up"])
        email = st.text_input("Email").strip()
        password = st.text_input("Password", type="password").strip()

        if choice == "Sign In":
            if st.button("Sign In"):
                if email in users["email"].values:
                    row = users[users["email"] == email]
                    if row.iloc[0]["password"].strip() == password:
                        st.session_state["logged_in"] = True
                        st.session_state["authenticated"] = True
                        st.session_state["email"] = email
                        st.session_state["user_email"] = email
                        st.query_params["email"] = email
                        st.rerun()
                    else:
                        st.error("Wrong password.")
                else:
                    st.error("Email not found.")

        elif choice == "Sign Up":
            if st.button("Sign Up"):
                if email in users["email"].values:
                    st.warning("Email already registered.")
                else:
                    new_user = pd.DataFrame([{"email": email, "password": password}])
                    users = pd.concat([users, new_user], ignore_index=True)
                    users.to_csv(USER_FILE, index=False)
                    st.success("Account created! You can now sign in.")

    elif st.session_state["logged_in"]:
        st.success(f"Logged in as {st.session_state['email']}")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["authenticated"] = False
            st.session_state["email"] = ""
            st.session_state["user_email"] = ""
            st.query_params.clear()
            st.rerun()

# ========================================
# 🔗 Integrating Your Provided Dashboard Code Below
# ========================================

if st.session_state.authenticated:
    with st.sidebar:

        st.markdown("### 💬 Main Menu")
        selected = option_menu(
            menu_title=None,
            options=["Project Overview", "Dataset", "Dashboard"],
            icons=["book", "folder", "bar-chart-line"],
            menu_icon=None,
            default_index=0,
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#DDEEFF",  # secondaryBackgroundColor
                    "border-radius": "8px"
                },
                "icon": {"color": "#2C3E50", "font-size": "18px"},  # textColor
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#F4F7FE",  # backgroundColor
                },
                "nav-link-selected": {
                    "background-color": "#1E88E5",  # primaryColor
                    "color": "white",
                    "font-weight": "bold",
                },
            }
        )
    try:
        data = pd.read_csv("cleaned_data.csv")
        data["Order Date"] = pd.to_datetime(data["Order Date"], errors='coerce')
        data["Profit Margin"] = data["Profit Margin"].replace('[\\$,]', '', regex=True).astype(float)
        data["Total"] = data["Total"].replace('[\\$,]', '', regex=True).astype(float)
    except FileNotFoundError:
        st.error("Dataset not found.")
        data = None

    if selected == "Project Overview":
        st.subheader("📘 Project Overview")

        st.write(
            "### 🧠 Retail Sales Forecasting System – Final Year Project"
        )

        st.write(
            "The primary objective is to empower businesses with the ability to analyze historical sales data and forecast future trends. "
            "By leveraging data science techniques and interactive visualizations, this system supports strategic decision-making and operational efficiency."
        )

        st.subheader("🎯 Project Objectives")
        st.markdown("- To analyze retail sales data and identify trends over time.")
        st.markdown("- To forecast future sales using historical patterns and seasonality.")
        st.markdown("- To visualize key business metrics through dynamic and interactive dashboards.")
        st.markdown("- To extract actionable insights that can assist in inventory planning and marketing strategies.")

        st.subheader("🧰 Technologies Used")
        st.markdown(
            "- **Python**, **Pandas**, **Plotly**, **Streamlit** for development and visualization.\n"
            "- **Machine Learning Models** for forecasting (e.g., ARIMA, Prophet, or LSTM).\n"
            "- **Streamlit Session State** for user login and interface interactivity.\n"
            "- **Data Wrangling & Preprocessing** to ensure accurate predictions and insights."
        )

        st.subheader("🚀 Key Features")
        st.markdown(
            "- **📊 Trend Analysis & Visualization** – Yearly, Monthly, Seasonal, and Quarterly sales breakdowns.")
        st.markdown("- **💰 Profit Analysis** – Track revenue vs profit margins.")
        st.markdown("- **📦 Product & Category Insights** – Identify top-selling products and customer behavior.")
        st.markdown("- **🔍 Anomaly Detection** – Spot unexpected sales drops or spikes.")
        st.markdown("- **👤 Customer Analytics** – Understand key customer segments and revenue contributions.")

        st.info(
            "🔎 *This project reflects core concepts from Data Science, Machine Learning, and Software Development, showcasing my ability to apply technical skills to real-world business problems.*")

    if selected == "Dataset":
        st.subheader("📂 Dataset Overview")
        if data is not None:
            st.dataframe(data, use_container_width=True)
            st.success("✅ Dataset Loaded Successfully!")
            st.markdown(f"Total Columns : {data.shape[1]}")
            st.markdown(f"Total Rows : {data.shape[0]}")
            st.markdown("🔍 **Missing Values :**")
            st.write(data.isnull().sum())
            st.markdown("**🧾 Column Names :**")
            st.write(data.columns.tolist())
            st.markdown(" Data Summary :")
            st.write(data.describe())
            st.markdown(" First 5 Rows :")
            st.dataframe(data.head())

    if selected == "Dashboard" and data is not None:
        st.subheader("📊 Retail Sales Dashboard")

        data["Year"] = data["Order Date"].dt.year
        data["Month"] = data["Order Date"].dt.month
        data["Quarter"] = data["Order Date"].dt.quarter
        season_map = {12: "Winter", 1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring",
                      6: "Summer", 7: "Summer", 8: "Summer", 9: "Fall", 10: "Fall", 11: "Fall"}
        data["Season"] = data["Month"].map(season_map)

        tab1, tab2, tab3, tab4 = st.tabs(["📈 Retail Price", "💵 Total Cost", "📉 Profit Margin", "📊 Insights"])

        with tab1:
            with st.form("form1"):
                st.number_input("Cost Price")
                st.text_input("City")
                st.text_input("Order Priority")
                st.number_input("Shipping Cost")
                st.number_input("Profit Margin")
                st.number_input("Order Quantity")
                st.number_input("Discount%")
                st.number_input("Subtotal")
                st.number_input("Order Total")
                if st.form_submit_button("Retail Price Prediction"):
                    st.success("Prediction feature not implemented yet.")

        with tab2:
            with st.form("form2"):
                st.number_input("Cost Price")
                st.number_input("Retail Price")
                st.number_input("Profit")
                st.number_input("Order Quantity")
                st.number_input("Subtotal")
                st.number_input("Discount%")
                st.number_input("Order Total")
                st.number_input("Shipping Cost")
                if st.form_submit_button("Total Cost Prediction"):
                    st.success("Prediction feature not implemented yet.")

        with tab3:
            with st.form("form3"):
                st.number_input("Cost Price")
                st.number_input("Retail Price")
                st.number_input("Profit")
                st.number_input("Order Quantity")
                st.number_input("Subtotal")
                st.number_input("Discount%")
                st.number_input("Order Total")
                st.number_input("Shipping Cost")
                if st.form_submit_button("Profit Margin Prediction"):
                    st.success("Prediction feature not implemented yet.")

        with tab4:
            st.subheader("📊 Interactive Insights")

            chart_option = st.selectbox(
                "Select a chart to display:",
                [
                    "📅 Yearly Sales",
                    "📆 Monthly Sales",
                    "💹 Yearly Profit",
                    "📈 Monthly Profit",
                    "🌦️ Seasonal Sales",
                    "📊 Quarterly Sales",
                    "🏆 Top Products",
                    "🛒 Category-wise Sales",
                    "🙋‍♂️ Top Customers",
                    "📈 Sales Trend Over Time",
                    "💰 Profit vs Sales"
                ]
            )

            if chart_option == "📅 Yearly Sales":
                fig = px.bar(data.groupby("Year")["Total"].sum().reset_index(), x="Year", y="Total", color="Total",
                             title="Yearly Sales", color_continuous_scale="Viridis")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "📆 Monthly Sales":
                fig = px.line(data.groupby("Month")["Total"].sum().reset_index(), x="Month", y="Total",
                              title="Monthly Sales", markers=True)
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "💹 Yearly Profit":
                fig = px.bar(data.groupby("Year")["Profit Margin"].sum().reset_index(), x="Year", y="Profit Margin",
                             color="Profit Margin", title="Yearly Profit", color_continuous_scale="Plasma")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "📈 Monthly Profit":
                fig = px.line(data.groupby("Month")["Profit Margin"].sum().reset_index(), x="Month", y="Profit Margin",
                              title="Monthly Profit", markers=True)
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "🌦️ Seasonal Sales":
                seasonal_sales = data.groupby("Season")["Total"].sum().reset_index()
                fig = px.bar(seasonal_sales, x="Season", y="Total", color="Total", title="Seasonal Sales",
                             color_continuous_scale="Cividis")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "📊 Quarterly Sales":
                quarterly = data.groupby("Quarter")["Total"].sum().reset_index()
                fig = px.bar(quarterly, x=["Q1", "Q2", "Q3", "Q4"], y="Total", color="Total", title="Quarterly Sales",
                             color_continuous_scale="Bluered")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "🏆 Top Products":
                top_products = data.groupby("Product Name")["Total"].sum().nlargest(10).reset_index()
                fig = px.bar(top_products, x="Product Name", y="Total", color="Total", title="Top Products",
                             color_continuous_scale="Tealgrn")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "🛒 Category-wise Sales":
                category = data.groupby("Product Category")["Total"].sum().reset_index()
                fig = px.pie(category, names="Product Category", values="Total", title="Category-wise Sales",
                             color_discrete_sequence=px.colors.sequential.RdBu)
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "🙋‍♂️ Top Customers":
                customers = data.groupby("Customer Name")["Total"].sum().nlargest(10).reset_index()
                fig = px.bar(customers, x="Customer Name", y="Total", color="Total", title="Top Customers",
                             color_continuous_scale="Sunset")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "📈 Sales Trend Over Time":
                trend = data.groupby("Order Date")["Total"].sum().reset_index()
                fig = px.line(trend, x="Order Date", y="Total", title="Sales Trend Over Time")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_option == "💰 Profit vs Sales":
                fig = px.scatter(data, x="Total", y="Profit Margin", title="Profit vs Sales",
                                 color="Profit Margin", size_max=15, color_continuous_scale="Turbo")
                st.plotly_chart(fig, use_container_width=True)


