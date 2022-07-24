from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='Tasks')
router.register(r'teams', TeamVievSet, basename='Teams')
router.register(r'users', UsersVievSet, basename='Users')

urlpatterns = router.urls
