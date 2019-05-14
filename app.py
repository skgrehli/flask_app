import os
from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, app!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# Entry point for the application.
# from . import app    # For application discovery by the 'flask' command.
# from . import views  # For import side-effects of setting up routes.