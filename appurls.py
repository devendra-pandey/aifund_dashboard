from routes.user import login, signup, logout
from routes.dashboard import dashboard
from routes.model import create_model
from routes.modelversion import create_mv
from routes.profile import create_profile
from routes.dropdown import dropdown
from application import app

app.add_url_rule("/", "login", login, methods=['GET', 'POST'])
app.add_url_rule("/signup", "signup", signup, methods=['GET', 'POST'])
app.add_url_rule("/logout", "logout", logout)
app.add_url_rule("/dashboard", "dashboard", dashboard)
app.add_url_rule('/createmodel',
                 "createmodel",
                 create_model,
                 methods=['GET', 'POST'])
app.add_url_rule('/createmv', "create_mv", create_mv, methods=['GET', 'POST'])
app.add_url_rule('/createprofile',
                 "create_profile",
                 create_profile,
                 methods=['GET', 'POST'])
app.add_url_rule('/dropdown/<model_id>', "dropdown", dropdown, methods=['GET'])
                