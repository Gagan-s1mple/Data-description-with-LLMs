# Data-description-with-LLMs

# Data Flattening and Analysis Project

This project aims to organize and analyze a vast amount of data distributed across a complex folder hierarchy. The data is stored in CSV files within folders categorized by city, department, and employee level. The workflow involves flattening the hierarchy, performing statistical analysis on the data, storing the results in a DuckDB database, and creating a chatbot interface for querying the database.

## Project Overview

### 1. Data Flattening
- **Folder Hierarchy:** Hundreds of folders with varying city names, departments, and employee levels.
- **Example CSV File Path:** "C:\Users\gagan\Downloads\Memsys company\Level 11 employees\Bangalore\Banking\Banking.csv"

### 2. Statistical Analysis
- Extracted data from CSV files is subjected to statistical analysis.
- Common statistics include average, median, mode, etc.

### 3. DuckDB Database
- The analyzed data is stored in a DuckDB database for efficient querying.

### 4. Chatbot Interface
- A chatbot, connected to the DuckDB database, provides a user-friendly interface to query information from the data.
- Example Queries:
  - "How many people from Austin are level 1 employees?"
  - "What is the average salary in the Banking department?"
  - "Tell me the distribution of employees across cities."

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Setup Dependencies:**
   - Detailed instructions for setting up dependencies are provided in the repository.

3. **Run the Project Scripts:**
   - Execute scripts in the specified order to flatten the hierarchy, perform statistical analysis, and store data in DuckDB.

## Contributing

- Contributions are welcome! Feel free to submit pull requests or open issues for improvements or bug fixes.

## License

- This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Future Considerations

- Explore and define additional functionalities for the chatbot.
- Enhance and optimize the data analysis process.
- Consider integrating with other databases or platforms.

Feel free to customize this readme based on your project's specific details and future plans.
