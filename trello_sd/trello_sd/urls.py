from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from auth_server.views import EmployeeModelViewSet, SubDivisionModelViewSet, MainView

router = DefaultRouter()
router.register('employees', EmployeeModelViewSet)
router.register('subdivisions', SubDivisionModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include(('auth_server.urls', 'auth_server'), namespace='auth_server')),
    path('', MainView.as_view())
]
