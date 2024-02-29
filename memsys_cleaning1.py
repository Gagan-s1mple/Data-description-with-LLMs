import os
import pandas as pd

def filter_csv_files(root_folder):
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

                            # Assuming the columns are 'employee_level', 'city', 'department'
                            expected_columns = ['level', 'work_location', 'DepartmentBU']

                            # Check if all expected columns are present in the dataframe
                            if all(column in df.columns for column in expected_columns):
                                # Filter rows that don't belong in the current file
                                df = df[(df['level'] == employee_level_folder) & (df['work_location'] == city_folder)]

                                # Save the filtered dataframe back to the CSV file
                                df.to_csv(csv_path, index=False)

# Replace 'your_root_folder' with the actual path to your root folder
filter_csv_files('/Users/anishnavali/Personal/Work/Memsys company without subfolders')
