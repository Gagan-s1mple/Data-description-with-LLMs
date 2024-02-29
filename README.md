# Memsys Project Files Readme

## Project Overview

This repository organizes project files for the Memsys company, focusing on employee data across different levels, cities, and industries.

## Folder Hierarchy

The project files adhere to the following hierarchy:

```
C:\Users\gagan\Downloads\Memsys project files\
    Memsys company without subfolders\
        Level {level} employees\
            {cities}\
                {keywords}.csv
```

Ignore the folder path names since it was used in a local system

### Levels

Employee data is classified into various levels, ranging from Level 1 to Level 11.

### Cities

Data within each level is further categorized based on the following cities:

- Bangalore
- Noida
- Chennai
- Pune
- Belgaum
- New Delhi
- Gurgaon
- Mysore
- Mumbai
- Kolkata
- Hyderabad
- Bhubaneswar
- Thiruvananthapuram
- Chicago
- New York
- Austin
- San Francisco
- Berlin
- London
- Singapore

### Keywords

Within each city folder, CSV files are organized based on industry keywords. The keywords encompass a wide range of sectors, including:

- CXO
- Retail
- Banking
- Healthcare
- Insurance
- Manufacturing
- Infotainment
- Media
- Communications
- Networking
- Embedded
- Education
- Government
- Public Sector
- MSME
- eCommerce
- Digital Transformations
- Life Sciences
- Energy
- Emerging Technologies
- FMCG
- Transportation
- Finance
- HRM
- Purchase
- Sales & Marketing
- Admin

## Data Processing

To facilitate analysis, Excel files within the hierarchy need to be flattened. Tables should then be joined to create a consolidated dataset. This unified dataset is intended to be uploaded to a DuckDB database for efficient storage and retrieval.

## Statistical Analysis

Once the unified dataset is created and stored in DuckDB, it can be subjected to statistical analysis. Common statistical measures such as mean, median, standard deviation, and percentile can be calculated to gain insights into employee data trends.

## How to Use

1. Navigate to the desired level, city, and keyword folder.
2. Retrieve the CSV files for the specific level, city, and industry keyword.
3. Use the provided data processing script (not provided) to flatten and join the tables.
4. Upload the processed data to DuckDB for further analysis.
5. Perform statistical analysis on the unified dataset stored in DuckDB.

## Notes

- Ensure proper permissions for accessing and modifying project files.
- Preserve data integrity during processing to avoid loss or corruption.
- Periodically update the repository with new data to maintain information currency.

Feel free to reach out for any clarification or assistance. Happy analyzing!
