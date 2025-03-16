import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

# Load Data
from data_loader import df

# Calculate important metrics
avg_cac = df['CAC'].mean()
min_cac_platform = df.loc[df['CAC'].idxmin()]['platform']
min_cac_value = df['CAC'].min()
max_cac_platform = df.loc[df['CAC'].idxmax()]['platform']
max_cac_value = df['CAC'].max()

# Initialize Dash App with Bootstrap Theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, 
                                              'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'])

# Set custom graph theme to match Cyborg
graph_theme = {
    'plot_bgcolor': '#222',
    'paper_bgcolor': '#222',
    'font': {'color': '#fff'},
    'title': {'font': {'size': 24, 'color': '#00bc8c'}},
    'legend': {'font': {'color': '#fff'}},
    'xaxis': {'gridcolor': '#444', 'title': {'font': {'color': '#fff'}}},
    'yaxis': {'gridcolor': '#444', 'title': {'font': {'color': '#fff'}}},
}

# App Layout
app.layout = dbc.Container([
    # Header with animation
    html.Div([
        html.H1([
            html.I(className="fas fa-chart-line me-3"),
            "E-commerce CAC Optimization"
        ], className="text-center mt-4 mb-1 display-4 fw-bold"),
        html.H4("Marketing Performance Dashboard", 
                className="text-center mb-4 text-muted fst-italic"),
    ], className="header-section"),
    
    # Stats Cards Row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.I(className="fas fa-dollar-sign fa-2x text-info me-3"),
                        html.Div([
                            html.H4("Avg. CAC", className="m-0"),
                            html.H2(f"${avg_cac:.2f}", className="text-info m-0")
                        ])
                    ], className="d-flex align-items-center")
                ])
            ], className="mb-4 border-info")
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.I(className="fas fa-trophy fa-2x text-success me-3"),
                        html.Div([
                            html.H4("Best Platform", className="m-0"),
                            html.H2([
                                min_cac_platform, html.Span(f" (${min_cac_value:.2f})", className="fs-6 ms-2 text-muted")
                            ], className="text-success m-0")
                        ])
                    ], className="d-flex align-items-center")
                ])
            ], className="mb-4 border-success")
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.I(className="fas fa-triangle-exclamation fa-2x text-warning me-3"),
                        html.Div([
                            html.H4("Highest CAC", className="m-0"),
                            html.H2([
                                max_cac_platform, html.Span(f" (${max_cac_value:.2f})", className="fs-6 ms-2 text-muted")
                            ], className="text-warning m-0")
                        ])
                    ], className="d-flex align-items-center")
                ])
            ], className="mb-4 border-warning")
        ], width=4),
    ]),
    
    # Filter and Graph Section
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                # Filters Column
                dbc.Col([
                    html.H5([
                        html.I(className="fas fa-filter me-2"),
                        "Dashboard Controls"
                    ], className="card-title mb-3"),
                    
                    html.Label("Filter by Platform:", className="fw-bold mb-2"),
                    dcc.Dropdown(
                        id="platform-dropdown",
                        options=[{"label": platform, "value": platform} for platform in df["platform"].unique()],
                        multi=True,
                        placeholder="Select Platform(s)",
                        style={"color": "black"},
                        className="mb-3"
                    ),
                    
                    html.Label("Chart Type:", className="fw-bold mb-2"),
                    dbc.RadioItems(
                        id="chart-type",
                        options=[
                            {"label": "Bar Chart", "value": "bar"},
                            {"label": "Line Chart", "value": "line"},
                            {"label": "Scatter Plot", "value": "scatter"}
                        ],
                        value="bar",
                        inline=True,
                        className="mb-3"
                    ),
                    
                    html.Label("Show Average Line:", className="fw-bold mb-2"),
                    dbc.Switch(
                        id="show-average",
                        value=True,
                        className="mb-3"
                    ),
                    
                    html.Hr(),
                    
                    html.Div([
                        html.I(className="fas fa-info-circle me-2 text-info"),
                        "Tip: Select multiple platforms to compare their performance."
                    ], className="text-muted small")
                    
                ], width=12, lg=3, className="mb-4"),
                
                # Graph Column
                dbc.Col([
                    dcc.Graph(id="cac-graph", figure={}, config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'modeBarButtonsToRemove': ['lasso2d', 'select2d']
                    }, className="border border-secondary")
                ], width=12, lg=9),
            ])
        ])
    ]),
    
    # Insights Section
    dbc.Card([
        dbc.CardHeader([
            html.I(className="fas fa-lightbulb me-2 text-warning"),
            "Key Insights"
        ], className="fw-bold"),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H5("Cost Analysis", className="border-bottom pb-2 text-info"),
                    html.Ul([
                        html.Li(f"Average CAC across all platforms: ${avg_cac:.2f}"),
                        html.Li([
                            f"The platform with the lowest acquisition cost is ", 
                            html.Strong(f"{min_cac_platform}"),
                            f" at ${min_cac_value:.2f}"
                        ]),
                        html.Li(f"{max_cac_platform} has the highest CAC, costing ${max_cac_value-min_cac_value:.2f} more than {min_cac_platform}")
                    ])
                ], width=12, md=6),
                dbc.Col([
                    html.H5("Recommendations", className="border-bottom pb-2 text-info"),
                    html.Ul([
                        html.Li([
                            "Consider ", 
                            html.Strong("reallocating budget"),
                            f" from {max_cac_platform} to {min_cac_platform} for better ROI"
                        ]),
                        html.Li("Test new audience targeting strategies on underperforming platforms"),
                        html.Li("Review campaigns with CAC above average for optimization opportunities")
                    ])
                ], width=12, md=6)
            ])
        ])
    ], className="my-4"),
    
    # Footer
    html.Footer([
        html.Hr(),
        html.P([
            "Dashboard last updated: March 15, 2025 | ",
            html.I(className="fas fa-sync-alt me-1"),
            "Data refreshes daily"
        ], className="text-center text-muted small")
    ], className="mt-4 mb-2")
    
], fluid=True, className="px-4 py-3")

# Define callbacks
@app.callback(
    Output("cac-graph", "figure"),
    [
        Input("platform-dropdown", "value"),
        Input("chart-type", "value"),
        Input("show-average", "value")
    ]
)
def update_graph(selected_platforms, chart_type, show_average):
    # Filter data based on selection
    if not selected_platforms:
        filtered_df = df
    else:
        filtered_df = df[df["platform"].isin(selected_platforms)]
    
    # Calculate average
    avg = filtered_df['CAC'].mean()
    
    # Create appropriate chart based on selection
    if chart_type == "bar":
        fig = px.bar(
            filtered_df, 
            x="platform", 
            y="CAC", 
            color="platform", 
            title="Customer Acquisition Cost by Platform",
            labels={"CAC": "Cost per Acquisition ($)", "platform": "Marketing Platform"},
            text_auto='.2f',
            color_discrete_sequence=px.colors.qualitative.Vivid
        )
        fig.update_traces(
            texttemplate='$%{text}',
            textposition='inside',
            marker_line_width=1,
            marker_line_color="#333"
        )
    elif chart_type == "line":
        fig = px.line(
            filtered_df, 
            x="platform", 
            y="CAC", 
            markers=True,
            color_discrete_sequence=['#00bc8c'],
            title="Customer Acquisition Cost Trend",
            labels={"CAC": "Cost per Acquisition ($)", "platform": "Marketing Platform"}
        )
        fig.update_traces(
            line_width=3,
            marker_size=10
        )
    else:  # scatter
        fig = px.scatter(
            filtered_df, 
            x="platform", 
            y="CAC", 
            size="CAC",
            color="platform",
            title="Customer Acquisition Cost Distribution",
            labels={"CAC": "Cost per Acquisition ($)", "platform": "Marketing Platform"},
            size_max=30
        )
    
    # Apply common styling
    fig.update_layout(**graph_theme)
    
    # Add average line if selected
    if show_average:
        fig.add_shape(
            type="line",
            x0=-0.5,
            y0=avg,
            x1=len(filtered_df['platform'])-0.5,
            y1=avg,
            line=dict(color="#f39c12", width=2, dash="dash")
        )
        
        fig.add_annotation(
            x=len(filtered_df['platform'])-0.5,
            y=avg,
            text=f"Avg: ${avg:.2f}",
            showarrow=False,
            yshift=10,
            font=dict(color="#f39c12")
        )
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_tickangle=-45,
        legend_title_text=""
    )
    
    return fig

# Run the App
if __name__ == "__main__":
    app.run_server(debug=True)