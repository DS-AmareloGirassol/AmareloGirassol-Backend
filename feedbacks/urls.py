from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('feedback', views.FeedbackViewSet)
