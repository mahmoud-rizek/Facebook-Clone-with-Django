from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from shortuuid.django_fields import ShortUUIDField

from django.utils.text import slugify
import shortuuid

from django.db.models.signals import post_save
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
    cover_image = models.ImageField(upload_to=user_diractory_path, null= True, blank=True, default='cover.jpg')
    image = models.ImageField(upload_to=user_diractory_path, null= True, blank=True, default='defaule.jpg')
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
    followers = models.ManyToManyField(User,  blank=True, related_name='followers')
    following = models.ManyToManyField(User,  blank=True, related_name='following')
    friends = models.ManyToManyField(User,  blank=True, related_name='friends')
    blocked = models.ManyToManyField(User,  blank=True, related_name='blocked')
    date = models.DateTimeField(auto_now_add= True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self):
        if self.full_name == None or self.full_name == "":
            return self.user.username
        else:
            return self.full_name
    
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug ==None:
            uuid_key = shortuuid.uuid()
            uniqueid= uuid_key[:4]
            self.slug = slugify(self.user.username) + '-' + str(uniqueid.lower())
        super(Profile, self).save(*args, **kwargs)
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
        
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


    
    
