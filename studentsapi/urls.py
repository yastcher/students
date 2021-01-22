from rest_framework.routers import DefaultRouter

from .views import StudentView

router = DefaultRouter()

router.register(r'info', StudentView, basename='info')

urlpatterns = router.urls
