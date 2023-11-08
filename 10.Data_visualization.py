import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import numpy as np

# Now that we have cleaned the data, the analysis can be performed

# Load the dataset into a pandas DataFrame
file_path = '9.CLEAN_DATA.csv'  # Replace with your file path
used_cars_data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(used_cars_data.head())

# Get the DataFrame's basic information
print(used_cars_data.info())

# Check for missing values in each column
print(used_cars_data.isnull().sum())

# Set pandas to display numbers with a maximum of two decimal places
pd.set_option('display.float_format', '{:.2f}'.format)

# Summary statistics for numeric columns
print(used_cars_data.describe())

# Create a new boolean column 'In Budapest' that is True if 'Location' contains 'Budapest'
used_cars_data['In Budapest'] = used_cars_data['Location'].str.contains('Budapest', na=False)

# Display the proportion of cars in and outside Budapest
print(used_cars_data['In Budapest'].value_counts(normalize=True))

# Descriptive statistics for price within Budapest
price_stats_budapest = used_cars_data[used_cars_data['In Budapest']]['Price'].describe()

# Descriptive statistics for price outside Budapest
price_stats_outside = used_cars_data[~used_cars_data['In Budapest']]['Price'].describe()

# Extract the year from the 'Year' column and convert it to an integer, if not already done
used_cars_data['Year Extracted'] = used_cars_data['Year'].str.extract(r'(\d{4})').astype(int)

# Confirm the column has been added
print(used_cars_data.columns)

# Create a DataFrame for cars older than the year 2012
cars_older = used_cars_data[used_cars_data['Year Extracted'] < 2012]

# Create a DataFrame for cars from the year 2012 onwards
cars_newer = used_cars_data[used_cars_data['Year Extracted'] >= 2012]

# Display the statistics
print("Price Statistics for Cars in Budapest:")
print(price_stats_budapest)
print("\nPrice Statistics for Cars Outside Budapest:")
print(price_stats_outside)

# Display the counts for each group
print("Number of cars older than 2012:", cars_older.shape[0])
print("Number of cars from 2012 onwards:", cars_newer.shape[0])

# Group 1: Cars in Budapest and older than 2012
budapest_older_cars = used_cars_data[(used_cars_data['In Budapest']) & (used_cars_data['Year Extracted'] < 2012)]

# Group 2: Cars in Budapest and from 2012 onwards
budapest_newer_cars = used_cars_data[(used_cars_data['In Budapest']) & (used_cars_data['Year Extracted'] >= 2012)]

# Group 3: Cars outside Budapest and older than 2012
outside_older_cars = used_cars_data[(~used_cars_data['In Budapest']) & (used_cars_data['Year Extracted'] < 2012)]

# Group 4: Cars outside Budapest and from 2012 onwards
outside_newer_cars = used_cars_data[(~used_cars_data['In Budapest']) & (used_cars_data['Year Extracted'] >= 2012)]

# Display the counts for each group
print("Number of cars in Budapest, older than 2012:", budapest_older_cars.shape[0])
print("Number of cars in Budapest, from 2012 onwards:", budapest_newer_cars.shape[0])
print("Number of cars outside Budapest, older than 2012:", outside_older_cars.shape[0])
print("Number of cars outside Budapest, from 2012 onwards:", outside_newer_cars.shape[0])


# Define a function to calculate the IQR
def iqr(series):
    return series.quantile(0.75) - series.quantile(0.25)


# Calculate median prices and IQR for visualization
median_price_budapest_older = budapest_older_cars['Price'].median()
median_price_outside_older = outside_older_cars['Price'].median()
iqr_budapest_older = iqr(budapest_older_cars['Price'])
iqr_outside_older = iqr(outside_older_cars['Price'])

median_price_budapest_newer = budapest_newer_cars['Price'].median()
median_price_outside_newer = outside_newer_cars['Price'].median()
iqr_budapest_newer = iqr(budapest_newer_cars['Price'])
iqr_outside_newer = iqr(outside_newer_cars['Price'])

# Bar chart for cars older than 2012
categories_older = ['Budapest (<2012)', 'Outside (<2012)']
median_prices_older = [median_price_budapest_older, median_price_outside_older]
iqr_values_older = [iqr_budapest_older, iqr_outside_older]

plt.figure(figsize=(8, 5))
bars_older = plt.bar(categories_older, median_prices_older, color=['blue', 'red'], yerr=iqr_values_older, capsize=5)
plt.title('Median Prices of Cars Older Than 2012')
plt.xlabel('Category')
plt.ylabel('Median Price (HUF)')
plt.xticks(rotation=45)
for bar in bars_older:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{round(yval, 2):,}', ha='center', va='bottom')
plt.tight_layout()
plt.show()

# Bar chart for cars from 2012 onwards
categories_newer = ['Budapest (>=2012)', 'Outside (>=2012)']
median_prices_newer = [median_price_budapest_newer, median_price_outside_newer]
iqr_values_newer = [iqr_budapest_newer, iqr_outside_newer]

plt.figure(figsize=(8, 5))
bars_newer = plt.bar(categories_newer, median_prices_newer, color=['blue', 'red'], yerr=iqr_values_newer, capsize=5)
plt.title('Median Prices of Cars From 2012 Onwards')
plt.xlabel('Category')
plt.ylabel('Median Price (HUF)')
plt.xticks(rotation=45)
for bar in bars_newer:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{round(yval, 2):,}', ha='center', va='bottom')
plt.tight_layout()
plt.show()


def calculate_effect_size(group1, group2):
    u, _ = mannwhitneyu(group1, group2, alternative='two-sided')
    n1 = len(group1)
    n2 = len(group2)
    delta = (2 * u) / (n1 * n2) - 1
    return delta


def report_mannwhitneyu_results(group1, group2, group1_name, group2_name):
    stat, p_value = mannwhitneyu(group1, group2, alternative='two-sided')
    median1 = np.median(group1)
    median2 = np.median(group2)
    effect_size = calculate_effect_size(group1, group2)

    print(f"Mann-Whitney U test comparing {group1_name} and {group2_name}:")
    print(f"U-statistic: {stat}")
    print(f"P-value: {p_value}")
    print(f"Median Price {group1_name}: {median1}")
    print(f"Median Price {group2_name}: {median2}")
    print(f"Effect Size (Cliff's Delta): {effect_size:.3f}")
    if p_value < 0.05:
        print("The result is statistically significant: We reject the null hypothesis.")
    else:
        print("The result is not statistically significant: We fail to reject the null hypothesis.")


# Perform the Mann-Whitney U test and report results for older cars
report_mannwhitneyu_results(
    budapest_older_cars['Price'],
    outside_older_cars['Price'],
    'Budapest (<2012)',
    'Outside (<2012)'
)

# Perform the Mann-Whitney U test and report results for newer cars
report_mannwhitneyu_results(
    budapest_newer_cars['Price'],
    outside_newer_cars['Price'],
    'Budapest (>=2012)',
    'Outside (>=2012)'
)

# In summary, the test indicates that for older cars (pre-2012), there is a significant difference
# in prices between those sold in Budapest and those sold outside Budapest. However, for newer cars (2012 and onwards),
# no significant price difference is detected based on the location of sale.

# This could mean that the market values older cars differently in Budapest compared to outside,
# while newer cars have more consistent pricing regardless of location.

# To directly answer the question:
# For older cars, there is evidence to suggest that there might be a difference in pricing between Budapest
# and outside of Budapest.
# For newer cars, the analysis suggests that people are not selling cars for
# significantly different prices outside of Budapest compared to within Budapest.
