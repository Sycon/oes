from django.conf.urls import url, include
from . import views
#from tastypie.api import Api
#from .resources import UserResource
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserView)

#res = UserResource()

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
