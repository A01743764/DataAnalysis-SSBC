# Data Analysis Project - Player Perfomances in E-Sports (SSBC) 

## Description
This project analyzes the performance of 13 brackets simulated for the game Super Smash Bros Crusade, processing raw data from Challonge to uncover victory patterns, rivalries, and performance metrics.
**Objective:** Transform unstructured JSONs into an interactive Dashboard for decision-making.

## Technologies Used
* **Python (Pandas):** Data extraction, cleaning, and transformation (ETL).
* **SQL Server:** Analytical queries and business logic validation.
* **Power BI:** Data visualization and storytelling.

Pipeline  
1. **Ingestion:** Reading multiple tournament JSON files.  
2. **Cleaning:**  
   * Name normalization (e.g., "Dr Mario" vs "Dr. Mario").  
   * Score parsing (e.g., "2-1" → Winner: 2, Loser: 1).  
   * Creation of calculated metrics (Game Difference).  
3. **Analysis:** Classification of victories into "Sweep" (3-0), "Solid," and "Close."  
4. **Visualization:** Interactive dashboard.  

## Results and Insights

### Key Findings:
* **Tournament King:** Marth has the highest Win Rate (X%).   
* **Rivalry:** The heatmap shows that Escanor loses 80% of the time against Bowser.  
<img width="1832" height="1055" alt="pag1" src="https://github.com/user-attachments/assets/6ca60910-8839-4e04-9eba-49ad68679194" />
<img width="1832" height="1046" alt="pag2" src="https://github.com/user-attachments/assets/1c0782b9-fbaa-411a-9f17-52874ad6f4a4" />
<img width="1818" height="1041" alt="pag3" src="https://github.com/user-attachments/assets/69c3c98d-86c9-428c-885d-964b2b8e1c55" />


## Project Structure
* `/Scripts`: Python code to reproduce the cleaning process.  
* `/Dashboard`: .pbix file and PDF of the final report.  
* `/Data`: Processed data ready for analysis.  
