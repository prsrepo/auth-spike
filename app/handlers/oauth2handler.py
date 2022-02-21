import json
from datetime import timedelta, datetime

import requests
from requests_oauthlib.oauth2_session import OAuth2Session

from app.models import Connection
from msgraphoauth import settings


class Oauth2Handler:
    def __init__(self):
        self.AUTHORITY_URL = 'https://login.microsoftonline.com/common'
        self.AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
        self.TOKEN_ENDPOINT = '/oauth2/v2.0/token'
        self.CLIENT_ID = settings.EXCEL365_CLIENT_ID
        self.CLIENT_SECRET = settings.EXCEL365_CLIENT_SECRET
        self.SCOPES = ['User.Read', 'Files.Read.All', 'offline_access']

        self.REDIRECT_URI = 'http://localhost:8080/app/oauth2/callback'

    @property
    def session(self):
        return OAuth2Session(
            self.CLIENT_ID,
            scope=self.SCOPES,
            redirect_uri=self.REDIRECT_URI
        )

    def get_authorization_url(self, state):
        auth_base = self.AUTHORITY_URL + self.AUTH_ENDPOINT
        authorization_url, state = self.session.authorization_url(
            auth_base,
            state=state
        )
        return authorization_url

    def handle_callback(self,
                        authorization_code,
                        auth_state):
        state_dict = json.loads(auth_state)
        conn = Connection.objects.get(email=state_dict.get('email'))
        if conn.meta_data.get('state') != auth_state:
            return False
        token_res = self.session.fetch_token(
            self.AUTHORITY_URL + self.TOKEN_ENDPOINT,
            client_secret=self.CLIENT_SECRET,
            code=authorization_code
        )
        conn.meta_data['access_token'] = token_res.get('access_token')
        conn.meta_data['refresh_token'] = token_res.get('refresh_token')
        conn.meta_data['expires_in'] = token_res.get('expires_in')
        conn.meta_data['expires_at'] = (datetime.utcnow() + timedelta(seconds=token_res.get('expires_in'))).timestamp()
        conn.meta_data['is_autheticated'] = True
        conn.meta_data['state'] = None
        conn.save()
        return True

    def refresh_token(self,
                      conn):
        token_res = self.session.refresh_token(
            self.AUTHORITY_URL + self.TOKEN_ENDPOINT,
            refresh_token=conn.meta_data['refresh_token'],
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET
        )
        conn.meta_data['access_token'] = token_res.get('access_token')
        conn.meta_data['refresh_token'] = token_res.get('refresh_token')
        conn.meta_data['expires_in'] = token_res.get('expires_in')
        conn.meta_data['expires_at'] = (datetime.utcnow() + timedelta(seconds=token_res.get('expires_in'))).timestamp()
        conn.save()

    def send_request(self,
                     url,
                     method,
                     json=None):
        conn = Connection.objects.get(meta_data__contains={'is_autheticated': True})
        if not conn:
            return {
                "message": "please create a valid connection and try again"
            }
        if conn.meta_data['expires_at'] < datetime.utcnow().timestamp():
            self.refresh_token(conn)
        response = requests.get(
            url,
            method,
            json=json,
            headers={'Authorization': f'Bearer {conn.meta_data["access_token"]}'}
        )
        return response
