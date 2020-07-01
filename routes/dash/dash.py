import dash
import dash_core_components as dcc
import dash_html_components as html
from application import app
import pandas as pd
from models.model import Model
from models.modelversion import Modelversion
from models.profile import Profile
from models.stock import Stock
from dash.dependencies import Input, Output
import dash_table

dashapp = dash.Dash(
    __name__,
    server=app,
    url_base_pathname="/dash/",
    external_stylesheets=[
        "//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css",
    ])


def getModelLayout(models_list_dic):
    model_layout = html.Div([
        html.Label("Select model: "),
        dcc.Dropdown(id="model_id",
                     options=models_list_dic,
                     placeholder="Select a Model",
                     value=models_list_dic[0].get("value"),
                     clearable=False)
    ],
                            className="form-group")
    return model_layout


def getModelVersionLayout():
    modelversion_layout = html.Div([
        html.Label("Select model version: ", **{"data-for":
                                                "modelversion_id"}),
        dcc.Dropdown(id="modelversion_id",
                     placeholder="Select a Model Version",
                     clearable=False)
    ])
    return modelversion_layout


def getProfileDateLayout():
    profile_date_layout = html.Div([
        html.Label("Select profile date: ", **{"data-for": "profile_id"}),
        dcc.Dropdown(id="profile_id",
                     placeholder="Select Profile Date",
                     clearable=False)
    ],
                                   className="form-group")
    return profile_date_layout


def getTableLayout(data):
    columns = [{
        "id": 'code',
        "name": "Code"
    }, {
        "id": 'name',
        "name": "Name"
    }, {
        "id": 'model_decision',
        "name": "Model Decision"
    }, {
        "id": 'exchange_token',
        "name": "Exchange_Token"
    }, {
        "id": 'instrument_token',
        "name": "Instrument_Token"
    }, {
        "id": 'stop_loss',
        "name": "Stop Loss"
    }, {
        "id": 'stop_gain',
        "name": "Stop Gain"
    }, {
        "id": 'triggered',
        "name": "Triggered"
    }, {
        "id": 'previous_close',
        "name": "Previous Close"
    }, {
        "id": 'today_open',
        "name": "Today Open"
    }, {
        "id": 'today_close',
        "name": "Today Close"
    }, {
        "id": 'delta_previous_today',
        "name": "Delta Previous Today"
    }, {
        "id": 'actual_delta',
        "name": "Actual Delta"
    }, {
        "id": 'return_generated',
        "name": "Return Generated"
    }, {
        "id": 'quantity',
        "name": "Quantity"
    }, {
        "id": 'quantity_adjusted',
        "name": "Quantity Adjusted"
    }, {
        "id": 'total_return',
        "name": "Total Return"
    }, {
        "id": 'transaction_value',
        "name": "Transaction Value"
    }, {
        "id": 'new_transaction_value',
        "name": "New Transaction Value"
    }, {
        "id": 'traditional_brokerage',
        "name": "Traditional Brokerage"
    }, {
        "id": 'zerodha_brokerage',
        "name": "Zerodha Brokerage"
    }, {
        "id": 'hybrid_brokerage',
        "name": "Hybrid Brokerage"
    }, {
        "id": 'tra_traditional_brokerage',
        "name": "TRA Traditional Brokerage"
    }, {
        "id": 'tra_zerodha_brokerage',
        "name": "TRA Zerodha Brokerage"
    }, {
        "id": 'tra_hybrid_brokerage',
        "name": "Tra Hybrid Brokerage"
    }]
    table_layout = html.Div(
        children=dash_table.DataTable(id="table",
         data=data, 
         columns=columns,
         fixed_rows={'headers': True},
        #  fixed_columns={'headers': True, 'data': 1},
         style_table={"height":400, 'minWidth': '100%', 'overflowY': 'auto'}))
    return table_layout


def buildSummaryStatisticReport(df):
    response = []

    total_return = df["tra_hybrid_brokerage"].sum(
    ) / df["new_transaction_value"].sum() * 100
    response.append(html.Div("Total Return: " + str(total_return)))

    buy_df = df[df["model_decision"] == "BUY"]
    buy_side_return = buy_df['tra_hybrid_brokerage'].sum(
    ) / buy_df['new_transaction_value'].sum() * 100
    response.append(html.Div("Buy Side Return: " + str(buy_side_return)))

    sell_df = df[df["model_decision"] == "SELL"]
    sell_side_return = sell_df['tra_hybrid_brokerage'].sum(
    ) / sell_df['new_transaction_value'].sum() * 100
    response.append(html.Div("Sell Side Return: " + str(sell_side_return)))

    triggered = df["triggered"].value_counts()
    for i in triggered.index:
        response.append(html.Div(i + ": " + str(triggered[i])))

    none_df = df[df["triggered"] == "None"]

    none_triggers_positive = len(none_df[none_df["total_return"] > 0])
    response.append(
        html.Div("None Triggers Positive: " + str(none_triggers_positive)))

    none_triggers_nagative = len(none_df[none_df["total_return"] < 0])
    response.append(
        html.Div("None Triggers Nagative: " + str(none_triggers_nagative)))

    total_return_from_none_triggers = none_df["tra_hybrid_brokerage"].sum(
    ) / none_df["new_transaction_value"].sum() * 100
    response.append(
        html.Div("Total Return From None Triggers: " +
                 str(total_return_from_none_triggers)))

    none_buy_df = none_df[none_df["model_decision"] == "BUY"]
    total_return_buy_side_none = none_buy_df["tra_hybrid_brokerage"].sum(
    ) / none_buy_df["new_transaction_value"].sum() * 100
    response.append(
        html.Div("Total Return Buy Side None: " +
                 str(total_return_buy_side_none)))

    none_sell_df = none_df[none_df["model_decision"] == "SELL"]
    total_return_sell_side_none = none_sell_df["tra_hybrid_brokerage"].sum(
    ) / none_sell_df["new_transaction_value"].sum() * 100
    response.append(
        html.Div("Total Return Sell Side None: " +
                 str(total_return_sell_side_none)))

    return html.Div(response)


with app.app_context():

    models = Model.query.all()
    models_list_dic = []

    for model in models:
        d = dict()
        d["label"] = model.name
        d["value"] = model.id
        models_list_dic.append(d)

    model_layout = getModelLayout(models_list_dic)
    modelversion_layout = getModelVersionLayout()
    profile_date_layout = getProfileDateLayout()

    dashapp.layout = html.Div([
        html.Div([
            model_layout,
            modelversion_layout,
            profile_date_layout,
        ],style={'marginLeft': 500, 'marginRight': 500,}),
        dcc.Tabs(id='tabs',
                 value='tab-1',
                 style={'width': '10%','height': '05%'},
                 children=[
                     dcc.Tab(label='Report1', value='tab-1'),
                     dcc.Tab(label='Report2', value='tab-2'),
                 ]),
        html.Div(id='tabs-content')
    ], className="container-fluid")


# model Callback
@dashapp.callback(Output('modelversion_id', 'options'),
                  [Input('model_id', 'value')])
def update_output(model_id):
    modelv_version_dic = []

    if model_id is None:
        return modelv_version_dic

    modelversion_list = Modelversion.query.filter_by(model_id=model_id).all()
    for modelversion in modelversion_list:
        a = dict()
        a["label"] = modelversion.version
        a["value"] = modelversion.id
        modelv_version_dic.append(a)

    return modelv_version_dic


# model version callback
@dashapp.callback(Output('profile_id', 'options'),
                  [Input('modelversion_id', 'value')])
def update_output1(modelversion_id):
    print("test", modelversion_id)
    profile_date_list = []
    if modelversion_id is None:
        return profile_date_list
    profiles = Profile.query.filter_by(modelversion_id=modelversion_id,
                                       is_active=True).all()

    for profile in profiles:
        a = dict()
        a["label"] = profile.report_date.strftime("%d/%m/%Y")
        a["value"] = profile.id
        profile_date_list.append(a)
    print("profile_date_list", profile_date_list)
    return profile_date_list


# profile date callback
@dashapp.callback(Output('tabs-content', 'children'),
                  [Input('profile_id', 'value'),
                   Input("tabs", "value")])
def update_stock(profile_id, tab):
    stock_list = []
    if profile_id is None:
        return stock_list

    query = Stock.query.filter_by(profile_id=profile_id, is_active=True)
    df_stock = pd.read_sql(query.statement, query.session.bind)

    if tab == "tab-1":
        data = df_stock.to_dict("records")
        table_layout = getTableLayout(data)
        return table_layout
    elif tab == "tab-2":
        summary_report = buildSummaryStatisticReport(df_stock)
        return summary_report
