from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.

class Manager(BaseUserManager):
	def create_user(self, username, password):
		if not username:
			raise ValueError("Username is required")
		if not password:
			raise ValueError("Password cannot be blank")

		user = self.model(
			username = username,
			password = password,
		)

		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(
			username = username,
			password = password,
		)

		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True
		user.save(using = self._db)
		return user

class User(AbstractBaseUser):
	username = models.CharField(primary_key=True, max_length=64)
	password = models.CharField(max_length=64)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['password']

	objects = Manager()

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True