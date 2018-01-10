from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Visitor(models.Model):
    Male = 'Male'
    Female = 'Female'
    GenderChoices = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=GenderChoices, default=Male)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username+' ~ '+self.address

@receiver(post_save, sender=User)
def update_user_visitor(sender, instance, created, **kwargs):
    if created:
        Visitor.objects.create(user=instance)
    instance.visitor.save()

class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    book_file = models.FileField(blank=True)
    thumbnail = models.FileField(blank=False)
    author = models.CharField(max_length=50, blank=False)
    publisher = models.CharField(max_length=80, blank=True)
    publish_date = models.DateField(blank=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title+" - "+self.author