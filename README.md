# Household Power Consumption Analysis

An Exploratory Data Analysis (EDA) project focused on understanding household electricity consumption patterns using Python, Pandas, Matplotlib, Seaborn, and Streamlit.

## Project Overview

This project analyzes minute-level household electricity consumption data to understand power usage patterns and relationships between different electrical variables.

The analysis includes data cleaning, feature engineering, univariate analysis, bivariate analysis, multivariate analysis, and time-based analysis.

## Dataset

The dataset contains household electricity measurements with the following major variables:

- Date
- Time
- Global Active Power
- Global Reactive Power
- Voltage
- Global Intensity
- Sub Metering 1
- Sub Metering 2
- Sub Metering 3

Additional features were created during the analysis:

- Day Name
- Month Name
- Year
- Hours
- Minutes
- Total Metering

## Data Cleaning

The dataset was cleaned by:

- Identifying invalid values represented by `?`
- Removing invalid records
- Converting numerical columns into appropriate numeric data types
- Converting the Date column into datetime format
- Creating additional time-based features

## Exploratory Data Analysis

### 1. Univariate Analysis

Individual variables were analyzed using:

- Distribution plots
- Histograms
- Summary statistics
- Spread and variation analysis

### 2. Bivariate Analysis

Relationships between two variables were explored using:

- Scatter plots
- Correlation analysis
- Statistical summaries

### 3. Multivariate Analysis

Multiple electricity-related variables were analyzed together using:

- Multivariable scatter plots
- Correlation heatmaps
- Time-based relationships

## Streamlit Dashboard

The project has been converted into an interactive Streamlit dashboard with three main sections:

### Home

Provides:

- Project introduction
- Dataset overview
- Column descriptions
- Dashboard structure

### EDA Analysis

Provides interactive:

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Distribution visualizations
- Correlation analysis

### Conclusion & Insights

Summarizes the major observations obtained from the exploratory analysis.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Git & GitHub

## Project Structure

''text
Household/
│
├── Home.py
├── household_cleandata.csv
├── requirements.txt
│
└── pages/
    ├── 1_EDA_Analysis.py
    └── 2_Conclusion_Insights.py
## Installation
## Installation

Clone the repository:

bash
git clone https://github.com/tiwaridevvrat4-source/Household-electricity-consumption-analysis.git
### Navigate to the project directory:
cd Household-electricity-consumption-analysis
### Install the required libraries:
pip install -r requirements.txt
### Run the Streamlit application:
streamlit run Home.py
