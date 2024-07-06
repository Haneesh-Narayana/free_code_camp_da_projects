import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

# Load data using pandas
data = pd.read_csv("/content/flat-ui__data-Sat Jul 06 2024.csv")

# Select relevant columns with descriptive names
years = data["Year"]
sea_levels = data["CSIRO Adjusted Sea Level"]

# Check for missing values (optional)
if data.isnull().values.any():
    print("WARNING: Missing values found in the data. Consider handling them appropriately.")
    # Handle missing values (e.g., imputation, removal)

# Full dataset linear regression
slope_full, intercept_full, r_value_full, p_value_full, std_err_full = stats.linregress(years, sea_levels)

# Calculate predicted sea level for 2050 (full data)
predicted_sea_level_2050_full = slope_full * 2050 + intercept_full

# Generate x-values for full data regression line
x_fit_full = np.linspace(min(years), max(years), 100)

# Calculate y-values for full data regression line
y_fit_full = slope_full * x_fit_full + intercept_full

# Recent data subset (year 2000 onwards)
recent_years = years[years >= 2000]
recent_sea_levels = sea_levels[years >= 2000]

# Linear regression for recent data
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = stats.linregress(recent_years, recent_sea_levels)

# Calculate predicted sea level for 2050 (recent data)
predicted_sea_level_2050_recent = slope_recent * 2050 + intercept_recent

# Generate x-values for recent data regression line
x_fit_recent = np.linspace(min(recent_years), max(recent_years), 100)

# Calculate y-values for recent data regression line
y_fit_recent = slope_recent * x_fit_recent

# Create the scatter plot
plt.figure(figsize=(10, 6))  # Set plot size for better readability

plt.scatter(years, sea_levels, label='Sea Level (inches)')

# Plot full data regression line
plt.plot(x_fit_full, y_fit_full, color='red', label='Full Data Best Fit (%.2f in/year)' % slope_full)

# Highlight full data prediction for 2050
plt.scatter(2050, predicted_sea_level_2050_full, marker='o', color='green', label='Full Data - 2050 (%.2f in)' % predicted_sea_level_2050_full)

# Plot recent data regression line
plt.plot(x_fit_recent, y_fit_recent, color='blue', label='Recent Data Best Fit (%.2f in/year)' % slope_recent)

# Highlight recent data prediction for 2050
plt.scatter(2050, predicted_sea_level_2050_recent, marker='o', color='purple', label='Recent Data - 2050 (%.2f in)' % predicted_sea_level_2050_recent)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend with informative labels
plt.legend()

# Show the plot with grid for better readability
plt.grid(True)
plt.tight_layout()  # Adjust spacing to prevent overlapping elements
plt.show()
