# BFP Fire Incidents Analysis (2012-2016)

This project involves the analysis of fire incidents data from 2012 to 2016, provided by the Bureau of Fire Protection (BFP). The project includes data cleaning, analysis, and visualization of the fire incidents through a dashboard.

## Project Structure

- `BFP_FireIncidents2012-2016.csv`: The raw dataset containing fire incidents from 2012 to 2016.
- `cleaned_data_BFP_FireIncidents2012-2016.csv`: The cleaned dataset used for analysis.
- `Dashboard.py`: The Python script for creating a dashboard to visualize the fire incidents data using Streamlit.
- `Project_Data_Cleaning.ipynb`: Python script for cleaning the dataset (`BFP_FireIncidents2012-2016.csv`).
- `Visualization.ipynb`: Python script for visualizing the dataset (`BFP_FireIncidents2012-2016.csv`).

## Installation Steps

1. **Set Up Your Environment**:
   - Ensure Python is installed. Download it from [python.org](https://www.python.org/downloads/).
   - Install the required libraries:
     ```bash
     pip install pandas numpy matplotlib seaborn plotly streamlit
     ```

2. **Download the Dataset**:
   - Obtain `BFP_FireIncidents2012-2016.csv` from the Bureau of Fire Protection or other sources.

3. **Clean the Data**:
   - Open `Project_Data_Cleaning.ipynb` in Jupyter Notebook.
   - Run the notebook to clean the raw dataset and generate `cleaned_data_BFP_FireIncidents2012-2016.csv`.

4. **Visualize the Data**:
   - Open `Visualization.ipynb` in Jupyter Notebook.
   - Execute the notebook to create visualizations from the cleaned dataset.

5. **Run the Dashboard**:
   - To launch the Streamlit dashboard, run the following command:
     ```bash
     streamlit run Dashboard.py
     ```
   - This will start a local server and open the dashboard in your web browser for interactive exploration of the fire incidents data.
