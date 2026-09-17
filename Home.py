import streamlit as st
import pandas as pd


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Household Power Consumption",
    layout="wide"
)


# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("household_cleandata.csv")


# =====================================================
# TITLE
# =====================================================

st.title("Household Power Consumption Analysis")

st.write(
    "Understanding household electricity consumption through "
    "data cleaning, feature engineering and exploratory data analysis."
)


# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.divider()

st.header("Project Overview")

st.write(
    "This project analyzes minute-level household electricity consumption "
    "data. The analysis includes data cleaning, feature engineering and "
    "exploration of electricity consumption patterns."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Data Cleaning")
    st.write(
        "Invalid values are identified and the dataset is prepared "
        "for analysis."
    )

with col2:
    st.subheader("Feature Engineering")
    st.write(
        "Date and time information is used to create useful analytical "
        "features."
    )

with col3:
    st.subheader("Exploratory Analysis")
    st.write(
        "Univariate, bivariate and multivariate analysis is performed "
        "to understand the data."
    )


# =====================================================
# DATASET SUMMARY
# =====================================================

st.divider()

st.header("Data Quality")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", f"{len(df):,}")

with col2:
    st.metric("Missing Values", f"{df.isnull().sum().sum():,}")

with col3:
    st.metric("Duplicate Records", f"{df.duplicated().sum():,}")

with col4:
    st.metric(
        "Numeric Features",
        df.select_dtypes(include="number").shape[1]
    )

# =====================================================
# DATASET PREVIEW
# =====================================================

st.divider()

st.header("Dataset Preview")

with st.expander("View Dataset Preview"):
    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# ANALYSIS COVERED
# =====================================================
st.divider()

st.header("Analysis Workflow")

st.write(
    "Raw Data → Data Cleaning → Feature Engineering → EDA → Insights"
)


# =====================================================
# FEATURES / COLUMN GUIDE
# =====================================================

st.divider()

st.header("Features")

st.write(
    "A simple guide to understand what each column represents."
)

features = {
    "Date": "The date when the data was recorded.",
    "Time": "The time when the data was recorded.",
    "Global_active_power": "The main power used by the household.",
    "Global_reactive_power": "The reactive power used by the household.",
    "Voltage": "The voltage level recorded at that time.",
    "Global_intensity": "The amount of electric current being used.",
    "Sub_metering_1": "Power used by the first sub-meter.",
    "Sub_metering_2": "Power used by the second sub-meter.",
    "Sub_metering_3": "Power used by the third sub-meter.",
    "Day_Name": "The day of the week, such as Monday or Tuesday.",
    "Month_Name": "The month of the year.",
    "Year": "The year in which the data was recorded.",
    "Hours": "The hour extracted from the recorded time.",
    "Minutes": "The minute extracted from the recorded time.",
    "Total_metering": (
        "The total of Sub_metering_1, Sub_metering_2 "
        "and Sub_metering_3."
    )
}

feature_df = pd.DataFrame(
    list(features.items()),
    columns=["Column Name", "Description"]
)

st.dataframe(
    feature_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.header("Technologies Used")

st.write(
    "Python | Pandas | NumPy | Matplotlib | Seaborn | Streamlit"
)


# =====================================================
# DASHBOARD STRUCTURE
# =====================================================

st.divider()

st.header("Dashboard Structure")

st.write(
    "Use the pages in the sidebar to explore the complete analysis."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Home")
    st.write(
        "Project overview, dataset summary and feature guide."
    )

with col2:
    st.subheader("EDA Analysis")
    st.write(
        "Explore distributions, relationships and time-based patterns."
    )

with col3:
    st.subheader("Conclusion")
    st.write(
        "Review key observations, findings and future scope."
    )

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Household Power Consumption")

st.sidebar.divider()

st.sidebar.subheader("Dashboard")

st.sidebar.write(
    "Use the navigation menu to explore the project."
)

st.sidebar.divider()

st.sidebar.subheader("Project Information")

st.sidebar.write(
    "This dashboard presents an exploratory analysis "
    "of household electricity consumption data."
)

st.sidebar.divider()

st.sidebar.caption("Built with Python and Streamlit")