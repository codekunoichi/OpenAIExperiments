import pandas as pd

# Create a sample DataFrame
data = {'group': [1, 1, 1, 2, 2, 2], 'value': [3, 5, 2, 4, 1, 6]}
df = pd.DataFrame(data)

# Rank values by 'group' partition
df['rank'] = df.groupby('group')['value'].rank(method='min', ascending=False)

# Show the result
print(df)
