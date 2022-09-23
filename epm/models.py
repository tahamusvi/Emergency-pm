from django.db import models
from django.utils import timezone
from accounts.models import User
# Create your models here.
# ----------------------------------------------------------------------------------------------------------------------------
class Epm(models.Model):
    text = models.CharField(max_length=1000)
    # sender = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name="outbox")
    # receiver = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name="inbox")
    time = models.DateTimeField(default=timezone.now)
    us = models.BooleanField()


    def __str__(self):
        return str(self.text)
