from django.db import models

class ProjectModel(models.Model):
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)

    def __str__(self):
        return    "like =" + str(self.like) + " " + "dislike =" +str(self.dislike)
    
