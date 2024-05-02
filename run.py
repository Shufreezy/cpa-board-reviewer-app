import json
import os
import secrets

from flask_bootstrap import Bootstrap5
from flask import Flask, url_for
from apps.services import routes
from OpenSSL import SSL

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'vapor'
app.secret_key = secrets.token_hex(16)

# routes
app.add_url_rule('/', view_func=routes.home)
app.add_url_rule('/reviewer', view_func=routes.reviewer)

if __name__ == "__main__":
    app.run(debug=True, port=5000, ssl_context='adhoc')