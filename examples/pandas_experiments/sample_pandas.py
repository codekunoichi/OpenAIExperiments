import pandas as pd

# Create a sample dataframe
data = {'col1': [1, 2, 3, 4, 5, 1, 2, 3]}
df = pd.DataFrame(data)

# Find unique values in a column
unique_values = df['col1'].unique()
print(unique_values)
