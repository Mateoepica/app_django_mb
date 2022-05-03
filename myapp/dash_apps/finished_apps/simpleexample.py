# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd
# from django_plotly_dash import DjangoDash
# from dash.dependencies import Input,Output
# app = DjangoDash(__name__) 

# df = pd.read_csv('C:/Users/matfa/proyectos_django/django_forms2/myapp/dash_apps/finished_apps/new_sales_2019_2021.csv')


# app.layout = html.Div([

#     html.Div([

#         html.H1("Predictions Meatn'bone" ),
#         html.Img(src= 'assets/meat.png')        
#     ], className='banner'),

#     html.Div([
#         html.Div([
#             html.P('Selecciona el mes', className='fix_label', style={'color':'black','margin-top':'2px'}),
#             dcc.RadioItems(id = 'meses-radioitems',
#                             labelStyle= {'display':'inline-block'},
#                             options= [
#                                 {'label':'Enero','value':'primera_dosis_cantidad'},# aca en el valor ponemos el titulo al que queremos hacer referencia
#                                  {'label':'Febrero','value' : 'segunda_dosis_cantidad'}
#                             ], value= 'primera_dosis_cantidad',
#                             style={'text-aling':'center','color': 'black' }, className='dcc_compon'),

#         ],className= 'create_container2 five colums',style={'margin-bottom':'20px'}),
#     ],className='row flex-display'),

#     html.Div([
#         html.Div([ 
#             dcc.Graph(id= 'my_graph', figure={})
#         ], className= 'create_container2 five columns'),

#         html.Div([
#             dcc.Graph(id='pie_graph',figure={})
#         ], className= 'create_container2 five columns')
#     ], className= 'create_container2 five columns'),

# ], id= 'mainContainer',style={'display':'flex','flex-direction':'colum'}) 


# @app.callback(
#     Output('my_graph',component_property='figure'),
#     [Input('dosis-radioitems',component_property= 'value')])

# def update_graph(value):
#     if value == 'primera_dosis_cantidad':
#         fig = px.bar(
#             data_frame=df,
#             x = 'jurisdiccion_nombre',
#             y = 'primera_dosis_cantidad'
#         )
#     else:
#         fig = px.bar(
#             data_frame= df,
#             x = 'jurisdiccion_nombre',
#             y = 'segunda_dosis_cantidad'
#         )
#     return fig

# @app.callback(
#     Output('pie_graph',component_property='figure'),
#      [Input('dosis-radioitems',component_property='value')])

# def update_graph_pie(value):
#     if value == 'primer_dosis_cantidad':
#         fig2 




import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
from django_plotly_dash import DjangoDash
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:/Users/matfa/proyectos_django/django_forms2/myapp/dash_apps/finished_apps/out_and_sales.csv")
data["ds"] = pd.to_datetime(data["ds"], format="%Y-%m-%d")
data.sort_values("ds",inplace=True)


x = data.ds
Xs = [x_point for x_point in range(len(x))]
y = data.yhat
y_scatter = data.total_sales
y_upper =  data.yhat_upper
y_lower =  data.yhat_lower

app= DjangoDash('MiEjemploSimple')

external_stylesheets = ['style.css']
app = DjangoDash('MiEjemploSimple', external_stylesheets=external_stylesheets)
app.title = "Meat N' Bone Analysis"


fig = go.Figure([
    go.Scatter(
        x=x,
        y=y,
        line=dict(color='rgb(255, 0, 0)'),
        mode='lines'
    ),
    go.Scatter(
        x=x,
        y=y_scatter,
        line=dict(color='rgb(0,0,200)'),
        mode='markers',
        marker=dict(size=3)
    ),
    go.Scatter(
        name='Upper Bound',
        x=x,
        y=y_upper,
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    ),
    go.Scatter(
        name='Lower Bound',
        x=x,
        y=y_lower,
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
])


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src='assets/bones.png', className="header-emoji"),
                html.H1(
                    children="Meat N' Bone Predictive Analytics", className="header-title"
                ),
                html.P(
                    children="Predictive analytics"
                    " of future sales in "
                    " Meat N' Bone in the US",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.ds.min().date(),
                            max_date_allowed=data.ds.max().date(),
                            start_date=data.ds.min().date(),
                            end_date=data.ds.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        figure=fig,
                        id="price-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)
@app.callback(
    Output("price-chart", "figure"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
    
)
def update_charts(start_date, end_date):
    mask = (
        (data.ds >= start_date)
        & (data.ds <= end_date)
    )
    filtered_data = data.loc[mask, :]
    # price_chart_figure = {
    #     "data": [
    price_chart_figure = go.Figure([
                    go.Scatter(
                        x=filtered_data["ds"],
                        y=filtered_data["total_sales"],
                        line=dict(color='rgb(0, 0, 200)'),
                        mode='markers',
                        marker=dict(size=3)
                    ),
                    go.Scatter(
                        x=filtered_data["ds"],
                        y=filtered_data["yhat"],
                        line=dict(color='rgb(255, 0, 0)'),
                        mode='lines'
                    ),
                    go.Scatter(
                        x=filtered_data["ds"],
                        y=filtered_data["yhat_lower"],
                        #line=dict(color='rgb(255, 0, 0, 0.2)'),
                        mode='lines',
                        marker=dict(color="#444"),
                        line=dict(width=0),
                        fillcolor='rgba(255,0, 0, 0.3)',
                        fill='tonexty',
                        showlegend=False
                    ),
                    go.Scatter(
                        x=filtered_data["ds"],
                        y=filtered_data["yhat_upper"],
                        #line=dict(color='rgb(255, 0, 0, 0.2)'),
                        mode='lines',
                        
                        marker=dict(color="#444"),
                        line=dict(width=0),
                        showlegend=False
                    ),
    ])
    #     ])],
    #     "layout": {
    #         "title": {
    #             "text": "Total Sales of Meat N' Bone",
    #             "x": 0.05,
    #             "xanchor": "left",
    #         },
    #         "xaxis": {"fixedrange": True},
    #         "yaxis": {"tickprefix": "$", "fixedrange": True},
    #         "colorway": ["#17B897"],
    #     },
    # }
    #for i in range(len(price_chart_figure.data)):
     #   price_chart_figure['data'][i].update_layout(transition_duration=500)
    return price_chart_figure


# import dash_core_components as dcc 
# import dash_html_components as html 
# #from dash import html
# #from dash import dcc
# from dash.dependencies import Input, Output

# import plotly.express as px 
# import pandas as pd

# from django_plotly_dash import DjangoDash

# app = DjangoDash('MiEjemploSimple')

# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
# mydf = pd.read_csv('C:/Users/matfa/proyectos_django/django_forms2/myapp/dash_apps/finished_apps/new_sales_2019_2021.csv')
# print(mydf.head())
# # df = pd.DataFrame({
# #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
# #     "Amount": [4, 1, 2, 2, 4, 5],
# #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# # })

# fig = px.scatter(mydf, x="day", y="total_sales")

# app.layout = html.Div(children=[
#     html.H1(children='Ventas de meatnbone'),

#     html.Div(children='''
#         2019-2021
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

