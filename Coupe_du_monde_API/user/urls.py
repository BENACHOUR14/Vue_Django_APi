from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
