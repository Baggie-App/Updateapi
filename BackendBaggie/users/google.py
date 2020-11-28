import json
import os
from google.auth.transport import requests
from google.oauth2 import id_token
from requests_oauthlib import OAuth1Session



class SocialValidation:
    """Social validation"""

    @staticmethod
    def google_auth_validation(access_token):
        """
        Provides support for verifying `OpenID Connect ID Tokens`_, especially
        ones generated by Google infrastructure.
        Verifies an ID Token issued by Google's OAuth 2.0 authorization server.

        Args:
            id_token (Union[str, bytes]): The encoded token.
            request (google.auth.transport.Request): The object used to make
                HTTP requests.
            audience (str): The audience that this token is intended for.
            This is typically your application's OAuth 2.0 client ID.
            If None then the audience is not verified.

        :param access_token:
        :return: Mapping[str, Any]: The decoded token
        """
        try:
            id_info = id_token.verify_oauth2_token(id_token=access_token,request=requests.Request())
            print(id_info)

        except ValueError:
            id_info = None
        return id_info

class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the Google oAUTH2 api to fetch the user info
        """
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request())

            if 'accounts.google.com' in idinfo['iss']:
                return idinfo

        except:
            return "The token is either invalid or has expired"
