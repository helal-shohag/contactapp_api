from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import contactView,bookView,authorView


router = DefaultRouter()

router.register("contacts",contactView)
router.register("book",bookView)
router.register('author',authorView)

urlpatterns = [
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('',include(router.urls)),
]

