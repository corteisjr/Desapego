from doeja.models import *
from .Timestamp import TimestampedModel

class Profile(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.user.username)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass
        
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
        
