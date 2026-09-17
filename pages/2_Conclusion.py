import streamlit as st
import pandas as pd


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Conclusion & Insights",
    layout="wide"
)



# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("household_cleandata.csv")


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Conclusion & Insights")

st.sidebar.caption(
    "Key observations from the household power consumption analysis."
)

st.sidebar.divider()

st.sidebar.subheader("Project Summary")

st.sidebar.write(
    "This section presents the major observations and "
    "overall conclusion obtained from the exploratory analysis."
)

st.sidebar.divider()

st.sidebar.caption("Household Power Consumption")


# =====================================================
# PAGE TITLE
# =====================================================

st.title("Conclusion & Insights")

st.write(
    "Key observations and conclusions obtained from the "
    "exploratory analysis of household power consumption."
)


# =====================================================
# KEY FINDINGS
# =====================================================

st.divider()

st.header("Key Findings")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Power Consumption")

    st.write(
        "Global active power shows variation across the dataset, "
        "indicating that household electricity consumption changes "
        "over time."
    )

    st.subheader("Voltage and Intensity")

    st.write(
        "Voltage and global intensity provide additional information "
        "about the electrical conditions and power usage of the household."
    )


with col2:

    st.subheader("Sub-Metering")

    st.write(
        "The three sub-metering variables represent electricity usage "
        "from different parts of the household. Total metering combines "
        "these sub-metering measurements."
    )

    st.subheader("Time-Based Patterns")

    st.write(
        "Year, month, day and hour based analysis helps identify "
        "changes in household electricity consumption across different "
        "time periods."
    )


# =====================================================
# MAJOR OBSERVATIONS
# =====================================================

st.divider()

st.header("Major Observations")

observations = [
    "Electricity consumption varies across different time periods.",
    "Data cleaning is important because invalid values were present in the dataset.",
    "Date and time features make it possible to study temporal consumption patterns.",
    "Distribution analysis helps identify the spread and unusual observations in numerical variables.",
    "Sub-metering variables provide additional information about household electricity usage.",
    "Correlation analysis helps understand relationships between different electricity-related variables.",
    "Combining power, intensity, voltage and metering variables provides a broader view of household electricity consumption."
]

for observation in observations:
    st.write(f"• {observation}")


# =====================================================
# OVERALL CONCLUSION
# =====================================================

st.divider()

st.header("Overall Conclusion")

st.write(
    "The exploratory data analysis provides an overall understanding "
    "of household electricity consumption and its variation over time. "
    "Data cleaning and feature engineering helped prepare the dataset "
    "for meaningful analysis. Univariate analysis explained individual "
    "variable distributions, while bivariate and multivariate analysis "
    "helped examine relationships among electricity-related variables. "
    "Time-based analysis further highlighted how consumption can vary "
    "across different years, months, days and hours."
)


# =====================================================
# FINAL SUMMARY
# =====================================================

st.divider()

st.subheader("Final Summary")

st.info(
    "The analysis shows that household electricity consumption is "
    "influenced by temporal variation and is better understood by "
    "examining power, intensity, voltage and sub-metering variables together."
)