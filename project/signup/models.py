from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Visitor(models.Model):
    Male = 'ML'
    Female = 'FM'
    GenderChoices = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=GenderChoices, default=Male)
    address = models.CharField(max_length=120)

@receiver(post_save, sender=User)
def update_user_visitor(sender, instance, created, **kwargs):
    if created:
        Visitor.objects.create(user=instance)
    instance.visitor.save()