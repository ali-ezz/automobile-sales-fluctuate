# Automobile Sales Fluctuation Analysis

This project analyzes the impact of recession on automobile sales for XYZAutomotives using historical data. The analysis includes comprehensive visualizations and an interactive dashboard to help directors understand sales trends during recession and non-recession periods.

## Project Overview

The project is divided into two main parts:

### Part 1: Data Visualizations (Jupyter Notebook)
- **File**: `automobile_analysis.ipynb`
- Creates 9 different visualizations using Matplotlib, Seaborn, and Pandas
- Analyzes automobile sales trends, recession impacts, and various economic factors

### Part 2: Interactive Dashboard (Dash Application)
- **File**: `dashboard.py`
- Interactive web dashboard using Plotly and Dash
- Allows directors to explore data by year and view recession vs yearly statistics

## Dataset Description

The `data/historical_automobile_sales.csv` contains the following columns:

- **Date**: The date of the observation
- **Year**: Year extracted from date
- **Month**: Month extracted from date
- **Recession**: Binary indicator (1 = recession, 0 = normal)
- **Automobile_Sales**: Number of vehicles sold
- **GDP**: Per capita GDP value in USD
- **unemployment_rate**: Monthly unemployment rate
- **Consumer_Confidence**: Consumer confidence index
- **Seasonality_Weight**: Seasonality effect weight
- **Price**: Average vehicle price
- **Advertising_Expenditure**: Company advertising spending
- **Vehicle_Type**: Type of vehicle (Supperminicar, Smallfamiliycar, Mediumfamilycar, Executivecar, Sports)
- **Competition**: Market competition measure
- **Growth_Rate**: GDP growth rate
- **City**: City where sales occurred

## Recession Periods Analyzed

1. **Period 1**: 1980
2. **Period 2**: 1981-1982
3. **Period 3**: 1991
4. **Period 4**: 2000-2001
5. **Period 5**: End of 2007 to mid-2009
6. **Period 6**: 2020 Feb-April (COVID-19 Impact)

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook or JupyterLab

### Installation

1. **Clone or download the project files**

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify the data file exists**:
   - Ensure `data/historical_automobile_sales.csv` is present
   - The file contains the historical automobile sales data

## Usage

### Running the Jupyter Notebook Analysis

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open the analysis notebook**:
   - Navigate to `automobile_analysis.ipynb`
   - Run all cells to generate visualizations

3. **Generated Images**:
   All plots are automatically saved to the `images/` directory:
   - `Line_plot_1.png` - Yearly sales fluctuation
   - `Line_plot_2.png` - Vehicle type trends during recession
   - `Bar_Chart.png` - Recession vs non-recession comparison
   - `Subplot.png` - GDP variations
   - `Bubble.png` - Seasonality impact
   - `Scatter.png` - Price vs sales correlation
   - `Pie_1.png` - Advertising expenditure by period
   - `Pie_2.png` - Advertising expenditure by vehicle type
   - `Line_plot_3.png` - Unemployment rate effects

### Running the Interactive Dashboard

1. **Start the dashboard**:
   ```bash
   python dashboard.py
   ```

2. **Access the dashboard**:
   - Open your web browser
   - Navigate to `http://127.0.0.1:8050`

3. **Dashboard Features**:
   - **Dropdown 1**: Select between "Yearly Statistics" and "Recession Period Statistics"
   - **Dropdown 2**: Select specific year for yearly analysis
   - **Interactive Charts**: Four different visualizations update based on selections

## Task Completion Status

### Part 1: Jupyter Notebook Visualizations ✅
- [x] Task 1.1: Line chart - yearly sales fluctuation
- [x] Task 1.2: Multi-line chart - vehicle type trends during recession
- [x] Task 1.3: Seaborn bar chart - recession vs non-recession comparison
- [x] Task 1.4: Subplot - GDP variations
- [x] Task 1.5: Bubble plot - seasonality impact
- [x] Task 1.6: Scatter plot - price vs sales correlation
- [x] Task 1.7: Pie chart - advertising expenditure by period
- [x] Task 1.8: Pie chart - advertising expenditure by vehicle type
- [x] Task 1.9: Line plot - unemployment rate effects

### Part 2: Interactive Dashboard ✅
- [x] Task 2.1: Dash application with meaningful title
- [x] Task 2.2: Dropdown menus with appropriate options
- [x] Task 2.3: Output display division with proper styling
- [x] Task 2.4: Callback functions for interactivity
- [x] Task 2.5: Recession report statistics graphs
- [x] Task 2.6: Yearly report statistics graphs

## Key Insights

The analysis reveals:

1. **Recession Impact**: Clear differences in sales patterns during recession vs normal periods
2. **Vehicle Type Variations**: Different vehicle types show varying resilience during recessions
3. **Seasonal Effects**: Monthly patterns in automobile sales
4. **Economic Correlations**: Relationships between GDP, unemployment, and sales
5. **Price Sensitivity**: How vehicle pricing affects sales during economic downturns

## File Structure

```
automobile-sales-fluctuate/
├── data/
│   └── historical_automobile_sales.csv
├── images/
│   ├── Line_plot_1.png
│   ├── Line_plot_2.png
│   ├── Bar_Chart.png
│   ├── Subplot.png
│   ├── Bubble.png
│   ├── Scatter.png
│   ├── Pie_1.png
│   ├── Pie_2.png
│   └── Line_plot_3.png
├── automobile_analysis.ipynb
├── dashboard.py
├── requirements.txt
└── README.md
```

## Troubleshooting

### Common Issues:

1. **Missing packages**: Run `pip install -r requirements.txt`
2. **Jupyter not starting**: Try `jupyter lab` instead of `jupyter notebook`
3. **Dashboard not loading**: Check if port 8050 is available
4. **Image files not saving**: Ensure `images/` directory exists

### Support

For technical issues or questions about the analysis, refer to the code comments in the notebook and dashboard files.

## Assignment Submission

This project fulfills all requirements for the automobile sales analysis assignment:
- Comprehensive data visualizations
- Interactive dashboard with user controls
- Proper file naming and organization
- Complete documentation and code comments
