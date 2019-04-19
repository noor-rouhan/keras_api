from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('test-viewset', views.testviewsets,base_name= 'test-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.UserProfileFeeedViewSet)

urlpatterns=[
    path('api_test_view/',views.HelloApiView.as_view()),
    path('',include(router.urls))

]
