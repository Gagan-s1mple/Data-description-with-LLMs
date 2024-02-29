import pandas as pd

# Load the CSV file
data = pd.read_csv('/Users/anishnavali/Personal/Work/memsys_combined copy.csv')

# Remove duplicate rows
duplicate_rows = data.drop_duplicates()

# Print the result
duplicate_rows.to_csv('/Users/anishnavali/Personal/Work/memsys_combined copy.csv')