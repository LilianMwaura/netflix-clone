from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ModelForm




# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/',default='DEFAULT VALUE')
    bio=models.TextField()
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    user_name=models.CharField(max_length=20,null=True)
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile
    def __str__(self):
       return str(self.user_name)
   
   
class Image(models.Model):
    image = models.ImageField('pictures',default='DEFAULT VALUE')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    def __str__(self):
       return str(self.user)
    

    

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']
    