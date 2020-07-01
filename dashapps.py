from routes.dash.dash import dashapp
from routes.dash.dash1 import dashapp1
from flask_login import login_required


def _protect_dash_app(app):
    for view_func in app.server.view_functions:
        if view_func.startswith(app.config.url_base_pathname):
            app.server.view_functions[view_func] = login_required(
                app.server.view_functions[view_func])


_protect_dash_app(dashapp)
_protect_dash_app(dashapp1)