from rest_framework.viewsets import ModelViewSet


from auth_server.models import Employee, SubDivision
from auth_server.serializers import EmployeeSerializer, SubDivisionSerializer


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.filter(state='Д')
    serializer_class = EmployeeSerializer


class SubDivisionModelViewSet(ModelViewSet):
    queryset = SubDivision.objects.all()
    serializer_class = SubDivisionSerializer
