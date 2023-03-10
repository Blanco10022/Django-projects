from django.db import models
from django.contrib.auth.models import User
import os

def renomer_image(instance, filename):
    upload_to = 'image/'
    #pho.png
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "profile_pic/{}.{}".format(instance.user.username, ext)
    return os.path.join(upload_to, filename)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(upload_to=renomer_image, blank=True)

    student = 'student'
    lecturer = 'lecturer'
    parent = 'parent'

    type_user = [
        (student, 'student'),( lecturer, 'lecturer'), (parent, 'parent')
    ]

    type_profile = models.CharField(max_length=100, choices=type_user, default=student)


    def __str__(self):
        return self.user.username


