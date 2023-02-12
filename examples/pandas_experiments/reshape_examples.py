# import pandas module
import pandas as pd

print('Inside...')

# making dataframe
df = pd.read_csv('/workspaces/OpenAIExperiments/examples/docs/nba.csv')

# it was print the first 5-rows
print(df.head())

# reshape the dataframe using stack() method
df_stacked = df.stack()
  
print(df_stacked.head(26))

# unstack() method
df_unstacked = df_stacked.unstack()
print(df_unstacked.head(10))

# it takes two columns "Name" and "Team"
df_melt = df.melt(id_vars =['Name', 'Team']) 
print(df_melt.head(10))
