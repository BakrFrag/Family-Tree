from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers 
from family_member.models import Member 



class MemberSerializer(serializers.ModelSerializer):
    """
    handle user registeration & user family tree
    """
    password_confirm = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)
    associated_members = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Member
        fields = ['id','username','email','password','password_confirm','associated_members']

    def get_associated_members(self,obj):
        """
        get associated members recursively 
        """
        serializer = self.__class__(obj.member_set.all() , many=True)
        return serializer.data

    def validate_password(self, password_value):
        
        try:
           
            validate_password(password_value)
            return password_value

        except ValidationError as E:
            
            raise serializers.ValidationError(E)

    def validate(self,attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("password_confirm")
        if password != confirm_password:
            raise serializers.ValidationError({"password":"parsed password & confirm password don't match"})
        
        attrs.pop("password_confirm")
        return attrs

    def create(self, validated_data):
       
        return Member.objects.create_user(
            **validated_data
        )

class RelativeAddSerializer(serializers.Serializer):
    """
    handle relative id 
    """
    relative_id = serializers.IntegerField()