# Memsys Employee Data Flattening and Joining Readme

This repository focuses on the significant challenges of flattening and joining employee data for Memsys company. The primary emphasis is on consolidating data from various levels, cities, and sectors into a unified dataset for effective analysis. Here's a detailed overview of the process:

## Flattening Hierarchy

The Python script `flatten_hierarchy.py` is crucial in this process. It generalizes path names, ensuring flexibility across different machines, and concatenates CSV files from various levels, cities, and keywords into a single comprehensive dataset. The result, `memsys_combined.csv`, serves as a flattened representation of the original hierarchical structure.

## Joining Data

Following the flattening process, the key objective is to join tables based on relevant key columns. This enables the creation of a cohesive dataset that captures information across different dimensions such as levels, cities, and sectors. The joined dataset facilitates a holistic view of the employee data, supporting more insightful analyses.

## Cleaning Data

While the flattening and joining processes are crucial, it's essential to note that the data is also subject to cleaning scripts (`memsys_cleaning1.py`, `memsys_cleaning2.py`, `removing_duplicates.py`, `delete_rows_with_invalid_start_date.py`). These scripts ensure that the dataset is accurate, consistent, and free from duplicates, enhancing the overall integrity of the data.

## Instructions for Use

1. **Flatten Hierarchy:**
   - Execute `flatten_hierarchy.py` by providing the root folder path to generate `memsys_combined.csv`.

2. **Joining Data:**
   - Utilize the flattened `memsys_combined.csv` as the primary dataset for in-depth analysis.
   - Implement additional join operations using relevant key columns for comprehensive insights.

3. **Cleaning Data:**
   - Prior to analysis, consider running the cleaning scripts (`memsys_cleaning1.py`, `memsys_cleaning2.py`, `removing_duplicates.py`, `delete_rows_with_invalid_start_date.py`) to ensure data accuracy and consistency.

4. **Review Output:**
   - Examine the joined and cleaned dataset to ensure a consolidated, accurate, and analytically valuable representation of the employee data.

  **Ignore the path names. They were just made in a different machine (MACOS)**

This repository places a significant emphasis on the challenges of flattening and joining data, while also acknowledging the importance of maintaining data integrity through cleaning processes.

Feel free to reach out for any further clarification or assistance. Happy data processing!
