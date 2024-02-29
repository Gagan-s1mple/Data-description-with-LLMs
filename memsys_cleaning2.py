# import pandas as pd

# def shift_data_on_invalid_date(csv_path):
#     df = pd.read_csv(csv_path)

#     # Check if 'AllocationStartDate' column exists
#     if 'AllocationStartDate' in df.columns:
#         # Identify rows where 'AllocationStartDate' is not a valid date
#         invalid_date_rows = pd.to_datetime(df['AllocationStartDate'], errors='coerce').isnull()

#         # Move data to the right for rows with invalid 'AllocationStartDate'
#         for index, row in df[invalid_date_rows].iterrows():
#             # Get the index of 'AllocationStartDate'
#             start_date_index = row.index.get_loc('AllocationStartDate')

#             # Move data to the right starting from 'AllocationStartDate' index
#             df.iloc[index, start_date_index + 1:] = row.iloc[start_date_index:].tolist()

#         # Drop the original 'AllocationStartDate' column
#         df = df.drop(columns=['AllocationStartDate'])

#         # Drop rows where 'AllocationStartDate' is not a valid date
#         df = df[~invalid_date_rows]

#         # Save the cleaned dataframe back to the CSV file
#         df.to_csv(csv_path, index=False)

# Replace 'your_csv_file.csv' with the actual path to your CSV file

# import pandas as pd

# def shift_columns_on_invalid_start_date(csv_path):
#     df = pd.read_csv(csv_path)

#     # Check if 'AllocationStartDate' column exists
#     if 'AllocationStartDate' in df.columns:
#         # Identify rows where 'AllocationStartDate' is not a valid date
#         invalid_date_rows = pd.to_datetime(df['AllocationStartDate'], errors='coerce').isnull()

#         # Specify columns to shift to the left
#         columns_to_shift = ['AllocationEndDate', 'Utilization', 'EmployeeStatus.1', 'PrevPerformance1To5', 
#                             'CurPerformance1To6', 'CSR1To5', 'EmployeeID']

#         # Move data to the left for specified columns in rows with invalid 'AllocationStartDate'
#         for column in columns_to_shift:
#             df.loc[invalid_date_rows, column] = df.loc[invalid_date_rows, column].shift(1)

#         # Drop the original 'AllocationStartDate' column
#         df = df.drop(columns=['AllocationStartDate'])

#         # Drop rows where 'AllocationStartDate' is not a valid date
#         df = df[~invalid_date_rows]

#         # Save the cleaned dataframe back to the CSV file
#         df.to_csv(csv_path, index=False)

# # Replace 'your_csv_file.csv' with the actual path to your CSV file
# shift_columns_on_invalid_start_date('/Users/anishnavali/Personal/Work/memsys_combined.csv')


import pandas as pd

import pandas as pd

def delete_rows_with_invalid_start_date(csv_path):
    df = pd.read_csv(csv_path)

    # Check if 'AllocationStartDate' column exists
    if 'AllocationStartDate' in df.columns:
        # Identify rows where 'AllocationStartDate' is not a valid date
        invalid_date_rows = pd.to_datetime(df['AllocationStartDate'], errors='coerce').isnull()

        # Drop rows where 'AllocationStartDate' is not a valid date
        df = df[~invalid_date_rows]

        # Save the modified dataframe back to the CSV file
        df.to_csv(csv_path, index=False)

# Replace 'your_csv_file.csv' with the actual path to your CSV file
delete_rows_with_invalid_start_date('/Users/anishnavali/Personal/Work/memsys_combined copy.csv')


