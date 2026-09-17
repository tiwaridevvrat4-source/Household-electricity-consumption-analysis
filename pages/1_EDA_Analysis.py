import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="EDA Analysis",
    layout="wide"
)

df = pd.read_csv("household_cleandata.csv")

st.title("Exploratory Data Analysis")

st.write(
    "Explore household power consumption patterns using "
    "Univariate, Bivariate and Multivariate Analysis."
)

# =====================================================
# ANALYSIS TYPE SELECTOR
# =====================================================

st.sidebar.markdown("## EDA Analysis")
st.sidebar.caption("Explore the dataset through different analytical approaches")

st.sidebar.divider()

analysis_type = st.sidebar.radio(
    "Analysis Type",
    [
        "Univariate Analysis",
        "Bivariate Analysis",
        "Multivariate Analysis"
    ]
)

st.sidebar.divider()

st.sidebar.caption("Household Power Consumption")
st.divider()


# =====================================================
# UNIVARIATE ANALYSIS
# =====================================================

if analysis_type == "Univariate Analysis":

    st.header("Univariate Analysis")

    st.caption(
        "Understand the distribution and spread of individual variables."
    )

    # Variable selection
    column = st.selectbox(
        "Select a variable",
        [
            "Global_active_power",
            "Global_reactive_power",
            "Voltage",
            "Global_intensity",
            "Sub_metering_1",
            "Sub_metering_2",
            "Sub_metering_3",
            "Total_metering"
        ]
    )

    # Convert selected column into numeric
    data = pd.to_numeric(
        df[column],
        errors="coerce"
    ).dropna()

    # Sample data for faster visualization
    if len(data) > 20000:
        data = data.sample(
            20000,
            random_state=42
        )

    # =================================================
    # SUMMARY STATISTICS
    # =================================================

    st.subheader("Summary Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Count",
            f"{len(data):,}"
        )

    with col2:
        st.metric(
            "Mean",
            f"{data.mean():.2f}"
        )

    with col3:
        st.metric(
            "Minimum",
            f"{data.min():.2f}"
        )

    with col4:
        st.metric(
            "Maximum",
            f"{data.max():.2f}"
        )

    # =================================================
    # DISTRIBUTION
    # =================================================

    st.divider()

    st.subheader("Distribution")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(
        data,
        bins=40
    )

    ax.set_title(
        f"Distribution of {column}"
    )

    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

    # =================================================
    # DETAILED STATISTICS
    # =================================================

    st.subheader("Detailed Statistics")

    stats = data.describe().to_frame("Value")

    st.dataframe(
        stats,
        use_container_width=True
    )

    # =================================================
    # INTERPRETATION
    # =================================================

    st.subheader("Interpretation")

    st.write(
        f"The selected variable is **{column}**. "
        "The histogram shows how the values are distributed "
        "across the dataset. Summary statistics provide "
        "information about the central tendency and spread "
        "of the variable."
    )

# =====================================================
# BIVARIATE ANALYSIS
# =====================================================

elif analysis_type == "Bivariate Analysis":

    st.header("Bivariate Analysis")

    st.caption(
        "Explore the relationship between two selected variables."
    )

    # =================================================
    # VARIABLE SELECTION
    # =================================================

    numeric_columns = [
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3",
        "Total_metering"
    ]

    col1, col2 = st.columns(2)

    with col1:
        x = st.selectbox(
            "Select X variable",
            numeric_columns
        )

    with col2:
        y = st.selectbox(
            "Select Y variable",
            numeric_columns,
            index=1
        )

    # =================================================
    # PREPARE DATA
    # =================================================

    plot_df = df[[x, y]].copy()

    plot_df[x] = pd.to_numeric(
        plot_df[x],
        errors="coerce"
    )

    plot_df[y] = pd.to_numeric(
        plot_df[y],
        errors="coerce"
    )

    plot_df = plot_df.dropna()

    # Sample for faster visualization
    if len(plot_df) > 10000:
        plot_df = plot_df.sample(
            10000,
            random_state=42
        )

    # =================================================
    # CORRELATION
    # =================================================

    correlation = plot_df[x].corr(plot_df[y])

    st.subheader("Relationship Summary")

    st.metric(
        "Correlation",
        f"{correlation:.2f}"
    )

    # =================================================
    # SCATTER PLOT
    # =================================================

    st.divider()

    st.subheader("Relationship Visualization")

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        data=plot_df,
        x=x,
        y=y,
        alpha=0.5,
        ax=ax
    )

    ax.set_title(
        f"{x} vs {y}"
    )

    ax.set_xlabel(x)
    ax.set_ylabel(y)

    st.pyplot(fig)

    # =================================================
    # DETAILED STATISTICS
    # =================================================

    st.subheader("Selected Variables Statistics")

    stats_df = plot_df[[x, y]].describe().T

    st.dataframe(
        stats_df,
        use_container_width=True
    )

    # =================================================
    # INTERPRETATION
    # =================================================

    st.subheader("Interpretation")

    st.write(
        f"The scatter plot shows the relationship between "
        f"**{x}** and **{y}**. The calculated correlation "
        f"between these variables is **{correlation:.2f}**. "
        "The scatter pattern helps identify the direction "
        "and strength of the relationship."
    )


# =====================================================
# MULTIVARIATE ANALYSIS
# =====================================================

else:

    st.header("Multivariate Analysis")

    st.caption(
        "Explore multiple electricity-related variables together."
    )

    # =================================================
    # PREPARE DATA
    # =================================================

    plot_df = df[
        [
            "Hours",
            "Global_active_power",
            "Global_intensity",
            "Voltage"
        ]
    ].copy()

    # Convert numeric columns
    numeric_cols = [
        "Hours",
        "Global_active_power",
        "Global_intensity",
        "Voltage"
    ]

    for col in numeric_cols:
        plot_df[col] = pd.to_numeric(
            plot_df[col],
            errors="coerce"
        )

    plot_df = plot_df.dropna()

    # Sample for faster visualization
    if len(plot_df) > 10000:
        plot_df = plot_df.sample(
            10000,
            random_state=42
        )

    # =================================================
    # MULTIVARIATE VISUALIZATION
    # =================================================

    st.subheader("Multivariable Relationship")

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.scatterplot(
        data=plot_df,
        x="Hours",
        y="Global_active_power",
        hue="Global_intensity",
        size="Voltage",
        alpha=0.6,
        ax=ax
    )

    ax.set_title(
        "Hour vs Global Active Power"
    )

    ax.set_xlabel("Hour")
    ax.set_ylabel("Global Active Power")

    st.pyplot(fig)

    st.write(
        "This visualization combines hour, global active power, "
        "global intensity and voltage to observe how electricity "
        "consumption changes across different hours."
    )

    # =================================================
    # CORRELATION HEATMAP
    # =================================================

    st.divider()

    st.subheader("Correlation Heatmap")

    st.caption(
        "Correlation values show the strength and direction "
        "of relationships between numerical variables."
    )

    corr_cols = [
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3",
        "Total_metering"
    ]

    corr_data = df[corr_cols].copy()

    corr_data = corr_data.apply(
        pd.to_numeric,
        errors="coerce"
    )

    corr = corr_data.corr()

    fig, ax = plt.subplots(figsize=(11, 7))

    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=ax
    )

    ax.set_title(
        "Correlation Heatmap"
    )

    st.pyplot(fig)

    # =================================================
    # INTERPRETATION
    # =================================================

    st.subheader("Interpretation")

    st.write(
        "Multivariate analysis helps us examine several "
        "electricity-related variables together. The scatter "
        "plot combines time, active power, intensity and voltage, "
        "while the correlation heatmap provides an overview of "
        "relationships among the numerical variables."
    )