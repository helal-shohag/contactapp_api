from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import contactView


router = DefaultRouter()

router.register("contacts",contactView)


urlpatterns = [
    path('',include(router.urls))
]
