import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the actual automobile sales data
df = pd.read_csv('data/historical_automobile_sales.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create Period column for easier filtering
df['Period'] = df['Recession'].map({1: 'Recession', 0: 'Non-Recession'})

# App layout
app.layout = html.Div([
    # Task 2.1: Title
    html.H1("Automobile Sales Dashboard - XYZ Automotive", 
            style={'textAlign': 'center', 
                   'color': '#2E86AB',
                   'marginBottom': '30px',
                   'fontFamily': 'Arial, sans-serif'}),
    
    html.Hr(),
    
    # Task 2.2: Dropdown menus
    html.Div([
        html.Label("Select Statistics:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            value='Yearly Statistics',
            placeholder="Select a report type",
            style={'marginBottom': '20px'}
        ),
        
        html.Label("Select Year:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': str(year), 'value': year} for year in sorted(df['Year'].unique())],
            value=2020,
            placeholder="Select-year",
            style={'marginBottom': '20px'}
        )
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '20px'}),
    
    # Task 2.3: Output display division
    html.Div(id='output-container', 
             className='chart-grid',
             style={'padding': '20px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '10px',
                    'margin': '20px'}),
    
    html.Hr(),
    
    html.Div([
        html.P("Dashboard created for automobile sales analysis assignment",
               style={'textAlign': 'center', 'color': '#666'})
    ])
])

# Task 2.4: Callback functions
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Task 2.5: Recession Report Statistics
        return create_recession_report_graphs()
    elif selected_statistics == 'Yearly Statistics':
        # Task 2.6: Yearly Report Statistics  
        return create_yearly_report_graphs(input_year)
    else:
        return html.Div("Please select a statistics type.")

def create_recession_report_graphs():
    """Create graphs for recession period statistics using actual data"""
    
    # Filter recession data
    recession_df = df[df['Recession'] == 1]
    
    # Graph 1: Average automobile sales by vehicle type during recession
    vehicle_sales = recession_df.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
    fig1 = px.bar(vehicle_sales, x='Vehicle_Type', y='Automobile_Sales',
                  title='Average Automobile Sales by Vehicle Type During Recession',
                  color='Vehicle_Type',
                  labels={'Automobile_Sales': 'Average Sales'})
    fig1.update_xaxes(tickangle=45)
    
    # Graph 2: Average monthly vehicle sales during recession
    monthly_sales = recession_df.groupby('Month')['Automobile_Sales'].mean().reset_index()
    # Define month order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_sales['Month'] = pd.Categorical(monthly_sales['Month'], categories=month_order, ordered=True)
    monthly_sales = monthly_sales.sort_values('Month')
    
    fig2 = px.line(monthly_sales, x='Month', y='Automobile_Sales',
                   title='Average Monthly Vehicle Sales During Recession',
                   markers=True)
    
    # Graph 3: GDP variation during recession years
    gdp_recession = recession_df.groupby('Year')['GDP'].mean().reset_index()
    fig3 = px.scatter(gdp_recession, x='Year', y='GDP',
                      title='GDP Variation During Recession Years',
                      size_max=15)
    fig3.update_traces(marker_size=10)
    
    # Graph 4: Unemployment rate during recession
    unemployment_recession = recession_df.groupby('Year')['unemployment_rate'].mean().reset_index()
    fig4 = px.area(unemployment_recession, x='Year', y='unemployment_rate',
                   title='Unemployment Rate During Recession Periods',
                   labels={'unemployment_rate': 'Unemployment Rate (%)'})
    
    return html.Div([
        html.H2("Recession Period Statistics", 
                style={'textAlign': 'center', 'color': '#d9534f'}),
        
        html.Div([
            html.Div([dcc.Graph(figure=fig1)], className='six columns'),
            html.Div([dcc.Graph(figure=fig2)], className='six columns'),
        ], className='row'),
        
        html.Div([
            html.Div([dcc.Graph(figure=fig3)], className='six columns'),
            html.Div([dcc.Graph(figure=fig4)], className='six columns'),
        ], className='row')
    ])

def create_yearly_report_graphs(year):
    """Create graphs for yearly statistics using actual data"""
    
    # Filter data for selected year
    year_df = df[df['Year'] == year]
    
    if year_df.empty:
        return html.Div([
            html.H2(f"No data available for year {year}", 
                    style={'textAlign': 'center', 'color': '#d9534f'})
        ])
    
    # Graph 1: Monthly sales trend for selected year
    monthly_trend = year_df.groupby('Month')['Automobile_Sales'].sum().reset_index()
    # Define month order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_trend['Month'] = pd.Categorical(monthly_trend['Month'], categories=month_order, ordered=True)
    monthly_trend = monthly_trend.sort_values('Month')
    
    fig1 = px.line(monthly_trend, x='Month', y='Automobile_Sales',
                   title=f'Monthly Sales Trend for {year}',
                   markers=True)
    fig1.update_traces(line_color='#2E86AB', line_width=3)
    
    # Graph 2: Vehicle type distribution for selected year
    vehicle_distribution = year_df.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()
    fig2 = px.pie(vehicle_distribution, values='Automobile_Sales', names='Vehicle_Type',
                  title=f'Vehicle Type Sales Distribution - {year}')
    
    # Graph 3: Quarterly advertising expenditure
    # Create quarters based on months
    quarter_map = {'Jan': 'Q1', 'Feb': 'Q1', 'Mar': 'Q1',
                   'Apr': 'Q2', 'May': 'Q2', 'Jun': 'Q2',
                   'Jul': 'Q3', 'Aug': 'Q3', 'Sep': 'Q3',
                   'Oct': 'Q4', 'Nov': 'Q4', 'Dec': 'Q4'}
    year_df_copy = year_df.copy()
    year_df_copy['Quarter'] = year_df_copy['Month'].map(quarter_map)
    quarterly_ad = year_df_copy.groupby('Quarter')['Advertising_Expenditure'].sum().reset_index()
    # Ensure quarter order
    quarter_order = ['Q1', 'Q2', 'Q3', 'Q4']
    quarterly_ad['Quarter'] = pd.Categorical(quarterly_ad['Quarter'], categories=quarter_order, ordered=True)
    quarterly_ad = quarterly_ad.sort_values('Quarter')
    
    fig3 = px.bar(quarterly_ad, x='Quarter', y='Advertising_Expenditure',
                  title=f'Quarterly Advertising Expenditure - {year}',
                  labels={'Advertising_Expenditure': 'Expenditure ($)'})
    fig3.update_traces(marker_color='#A23B72')
    
    # Graph 4: Consumer confidence vs sales correlation
    monthly_metrics = year_df.groupby('Month').agg({
        'Automobile_Sales': 'sum',
        'Consumer_Confidence': 'mean'
    }).reset_index()
    monthly_metrics['Month'] = pd.Categorical(monthly_metrics['Month'], categories=month_order, ordered=True)
    monthly_metrics = monthly_metrics.sort_values('Month')
    
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=monthly_metrics['Month'], y=monthly_metrics['Automobile_Sales'], 
                             mode='lines+markers', name='Sales',
                             yaxis='y', line=dict(color='#2E86AB')))
    fig4.add_trace(go.Scatter(x=monthly_metrics['Month'], y=monthly_metrics['Consumer_Confidence'],
                             mode='lines+markers', name='Consumer Confidence',
                             yaxis='y2', line=dict(color='#F18F01')))
    
    fig4.update_layout(
        title=f'Sales vs Consumer Confidence - {year}',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Sales Volume', side='left'),
        yaxis2=dict(title='Consumer Confidence', side='right', overlaying='y'),
        legend=dict(x=0.7, y=1)
    )
    
    return html.Div([
        html.H2(f"Yearly Statistics - {year}", 
                style={'textAlign': 'center', 'color': '#2E86AB'}),
        
        html.Div([
            html.Div([dcc.Graph(figure=fig1)], className='six columns'),
            html.Div([dcc.Graph(figure=fig2)], className='six columns'),
        ], className='row'),
        
        html.Div([
            html.Div([dcc.Graph(figure=fig3)], className='six columns'),
            html.Div([dcc.Graph(figure=fig4)], className='six columns'),
        ], className='row')
    ])

# Custom CSS styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .row {
                display: flex;
                flex-wrap: wrap;
                margin: 10px 0;
            }
            .six.columns {
                width: 48%;
                margin: 1%;
            }
            .chart-grid {
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
