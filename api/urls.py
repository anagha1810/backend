from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import courseViewSet, ratingViewSet,UserViewSet

router = routers.DefaultRouter()
router.register('courses', courseViewSet)
router.register('ratings', ratingViewSet)
router.register('users', UserViewSet)

urlpatterns = [

    path('', include(router.urls)),

]


