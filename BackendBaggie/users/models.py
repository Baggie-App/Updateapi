from django.db import models
import jwt
import random
import os
import requests
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta
from django.conf import settings
from django.core.validators import RegexValidator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFill


class MyAccountManager(BaseUserManager):
	def create_vendoruser(self,vandorName=None,profileImage=None,email=None,mobileNumber=None,password=None,role='vendor'):
		if email is None:
			raise TypeError('Users should have a Email')
		if mobileNumber is None:
			raise TypeError('User should have a MobileNumber')
		if vandorName is None:
			raise TypeError("Vandor should have a vandorName")
		if profileImage is None:
			raise TypeError("Please add your Company Images")
		user = self.model(
		vandorName=vandorName,
		profileImage =profileImage,
		mobileNumber=mobileNumber,
		email=self.normalize_email(email))
		user.set_password(password)
		user.role = role
		if profileImage != None and vandorName !=None:
			user.save()
		else:
			return user
		return user

	def create_user(self,email=None,name=None, password=None,mobileNumber=None, role="customer"):
		if mobileNumber is None:
			raise TypeError('Users should have a MobileNumber')
		if email is None:
			raise TypeError('Users should have a Email')
		user = self.model(
		mobileNumber=mobileNumber,
		email=self.normalize_email(email),
		name = name
		)
		user.set_password(password)
		user.role = role
		user.save()
		return user

	def create_superuser(self,email=None,mobileNumber=None,password=None,role='superuser'):

		if password is None:
			raise TypeError('Password should not be none')
		if email is None:
			raise TypeError('Users should have a Email')
		if mobileNumber is None:
			raise TypeError('User should have a MobileNumber')

		user = self.model(
		mobileNumber=mobileNumber,
		email=self.normalize_email(email))
		user.set_password(password)
		user.is_superuser = True
		user.is_staff = True
		user.role = role
		user.save()
		return user

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
				  'twitter': 'twitter', 'email': 'email'}

class CustomUser(AbstractBaseUser,PermissionsMixin):
	username      = None
	email         = models.EmailField(verbose_name = "email", max_length = 35, unique =True)
	firstName     = models.CharField(max_length = 50, null=True)
	lastName      = models.CharField(max_length = 50, null = True)
	vandorName    = models.CharField(max_length=350, null=True, unique=True)
	name          = models.CharField(max_length=100, null=True)
	mobileNumber  = models.CharField(max_length= 15, unique=True, null=True)
	profileImage  = models.ImageField(upload_to='profiles/', null=True)
	varificationNumber = models.CharField(null=True, max_length=350)
	is_active     = models.BooleanField(default=True)
	is_staff      = models.BooleanField(default= False)
	is_verified   = models.BooleanField(default=False)
	provider      = models.CharField(max_length=25, null=True)
	role          = models.CharField(max_length=15, default='customer')
	created_at    = models.DateTimeField(auto_now_add=True)
	updated_at    = models.DateTimeField(auto_now=True)
	auth_provider = models.CharField(
		max_length=255, blank=False,
		null=False, default=AUTH_PROVIDERS.get('email'))
	phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
    #phone       = models.CharField('Phone',validators =[phone_regex], max_length=10, unique = True,null=True)

	REQUIRED_FIELDS = ['mobileNumber']
	USERNAME_FIELD  = 'email'

	objects = MyAccountManager()

	def __str__(self):
		return self.email


	@property
	def get_email(self):
		"""
		This method is required by Django for things like handling emails.
		Typically, this would be the user's first and last name. Since we do
		not store the user's real name, we return their emails instead.
		"""
		return self.email

	@property
	def get_mobileNumber(self):
         """
         This method is required by Django for things like handling emails.
         Typically, this would be the user's first and last name. Since we do
         not store the user's real name, we return their emails instead.
         """
         return self.mobileNumber



	def tokens(self):
		print(self.pk)
		refresh = RefreshToken.for_user(self)
		return{
		    'refresh': str(refresh),
            'access': str(refresh.access_token)
		}

class PhoneOTP(models.Model):

    phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    mobileNumber= models.CharField(max_length=17, unique = True)
    otp         = models.CharField(max_length=9, blank = True, null=True)
    count       = models.IntegerField(default=0, help_text = 'Number of otp_sent')
    validated   = models.BooleanField(default = False, help_text = 'If it is true, that means user have validate otp correctly in second API')
    otp_session_id = models.CharField(max_length=120, null=True, default = "")
    #username    = models.CharField(max_length=20, blank = True, null = True, default = None )
    email       = models.CharField(max_length=50, null = True, blank = True, default = None)
    password    = models.CharField(max_length=100, null = True, blank = True, default = None)



    def __str__(self):
        return str(self.mobileNumber) + ' is sent ' + str(self.otp)



class BaseAbstractModel(models.Model):
    """
    This model defines base models that implements common fields like:
    created_at
    updated_at
    is_deleted
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        """Soft delete a model instance"""
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
        ordering = ['-created_at']

class BlackList(BaseAbstractModel):
    """
    This class defines black list model.
    Tokens of logged out users are stored here.
    """

    token = models.CharField(max_length=200, unique=True)

    @staticmethod
    def delete_tokens_older_than_a_day():
        """
        This method deletes tokens older than one day
        """
        past_24 = datetime.now() - timedelta(hours=24)

	# @property
	# def token(self):
	# 	print("hello i am inside token")
	# 	"""
	# 	We need to make the method for creating our token private. At the
	# 	same time, it's more convenient for us to access our token with
	# 	`user.token` and so we make the token a dynamic property by wrapping
	# 	in in the `@property` decorator.
	# 	"""
	# 	return self._generate_jwt_token()
	#
	# def _generate_jwt_token(self):
	# 	"""
	# 	We generate JWT token and add the user id, username and expiration
	# 	as an integer.
	# 	"""
	# 	token_expiry = datetime.now() + timedelta(hours=24)
	#
	# 	token = jwt.encode({
	# 		'id': self.pk,
	# 		'email': self.get_email,
	# 		'mobileNumber':self.get_mobileNumber,
	# 		'exp': int(token_expiry.strftime('%s'))
	# 	}, settings.SECRET_KEY, algorithm='HS256')
	#
	# 	return token.decode('utf-8')

        BlackList.objects.filter(created_at__lt=past_24).delete()
