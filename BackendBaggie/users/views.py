from django.contrib.auth import get_user_model
from rest_framework import viewsets # new
from users.models import CustomUser,PhoneOTP
from users.serializers import (
    RegisterVendonSerializer,
    RegisteCustomerSerializer,
    LoginwithPhoneCustomerSerializer,
    LoginVendorSerializer,
    EmailVerificationSerializer,
    SetNewPasswordSerializer,
    LogoutSerializer,
    ResetPasswordEmailRequestSerializer,
    CustomVendorSerilizer,
    )
from users.utils import Util
from users.renderers import UserRenderer,UserJSONRenderer
from headers import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import os
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
from django.http import HttpResponse
import http.client
conn = http.client.HTTPConnection("")


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


########## RegisterView ##########################
class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterVendonSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user)
        user_data ={
        "response":user_data,
        "refresh":str(token),
        "access": str(token.access_token),
        }
        # current_site = '127.0.0.1:8000'
        # #current_site = get_current_site(request).domain
        # relativeLink = reverse('email-verify')
        # absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        # email_body = 'Hi '+user.username + \
        #     ' Use the link below to verify your email \n' + absurl
        # data = {'email_body': email_body, 'to_email': user.email,
        #        'email_subject': 'Verify your email'}

        #Util.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)
class RegisterCustomerView(generics.GenericAPIView):

    serializer_class = RegisteCustomerSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user)
        user_data ={
        "response":user_data,
        "refresh":str(token),
        "access": str(token.access_token),
        }
        # current_site = '127.0.0.1:8000'
        # #current_site = get_current_site(request).domain
        # relativeLink = reverse('email-verify')
        # absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        # email_body = 'Hi '+user.username + \
        #     ' Use the link below to verify your email \n' + absurl
        # data = {'email_body': email_body, 'to_email': user.email,
        #        'email_subject': 'Verify your email'}

        #Util.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)

############## Veryfy Email View ##############################
class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            print(payload['user_id'])
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# ################# Loginin with phone ###################
class LoginPhoneAPIView(generics.GenericAPIView):
    serializer_class = LoginwithPhoneCustomerSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
#
################# Login with email and passwod #############
class LoginemailAPIView(generics.GenericAPIView):
    serializer_class = LoginVendorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#reset password
class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data['email']

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            user_data = serializer
            user_data ={
                  "uidb64":str(uidb64),
                  "token": str(token),
            }

        return Response(user_data, status=status.HTTP_200_OK)
            # current_site = "127.0.0.1:8000"
            # #current_site = get_current_site(
            # #    request=request).domain
            # relativeLink = reverse(
            #     'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            #
            # redirect_url = request.data.get('redirect_url', '')
            # absurl = 'http://'+current_site + relativeLink
            # email_body = 'Hello, \n Use link below to reset your password  \n' + \
            #     absurl+"?redirect_url="+redirect_url
            # data = {'email_body': email_body, 'to_email': user.email,
            #         'email_subject': 'Reset your passsword'}
            # Util.send_email(data)
        #return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


#using temporary
class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error':'Token is not valid, please request a new one'})
            return Response({'success':True, 'message':'Credentials Valid', 'uidb64':uidb64, 'token':token})
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error':'Token is not valid, please Try a new one'})

class AccountlistView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomVendorSerilizer
    filter_backends = (filters.DjangoFilterBackend,SearchFilter, OrderingFilter)
    filterset_fields = ('role',)
    search_fields = ('role',)


# class PasswordTokenCheckAPI(generics.GenericAPIView):
#     serializer_class = SetNewPasswordSerializer
#
#     def get(self, request, uidb64, token):
#
#         redirect_url = request.GET.get('redirect_url')
#
#         try:
#             id = smart_str(urlsafe_base64_decode(uidb64))
#             user = CustomUser.objects.get(id=id)
#
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 if len(redirect_url) > 3:
#                     return CustomRedirect(redirect_url+'?token_valid=False')
#                 else:
#                     return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')
#
#             if redirect_url and len(redirect_url) > 3:
#                 return CustomRedirect(redirect_url+'?token_valid=True&?message=Credentials Valid&?uidb64='+uidb64+'&?token='+token)
#             else:
#                 return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')
#
#         except DjangoUnicodeDecodeError as identifier:
#             if not PasswordResetTokenGenerator().check_token(user):
#                 return CustomRedirect(redirect_url+'?token_valid=False')


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

#logout from app
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)




class ValidatePhoneSendOTP(APIView):

    def post(self, request, *args, **kwargs):
        mobileNumber = request.data.get('mobileNumber')
        password = request.data.get('password', False)
        email    = request.data.get('email', False)

        if phone_number:
            phone = str(mobileNumber)
            user = CustomUser.objects.filter(phone__iexact = phone)
            if user.exists():
                return Response({
                    'status' : False,
                    'detail' : 'Phone number already exists'
                })

            else:
                key = send_otp(phone)
                if key:
                    old = PhoneOTP.objects.filter(phone__iexact = phone)
                    if old.exists():
                        old = old.first()
                        count = old.count
                        if count > 10:
                            return Response({
                                'status' : False,
                                'detail' : 'Sending otp error. Limit Exceeded. Please Contact Customer support'
                            })

                        old.count = count +1
                        old.save()
                        print('Count Increase', count)

                        conn.request("GET", "https://2factor.in/API/R1/?module=SMS_OTP&apikey=1028fcd9-3158-11ea-9fa5-0200cd936042&to="+phone+"&otpvalue="+str(key)+"&templatename=WomenMark1")
                        res = conn.getresponse()

                        data = res.read()
                        data=data.decode("utf-8")
                        data=ast.literal_eval(data)


                        if data["Status"] == 'Success':
                            old.otp_session_id = data["Details"]
                            old.save()
                            print('In validate phone :'+old.otp_session_id)
                            return Response({
                                   'status' : True,
                                   'detail' : 'OTP sent successfully'
                                })
                        else:
                            return Response({
                                  'status' : False,
                                  'detail' : 'OTP sending Failed'
                                })




                    else:

                        obj=PhoneOTP.objects.create(
                            phone=phone,
                            otp = key,
                            email=email,
                            password=password,
                        )
                        conn.request("GET", "https://2factor.in/API/R1/?module=SMS_OTP&apikey=1028fcd9-3158-11ea-9fa5-0200cd936042&to="+phone+"&otpvalue="+str(key)+"&templatename=WomenMark1")
                        res = conn.getresponse()
                        data = res.read()
                        print(data.decode("utf-8"))
                        data=data.decode("utf-8")
                        data=ast.literal_eval(data)

                        if data["Status"] == 'Success':
                            obj.otp_session_id = data["Details"]
                            obj.save()
                            print('In validate phone :'+obj.otp_session_id)
                            return Response({
                                   'status' : True,
                                   'detail' : 'OTP sent successfully'
                                })
                        else:
                            return Response({
                                  'status' : False,
                                  'detail' : 'OTP sending Failed'
                                })


                else:
                     return Response({
                           'status' : False,
                            'detail' : 'Sending otp error'
                     })

        else:
            return Response({
                'status' : False,
                'detail' : 'Phone number is not given in post request'
            })



def send_otp(phone):
    if phone:
        key = random.randint(99999,999999)
        print(key)
        return key
    else:
        return False

class ValidateOTP(APIView):

    def post(self, request, *args, **kwargs):
        mobileNumber = request.data.get('mobileNumber', False)
        otp_sent = request.data.get('otp', False)


        if phone and otp_sent:
            old = PhoneOTP.objects.filter(phone__iexact = phone)
            if old.exists():
                old = old.first()
                otp_session_id = old.otp_session_id
                print("In validate otp"+otp_session_id)
                conn.request("GET", "https://2factor.in/API/V1/1028fcd9-3158-11ea-9fa5-0200cd936042/SMS/VERIFY/"+otp_session_id+"/"+otp_sent)
                res = conn.getresponse()
                data = res.read()
                print(data.decode("utf-8"))
                data=data.decode("utf-8")
                data=ast.literal_eval(data)



                if data["Status"] == 'Success':
                    old.validated = True
                    old.save()
                    return Response({
                        'status' : True,
                        'detail' : 'OTP MATCHED. Please proceed for registration.'
                            })

                else:
                    return Response({
                        'status' : False,
                        'detail' : 'OTP INCORRECT'
                    })



            else:
                return Response({
                        'status' : False,
                        'detail' : 'First Proceed via sending otp request'
                    })


        else:
            return Response({
                        'status' : False,
                        'detail' : 'Please provide both phone and otp for Validation'
                    })
#
# ##################### Request password to email ###################
# class RequestPasswordResetEmail(generics.GenericAPIView):
#     serializer_class = ResetPasswordEmailRequestSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#
#         email = request.data['email']
#
#         if CustomUser.objects.filter(email=email).exists():
#             user = CustomUser.objects.get(email=email)
#             uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
#             token = PasswordResetTokenGenerator().make_token(user)
#             current_site = get_current_site(
#                 request=request).domain
#             relativeLink = reverse(
#                 'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
#             absurl = 'http://'+current_site + relativeLink
#             email_body = 'Hello, \n Use link below to reset your password  \n' + absurl
#             data = {'email_body': email_body, 'to_email': user.email,
#                     'email_subject': 'Reset your passsword'}
#             Util.send_email(data)
#         return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
#
#
# class PasswordTokenCheckAPI(generics.GenericAPIView):
#     serializer_class = SetNewPasswordSerializer
#
#     def get(self, request, uidb64, token):
#
#         try:
#             id = smart_str(urlsafe_base64_decode(uidb64))
#             user = CustomUser.objects.get(id=id)
#
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)
#
#             return Response({'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)
#
#         except DjangoUnicodeDecodeError as identifier:
#             if not PasswordResetTokenGenerator().check_token(user):
#                 return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)
#
#
# class SetNewPasswordAPIView(generics.GenericAPIView):
#     serializer_class = SetNewPasswordSerializer
#
#     def patch(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

# class GoogleAuthAPIView(APIView):
#     """
#     Manage Google Login
#     """
#     #renderer_classes = (UserRenderer,)
#
#     def post(self, request):
#         token = request.data.get('access_token', None)
#         if token is None:
#             return Response({
#                 "message": "Please provide a token"
#             }, status.HTTP_401_UNAUTHORIZED)
#         user_info = requests.get(
#             "https://oauth2.googleapis.com/tokeninfo?id_token={}".format(token)).json()
#
#         if "error" in str(user_info):
#             return Response({"error": "Something went wrong,please try again"}, status.HTTP_401_UNAUTHORIZED)
#         user_data = {
#             'first_name': user_info['given_name'],
#             'last_name': user_info['family_name'],
#             'profilePic': user_info['picture'],
#             "email": user_info['email'],
#         }
#         email = user_data['email']
        # username = Utils.create_username(
        #     user_data['first_name'], user_data['last_name'])
        # filtered_user_by_email = CustomUser.objects.filter(email=email).first()
        # if filtered_user_by_email:
        #     user = authenticate(
        #         username=filtered_user_by_email.email, password='XXXXXXXX')
        #     if user is not None:
        #         return Response({
        #             'username': user.username,
        #             'email': user.email,
        #             'token': user.token})
        # else:
        #     user = {'username': username,
        #             'email': email, 'password': 'XXXXXXXX'}
        #
        #     #User.objects.create_user(**user)
        #     user = CustomUser.objects.filter(email=email).first()
        #     user.is_verified = True
        #     user.provider = "google"
        #     user.save()
        #     new_user = authenticate(username=user.email, password="XXXXXXXX")
            # return Response({
            #     'username': new_user.username,
            #     'email': new_user.email,
            #     'token': new_user.token})
