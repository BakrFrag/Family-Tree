from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
# Create your models here.

class Member(AbstractUser):
    parent = models.ForeignKey( 
        'self' , 
        blank = True , 
        null = True , 
        on_delete = models.CASCADE 
    )

    def clean(self):
        """
        allow validate parsed password as predefind password validators
        """
        try:
            
            validate_password(self.password)
            
        except Exception as E:
           
            raise ValidationError({
                "password":"parsed password value don't match validation"
            })

    def save(self , *args , **kwargs):
        """
        full model clean before save
        """
        
        self.full_clean()
        return super(Member,self).save(*args,**kwargs)