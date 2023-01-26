from flask import Flask
from flasgger import Swagger

from config.database import init_db, dummy_data
from config.environment import DEBUG_MODE
from routers import institution_bp, user_bp, project_bp

app = Flask(__name__)
swagger = Swagger(app)

with app.app_context():
    init_db()

app.register_blueprint(institution_bp)
app.register_blueprint(user_bp)
app.register_blueprint(project_bp)


@app.route('/dummy')
def test():
    dummy_data()
    return {'message': 'Dummy data created successfully'}


app.run(debug=DEBUG_MODE)
