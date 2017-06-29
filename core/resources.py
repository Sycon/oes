#from django.contrib.auth.models import User
from tastypie.resources import ModelResource

from core.models import User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
