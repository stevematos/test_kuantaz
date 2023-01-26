from flask import Flask, jsonify
from flasgger import Swagger

from config.database import init_db
from config.environment import DATABASE_DIALECT, DEBUG_MODE
from routers import institution_bp

app = Flask(__name__)
swagger = Swagger(app)

with app.app_context():
    init_db()

app.register_blueprint(institution_bp)


@app.route('/test')
def test():
    return jsonify({'dialect': DATABASE_DIALECT})


app.run(debug=DEBUG_MODE)