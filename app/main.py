from config.constants import PATH_SWAGGER_DOCS
from config.database import dummy_data, init_db
from config.environment import DEBUG_MODE
from flasgger import Swagger
from flask import Flask
from routers import institution_bp, project_bp, user_bp

app = Flask(__name__)

swagger = Swagger(app, template_file=f"{PATH_SWAGGER_DOCS}/template.yml")

with app.app_context():
    init_db()

app.register_blueprint(institution_bp)
app.register_blueprint(user_bp)
app.register_blueprint(project_bp)


@app.route("/dummy")
def test():
    dummy_data()
    return {"message": "Dummy data created successfully"}


app.run(host="0.0.0.0", debug=DEBUG_MODE)
