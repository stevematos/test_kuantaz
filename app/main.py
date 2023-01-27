from flask import Flask
from flasgger import Swagger

from config.constants import PATH_SWAGGER_DOCS
from config.database import init_db, dummy_data
from config.environment import DEBUG_MODE
from routers import institution_bp, user_bp, project_bp

app = Flask(__name__)

swagger = Swagger(app, template_file=f"{PATH_SWAGGER_DOCS}/template.yml")

with app.app_context():
    init_db()

app.register_blueprint(institution_bp)
app.register_blueprint(user_bp)
app.register_blueprint(project_bp)


@app.route('/dummy')
def test():
    dummy_data()
    return {'message': 'Dummy data created successfully'}


app.run(host='0.0.0.0', debug=DEBUG_MODE)
