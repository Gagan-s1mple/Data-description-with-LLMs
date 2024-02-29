import os
import pandas as pd

def concatenate_csv_files(root_folder, output_file):
    all_dataframes = []

    for employee_level_folder in os.listdir(root_folder):
        employee_level_path = os.path.join(root_folder, employee_level_folder)
        if os.path.isdir(employee_level_path):
            for city_folder in os.listdir(employee_level_path):
                city_path = os.path.join(employee_level_path, city_folder)
                if os.path.isdir(city_path):
                    for csv_file in os.listdir(city_path):
                        if csv_file.endswith('.csv'):
                            csv_path = os.path.join(city_path, csv_file)
                            df = pd.read_csv(csv_path)
                            all_dataframes.append(df)

    # Concatenate all dataframes vertically
    result_df = pd.concat(all_dataframes, ignore_index=True)

    # Save the concatenated dataframe to a new CSV file
    result_df.to_csv(output_file, index=False)

# Replace 'your_root_folder' with the actual path to your root folder
# Replace 'output_combined.csv' with the desired output file name
concatenate_csv_files('/Users/anishnavali/Personal/Work/Memsys company without subfolders', 'memsys_combined.csv')
