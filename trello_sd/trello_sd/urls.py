from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from auth_server.views import EmployeeModelViewSet, SubDivisionModelViewSet

router = DefaultRouter()
router.register('employees', EmployeeModelViewSet)
router.register('subdivisions', SubDivisionModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
