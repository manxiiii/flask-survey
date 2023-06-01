from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key

# Configure Flask Debug Toolbar
app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

# Your Flask routes and other application code...

if __name__ == '__main__':
    app.run()
