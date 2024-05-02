import os
import requests
import json

from flask import render_template, redirect, request
from ..reviewer.context import context as reviewer_context

from oauthlib.oauth2 import WebApplicationClient

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)

DATA = {
    'response_type': 'code',
    'redirect_uri': 'https://localhost:5000/reviewer', #TODO
    'scope': 'https://www.googleapis.com/auth/forms.responses.readonly',
    'client_id': GOOGLE_CLIENT_ID,
    'prompt': 'consent'
}

URL_DICT = {
    'google_oauth' : 'https://accounts.google.com/o/oauth2/v2/auth',
    'token_gen' : 'https://oauth2.googleapis.com/token',
    'get_user_info' : 'https://www.googleapis.com/oauth2/v3/userinfo'
}

# OAuth 2 client setup
CLIENT = WebApplicationClient(GOOGLE_CLIENT_ID)
REQ_URI = CLIENT.prepare_request_uri(
    uri=URL_DICT['google_oauth'],
    redirect_uri=DATA['redirect_uri'],
    scope=DATA['scope'],
    prompt=DATA['prompt']
)

def home():
    return render_template("base.html", title="Boards Reviewer Application")

def reviewer():
    if request.args.get('code') is None:
        return redirect(REQ_URI)
    else:
        code = request.args.get('code')

        token_url, headers, body = CLIENT.prepare_token_request(
            URL_DICT['token_gen'],
            authorisation_response=request.url,
            # request.base_url is same as DATA['redirect_uri']
            redirect_url=request.base_url,
            code=code)
        
        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET))
        
        CLIENT.parse_request_body_response(json.dumps(token_response.json()))

        uri, headers, body = CLIENT.add_token(URL_DICT['get_user_info'])

        return render_template("pages/reviewer.html", **reviewer_context)