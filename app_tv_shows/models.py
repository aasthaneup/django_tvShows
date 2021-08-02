from django.db import models
from datetime import date, datetime
from time import strftime

# My custom manager
class ShowManager(models.Manager):
    def show_validator (self, postData):
        errors = {}
        if Show.objects.filter(title = postData['title']).exists() and postData['do_what']!= "update_record":
            errors['title'] = "The show title already exists. Please add any other show"

        if postData['do_what']== "update_record" and postData['title'] != postData['original_title'] and Show.objects.filter(title = postData['title']).exists():
            errors['title'] = "The show title already exists. Please check the title you entered"

        if len(postData['title']) < 2:
            errors['title'] = "The length of the Show's title must be at least 2 characters long"

        if len(postData['network']) < 3:
            errors['network'] = "The length of the network must be at least 3 characters long"
        
        if len(postData['releasedate']) == "":
            errors['releasedate'] = "The release date must be provided!"
        
        # print("datenow = ")
        # print(date.today())
        # print("date release string= "+postData['releasedate'])
        # print("release date = ")
        # print(datetime.strptime(postData['releasedate'], '%Y-%m-%d'))

        if datetime.strptime(postData['releasedate'], '%Y-%m-%d') >= datetime.now():
            # print("==========successful========")
            errors['releasedate'] = "Release date you entered is invalid. It must be in the past"

        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc'] = "The description (if given) must be at least 10 characters long"
        
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releasedate = models.DateField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ShowManager()