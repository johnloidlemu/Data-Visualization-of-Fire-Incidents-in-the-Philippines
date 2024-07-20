# BFP Fire Incidents Analysis (2012-2016)

This project involves the analysis of fire incidents data from 2012 to 2016, provided by the Bureau of Fire Protection (BFP). The project includes data cleaning, analysis, and visualization of the fire incidents through a dashboard.

## Project Structure

- `data/BFP_FireIncidents2012-2016.csv`: The raw dataset containing fire incidents from 2012 to 2016.
- `data/cleaned_data_BFP_FireIncidents2012-2016.csv`: The cleaned dataset used for analysis.
- `Dashboard.py`: The Python script for creating a dashboard to visualize the fire incidents data using Streamlit.
- `Project_Data_Cleaning.ipynb`: Python script for cleaning the dataset (`data/BFP_FireIncidents2012-2016.csv`).
- `Visualization.ipynb`: Python script for visualizing the dataset (`data/cleaned_data_BFP_FireIncidents2012-2016.csv`).

## Installation Steps

1. **Set Up Your Environment**:
   - Ensure Python is installed. Download it from [python.org](https://www.python.org/downloads/).
   - Install the required libraries:
     ```bash
     pip install pandas numpy matplotlib seaborn plotly streamlit
     ```

2. **Download the Dataset**:
   - Obtain `BFP_FireIncidents2012-2016.csv` from the Bureau of Fire Protection or other sources.
   - Place the dataset in the `data/` directory of the project.

3. **Clean the Data**:
   - Open `Project_Data_Cleaning.ipynb` in Jupyter Notebook.
   - Ensure the notebook reads the dataset from the `data/` directory:
     ```python
     raw_data_path = 'data/BFP_FireIncidents2012-2016.csv'
     cleaned_data_path = 'data/cleaned_data_BFP_FireIncidents2012-2016.csv'
     ```
   - Run the notebook to clean the raw dataset and generate `data/cleaned_data_BFP_FireIncidents2012-2016.csv`.

4. **Visualize the Data**:
   - Open `Visualization.ipynb` in Jupyter Notebook.
   - Ensure the notebook reads the cleaned data from the `data/` directory:
     ```python
     cleaned_data_path = 'data/cleaned_data_BFP_FireIncidents2012-2016.csv'
     ```
   - Execute the notebook to create visualizations from the cleaned dataset.

5. **Run the Dashboard**:
   - To launch the Streamlit dashboard, run the following command:
     ```bash
     streamlit run Dashboard.py
     ```
   - Ensure `Dashboard.py` references the correct file paths for the dataset:
     ```python
     import pandas as pd
     # Locate your dataset and change the values of raw_data_path variable if needed.
     raw_data_path = 'data/BFP_FireIncidents2012-2016.csv'
     cleaned_data_path = 'data/cleaned_data_BFP_FireIncidents2012-2016.csv'
     
     df = pd.read_csv(cleaned_data_path)
     ```
   - This will start a local server and open the dashboard in your web browser for interactive exploration of the fire incidents data.
