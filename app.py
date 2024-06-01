from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from controller.transit_controller import transit_schedule_bp
import os

app = Flask(__name__)

# Register blueprints
app.register_blueprint(transit_schedule_bp, url_prefix='/transit')

# Swagger UI configuration
SWAGGER_URL = '/api/docs'
API_URL = '/swagger/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Transit API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Serve the Swagger YAML file
@app.route('/swagger/<path:filename>')
def swagger(filename):
    return send_from_directory(os.path.join(app.root_path, 'swagger'), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
