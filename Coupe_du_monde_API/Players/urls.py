from rest_framework import routers
from Players import views

router = routers.DefaultRouter()
router.register(r'Players', views.PlayerViewSet)
