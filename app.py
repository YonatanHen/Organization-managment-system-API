from flask import Flask

from routes.user import user_bp
from routes.endpoint import ep_bp
from routes.organization import org_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(ep_bp)
app.register_blueprint(org_bp)

if __name__ == '__main__':
    app.run() #debug=True


