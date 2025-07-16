"""
This script converts the data from csv to df
Manipulates the df to get Relevant Info
Finally Checks the Distribution of the dataset
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("integrated_flood_risk_assessment.csv")
print(df.dtypes)

subset = df[[
    "Date", "Precipitation", "Station", "Year", "Storm_ID",
    "Storm_Duration", "Rainfall_Intensity", "Flood_Risk_Category", "Flood_Risk_Score"
]]
subset["Date"] = pd.to_datetime(subset["Date"], errors='coerce')
print(subset.describe())

subset[["Precipitation", "Storm_Duration", "Rainfall_Intensity", "Flood_Risk_Score"]].hist(
    bins=30,
    figsize=(10, 8)
)

plt.tight_layout()
plt.savefig("histogram.pdf")  # Save to PDF
plt.show()