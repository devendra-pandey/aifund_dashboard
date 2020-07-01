from application import app
from db import db
from security import login_manager
import appurls



@app.before_first_request
def createTable():
    db.create_all()
    db.session.commit()


def init():
    db.init_app(app)
    login_manager.init_app(app)
    import dashapps


if __name__ == '__main__':
    init()
    app.run(debug=True)
