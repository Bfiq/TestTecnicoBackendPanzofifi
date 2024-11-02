from .views import CommentView
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'comments', CommentView, basename="comments")

urlpatterns = router.urls
