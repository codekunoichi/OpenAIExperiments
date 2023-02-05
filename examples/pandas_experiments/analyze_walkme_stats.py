import os
import pandas as pd

print(os.getcwd())

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel('/workspaces/OpenAIExperiments/examples/docs/2.0 Homepage Status Count Clicks 20230129-20230131.xlsx')

# Show the first 5 rows of the DataFrame
print(df.head())

# Get unique values from 'column_1'
unique_values = df['Tracked Event Name'].unique()

# Print the result
print(unique_values)

# End User ID
unique_values = df['End User ID'].unique()

# Print the result
print(unique_values)

# Wm Account
unique_values = df['Wm Account'].unique()

# Print the result
print(unique_values)
