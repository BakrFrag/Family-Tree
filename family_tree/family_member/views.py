from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin,  ListModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser , IsAuthenticated , OR
from rest_framework.decorators import action
from .serializers import MemberSerializer, RelativeAddSerializer
from .models import Member 


class MemberViewset(
    CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    """
    http method Post 
    http action Create
    handle user registeration 
    check for password validation & user object creation
    """
    
    serializer_class = MemberSerializer
    

    def get_queryset(self):
        """
        superuser , can view all users with all associated relatives and filter with username
        normal user can only view his family tree or family tree of his relatives 
        otherwise none
        """
        queryset = Member.objects.exclude(is_staff=True).prefetch_related("member_set").all()
        user = self.request.user 
        kwargs = self.request.query_params
        parsed_username = kwargs.get("username")
        if user.is_staff:
            return queryset.filter(username=parsed_username) if parsed_username else queryset

        elif not parsed_username:
            return queryset.filter(username=user.username)


        return queryset.filter(username=parsed_username) if parsed_username in queryset.filter(username = user.username).first().member_set.values_list("username",flat = True) else Member.objects.none()

            
        
    def get_permissions(self):
        """
        overide default permissions
        if user is superuser / staff user can list all users with thier relatives
        otherwise , user register allow for all 
        """
        if self.request.method == "GET":
            return [OR(IsAdminUser(),IsAuthenticated())]

        return [AllowAny()] 


    @action(detail=False,methods=["POST"],serializer_class=RelativeAddSerializer,permission_classes=[IsAuthenticated],url_path="add/relatives",url_name="add_relatives")
    def add_relatives(self,request):
        """
        add relatives to user
        """
        serializer = RelativeAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        relative_id = serializer.validated_data.get("relative_id")
        parent_user = request.user 
      #  relative_user = Member.objects.filter(id= relative_id).first()
        
        relative_user = get_object_or_404(Member , id = relative_id)
        if parent_user == relative_user:
            return Response({
                "message":"Parent user is the same as relative user!"
            },status = status.HTTP_400_BAD_REQUEST)
        elif relative_user in parent_user.member_set.all():
            return Response(
                {
                    "message":f"relative user: {relative_user.username} is already in relatives"
                }, status = status.HTTP_400_BAD_REQUEST
            )
        elif relative_user.parent is None and not relative_user.member_set.all():
                parent_user.member_set.add(relative_user)
                return Response({
                    "message":f"relative user {relative_user.username} add to parent user {parent_user.username}"
                },status = status.HTTP_200_OK)  
        return Response({
                "message":f"relative user {relative_user.username} associated with anther parent user or relative user is already parent user"
            },status = status.HTTP_400_BAD_REQUEST) 