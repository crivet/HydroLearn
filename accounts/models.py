from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.UserManager import UserManager
import uuid

'''
    Custom user implementation to use email as the 'username' 
    overriding default django auth settings

    also provides some additional permissions settings and a crated date

    tied to the UserManager

    to utilize this model include the following  in settings.py
    AUTH_USER_MODEL = 'accounts.User'

    ^ potentially the wrong path so just be careful

'''


class User(AbstractUser):
    # password is a default field, so no need to add it here
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)  # can log in
    is_staff = models.BooleanField(default=False)  # staff user
    is_superuser = models.BooleanField(default=False)  # superuser


    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.profile:
            if self.profile.get_full_name():
                return self.profile.get_full_name()

        return None

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return super(User, self).has_perm(perm, obj)

    def has_module_perms(self, app_label):
        return super(User,self).has_module_perms(app_label)

    @property
    def username(self):
        return self.email

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def is_admin(self):
        return self.is_superuser

    # these methods were overwriting required attributes for djangocms
    #  CMS Requires: is_active, is_staff, & is_superuser
    # @property
    # def is_staff(self):
    #     return self.is_staff

    # @property
    # def is_active(self):
    #     return self.is_active


''' 
    User Profile information.
       Extendable model linked to system users to store additional information on the user
'''


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    email_confirmed = models.BooleanField(default=False)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        elif self.first_name:
            return "%s" % self.first_name
        else:
            return None

    # add any additional information to be tied to the user
    #
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)

    # potentially add mappings to created modules, shared_with modules
    # (most likely better represented in module)

    # created_modules =
    # shared_with_modules =

    # maybe
    # created_topics =
    # shared_with_topics =
    # created_sections =
    # shared_with_sections =

# Extend the post_save event's create method to map a user to a
# profile instance for newly created users
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
