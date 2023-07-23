from doeja.models import *


class Donation(TimestampedModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name_of_object = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    date_of_donation = models.DateField(default=None, null=True, blank=True)
    status = models.IntegerField(choices=DONATION_STATUS, default=1)
    picture = models.ImageField(null=True, blank=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.name_of_object} - {self.category}'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)