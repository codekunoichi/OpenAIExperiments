import os
import pandas as pd

print(os.getcwd())

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel('/workspaces/OpenAIExperiments/examples/docs/2.0 Homepage Status Count Clicks 20230129-20230131.xlsx')

print('\n\n**** Excel Columns ****')
print(df.columns)
# Show the first 5 rows of the DataFrame
# print(df.head())

# Get unique values from 'column_1'
unique_values = df['Tracked Event Name'].unique()

# Print the result
print('\n\n**** Unique Values Tracked Event Name ****')
print(unique_values)

# End User ID
unique_values = df['End User ID'].unique()

# Print the result
print('\n\n**** Unique End User IDs ****')
print(unique_values)

# Wm Account
unique_values = df['Wm Account'].unique()

# Print the result
print('\n\n**** Unique Values Wm Accounts ****')
print(unique_values)

# Find the average time spend by the WM Account
grouped = df.groupby('Wm Account')['Avg Session Duration Min By User Trackedevent'].mean()

print('\n\n**** Group by Wm Account Name, then find average time spent ****')
print(grouped)

print (grouped.size)