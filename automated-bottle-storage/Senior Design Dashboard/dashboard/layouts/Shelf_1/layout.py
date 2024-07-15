import dash_core_components as dcc
import dash_html_components as html
from dashboard.layouts.Shelf_1.callbacks import Shelf_Colors

def build():
    return dcc.Tab(label='Shelf 1', children=[
            html.Div([
                html.Div([
                    html.Label('Shelf 1'),
                ], style={'height': '40px','width':'100px', 'font-size':'30px'}),
                html.Div([
                    html.Div([
                        html.Button(id='Slot_1', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color': Shelf_Colors['Slot_1_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_2', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_2_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_3', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_3_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_4', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_4_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_5', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_5_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_6', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_6_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_7', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_7_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_8', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_8_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_9', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_9_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                ], style={'height':'70px'}),


                html.Div([
                    html.Div([
                        html.Button(id='Slot_10', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_10_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_11', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_11_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_12', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_12_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_13', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_13_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_14', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_14_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_15', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_15_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_16', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_16_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_17', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_17_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_18', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_18_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                ], style={'height':'70px'}),


                html.Div([
                    html.Div([
                        html.Button(id='Slot_19', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_19_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_20', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_20_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_21', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_21_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_22', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_22_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_23', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_23_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_24', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_24_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_25', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_25_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_26', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_26_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_27', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_27_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                ], style={'height':'70px'}),


                html.Div([
                    html.Div([
                        html.Button(id='Slot_28', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_28_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_29', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_29_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_30', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_30_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_31', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_31_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_32', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_32_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_33', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_33_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_34', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_34_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_35', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_35_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_36', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_36_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                ], style={'height':'70px'}),


                html.Div([
                    html.Div([
                        html.Button(id='Slot_37', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_37_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_38', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_38_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_39', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_39_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_40', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_40_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_41', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_41_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                        html.Button(id='Slot_42', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_42_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_43', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_43_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_44', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_44_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                    html.Div([
                    html.Button(id='Slot_45', n_clicks=0, style={'border-radius':'50%', 'height':'50px', 'width':'50px', 'border': '2px solid black', 'background-color':Shelf_Colors['Slot_45_Color']})
                    ], style = {'display':'inline-block', 'width':'70px'}),
                ], style={'height':'70px'}),
            ], style={})
    ])