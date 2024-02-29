## Overview

This repository details the process of generating an organized dataset from an existing employee data Excel file (`UpdatedAllocationGen.csv`). In the absence of original subfoldered Excel files, a custom hierarchical structure was created, and data was artificially distributed into subfiles. This was done to simulate real-world data management scenarios, learn the process of organizing data, and subsequently join and analyze the dataset.

## Employee Data Processing Workflow

### 1. Creating Subfiles

A Python script named `Employee data.ipynb` was developed to mimic the original dataset structure. The script reads the existing Excel file, filters data based on predefined keywords, cities, and employee levels, and saves the filtered data into CSV files. Each CSV file represents a combination of city and industry sector (keyword). The generated folder structure is:

```
C:\Users\gagan\Downloads\Memsys\Level {level} employees\{city}\{keyword}.csv
```

### 2. Folder Structure

The hierarchical structure was artificially created based on employee levels, cities, and industry sectors (keywords). This structure aims to organize the data logically, facilitating easier data management and retrieval.

### 3. Reasoning

The process of creating this hierarchy and distributing data into subfiles was necessary due to the unavailability of the original subfoldered Excel files. This approach was adopted to simulate a scenario where data is structured across different levels and categories.

## Deleting Subfolders and Moving Files

Once the data was organized into the hierarchical structure, a Python script named `Delete subfolders.ipynb` was developed. This script deletes unnecessary subfolders and moves their content to the previous folder, simplifying the dataset structure.

### Reasoning

Deleting subfolders and consolidating files into the parent folder was done to streamline the dataset. This operation was performed after creating the artificial hierarchy to maintain a clean and organized dataset for future analysis.

## Instructions for Use

1. **Execute Python Scripts:**
    - Run `Employee data.ipynb` to create subfiles and organize the data.
    - Run `Delete subfolders.ipynb` to delete unnecessary subfolders and move files.
2. **Review Output:** Examine the resulting hierarchical folder structure, ensuring files are correctly organized.
3. **Additional Processing:** Conduct any further data processing or statistical analysis required on the organized dataset.

Feel free to reach out for any further clarification or assistance. Happy data processing!
