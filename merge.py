import pandas as pd

# Load the two datasets
df1 = pd.read_csv('main.csv')
df2 = pd.read_csv('filtered_doc_details.csv')

# Merge the datasets based on a common key
merged_df = pd.merge(df1, df2, on='Doctor_id', how='inner')  # Replace 'common_key' with the actual common key in the datasets

# Perform necessary data processing and analysis on the merged dataset
# ...

# Save the merged dataset to a new file if needed
merged_df.to_csv('merged_dataset.csv', index=False)
