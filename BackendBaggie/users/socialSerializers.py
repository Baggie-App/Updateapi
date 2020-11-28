from rest_framework import serializers
from users import google
from users.register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed
from users.models import CustomUser


class GoogleSocialAuthSerializer(serializers.Serializer):
    """
    Handle serialization and deserialization of User objects
    """

    access_token = serializers.CharField()

    def validate(self, data):
        """
        Handles validating a request and decoding and getting user's info
        associated to an account on Google then authenticates the User
        : params access_token:
        : return: user_token
        """
        #print(data.get('access_token'))
        id_info = google.SocialValidation.google_auth_validation(
            access_token=data.get('access_token'))
        print(id_info)
        # check if data data retrieved once token decoded is empty
        if not id_info:
            raise serializers.ValidationError('token is not valid')

        # check if a user exists after decoding the token in the payload
        # the user_id confirms user existence since its a unique identifier

        user_id = id_info['sub']

        # query database to check if a user with the same email exists
        user = CustomUser.objects.filter(email=id_info.get('email'))

        # if the user exists,return the user token
        if user:
            return {
                'user_exists': True,
                'message': 'Welcome back ' + str(id_info.get('name'))
            }

        if id_info.get('picture'):
            id_info['user_profile_picture'] = id_info['picture']

        user_id = id_info['sub']
        email = id_info['email']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id, email=email)



# class GoogleSocialAuthSerializer(serializers.Serializer):
#     auth_token = serializers.CharField()
#
#     def validate_auth_token(self, auth_token):
#         user_data = google.Google.validate(auth_token)
#         print(user_data)
#         try:
#             user_data['sub']
#         except:
#             raise serializers.ValidationError(
#                 'The token is invalid or expired. Please login again.'
#             )
#
#         if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
#
#             raise AuthenticationFailed('oops, who are you?')
#
#         user_id = user_data['sub']
#         email = user_data['email']
#         name = user_data['name']
#         provider = 'google'
#
#         return register_social_user(
#             provider=provider, user_id=user_id, email=email, name=name)
