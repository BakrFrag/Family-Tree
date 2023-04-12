from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin ,  ListModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAdminUser
from .serializers import MemberSerializer 
from .models import Member 


class MemberRegisterViewset(
    CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    """
    http method Post 
    http action Create
    handle user registeration 
    check for password validation & user object creation
    """
    
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    def get_permissions(self):
        """
        overide default permissions
        if user is superuser / staff user can list all users with thier relatives
        otherwise , user register allow for all 
        """
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()] 