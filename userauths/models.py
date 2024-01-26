from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from shortuuidfield import ShortUUIDField


# Create your models here.



GENDER = (
    ('female','Female'),
    ('male','Male')
)
RELATIONSHIP = (
    ('sigle','Sigle'),
    ('married','Married')
)


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER,default= 'male')    
    otp = models.CharField(max_length=10, blank=True, null=True)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['username']
    
    def __str__(self):
        return self.username
    
    
    
def user_diractory_path(filename, instance):
    ext= filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, ext)
    return "user_{0}/{1}.{2}".format(instance.user.id, filename)

class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabet='abcdefghijklmnopqrstuvwxyz')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to=user_diractory_path, default='cover.jpg')
    image = models.ImageField(upload_to=user_diractory_path, default='defaule.jpg')
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null= True, blank=True)
    gender = models.CharField( max_length=50, choices= GENDER, default= 'male')
    relationship = models.CharField( max_length=50, choices= RELATIONSHIP, default= 'sigle')
    bio = models.CharField(max_length=200, null= True, blank=True)
    about_me = models.TextField( null= True, blank=True)
    
    
    country = models.CharField(max_length=200, null= True, blank=True)
    city = models.CharField(max_length=200, null= True, blank=True)
    state = models.CharField(max_length=200, null= True, blank=True)
    address = models.CharField(max_length=200, null= True, blank=True)
    
    working_at = models.CharField(max_length=200, null= True, blank=True)
    
    
    instagram = models.CharField(max_length=200, null= True, blank=True)
    whatsapp = models.CharField(max_length=200, null= True, blank=True)
    verified = models.BooleanField(default=False)
    followers = models.models.ManyToManyField(User,  blank=True, related_name='followers')
    following = models.models.ManyToManyField(User,  blank=True, related_name='following')
    friends = models.models.ManyToManyField(User,  blank=True, related_name='friends')
    blocked = models.models.ManyToManyField(User,  blank=True, related_name='blocked')
    date = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.user.username
    
    
    
