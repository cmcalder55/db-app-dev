from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
#from pandas import read_csv

print('Code Started')

def init(app: Dash):

    tabs = []

    import dashboard.layouts.Shelf_1 as Shelf_1
    Shelf_1.callbacks.register(app)
    tabs.append(Shelf_1.layout.build())

    import dashboard.layouts.Shelf_2 as Shelf_2
    #Shelf_2.callbacks.register(app)
    tabs.append(Shelf_2.layout.build())

    import dashboard.layouts.Shelf_3 as Shelf_3
    #Shelf_2.callbacks.register(app)
    tabs.append(Shelf_3.layout.build())



    return html.Div(children=[
            html.Div([
                html.Label('Infineum Smart Storage Device Beta-Prototype')
            ],style={'font-size':'50px', 'height': '100px'}),

            html.Div([
                html.Div([
                    dcc.Tabs(id='shelves',
                    children=tabs,
                    style={'height':'50%'}),
                ]),

            html.Div(style={'hieght':'100px'}),

            html.Div(id='sample_info'),

                html.Div([],style={'height':'50px'}),
            ], style={'display':'text-inline', 'width':'55%'}),

            html.Div([

            ], style={'display':'text-inline','width':'45%'})
        ])