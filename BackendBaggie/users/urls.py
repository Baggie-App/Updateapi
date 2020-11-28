from django.urls import path,include
from rest_framework.routers import SimpleRouter
#3rd party
from users.views import (
    RegisterView,
    RegisterCustomerView,
    LoginPhoneAPIView,
    LoginemailAPIView,
    VerifyEmail,
    PasswordTokenCheckAPI,
    SetNewPasswordAPIView,
    LogoutAPIView,
    RequestPasswordResetEmail,
    AccountlistView,
    )
from users.socialViews import (
   GoogleSocialAuthView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

#############################################
path('register/vendor/', RegisterView.as_view(), name="register"),
path('register/customer/', RegisterCustomerView.as_view(), name="registercustomer"),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

path('login/vendor/', LoginemailAPIView.as_view(), name="login"),
path('loginwithphone/customer/', LoginPhoneAPIView.as_view(), name ="loginwithphone"),
path('email-verify/', VerifyEmail.as_view(), name="email-verify"),

path('request-passwordchange-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
path('password-reset/<uidb64>/<token>/',
     PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
path('password-reset-complete', SetNewPasswordAPIView.as_view(),
     name='password-reset-complete'),
path('logout/', LogoutAPIView.as_view(), name="logout"),
#####################################################################
path('social/google/', GoogleSocialAuthView.as_view()),

path('vendorlist/', AccountlistView.as_view()),

]

# router = SimpleRouter()
# router.register('register', RegisterUserViewSet, basename='users')
# router.register('login', RegisterUserViewSet)
# urlpatterns = router.urls
