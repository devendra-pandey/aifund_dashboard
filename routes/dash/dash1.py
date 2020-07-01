import dash
import dash_core_components as dcc
import dash_html_components as html
from application import app

dashapp1 = dash.Dash(
    __name__,
    server=app,
    url_base_pathname="/dash1/",
    external_stylesheets=[
        "//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css",
    ])

with app.app_context():
    dashapp1.layout = html.Div([
        html.Div([
            html.Div([
                html.Label("Select model1: "),
                dcc.Dropdown(id="model_id",
                             options=[
                                 {
                                     'label': 'New York City',
                                     'value': 'NYC'
                                 },
                                 {
                                     'label': 'Montreal',
                                     'value': 'MTL'
                                 },
                                 {
                                     'label': 'San Francisco',
                                     'value': 'SF'
                                 },
                             ],
                             value='MTL',
                             clearable=False)
            ],
                     className="form-group"),
            html.Div([
                html.Label("Select model version1: ", **
                           {"data-for": "modelversion_id"}),
                dcc.Dropdown(id="modelversion_id",
                             options=[
                                 {
                                     'label': 'New York City',
                                     'value': 'NYC'
                                 },
                                 {
                                     'label': 'Montreal',
                                     'value': 'MTL'
                                 },
                                 {
                                     'label': 'San Francisco',
                                     'value': 'SF'
                                 },
                             ],
                             value='MTL',
                             clearable=False)
            ],
                     className="form-group"),
            html.Div([
                html.Label("Select profile date1: ", **
                           {"data-for": "profile_id"}),
                dcc.Dropdown(id="profile_id",
                             options=[
                                 {
                                     'label': 'New York City',
                                     'value': 'NYC'
                                 },
                                 {
                                     'label': 'Montreal',
                                     'value': 'MTL'
                                 },
                                 {
                                     'label': 'San Francisco',
                                     'value': 'SF'
                                 },
                             ],
                             value='MTL',
                             clearable=False)
            ],
                     className="form-group")
        ])
    ],
                               className="container")
