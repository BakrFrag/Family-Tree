from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin ,  ListModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import MemberSerializer 
from .models import Member 


class MemberRegisterViewset(
    CreateModelMixin , 
    viewsets.GenericViewSet):
    """
    http method Post 
    http action Create
    handle user registeration 
    check for password validation & user object creation
    """
    permission_classes = [AllowAny]
    serializer_class = MemberSerializer