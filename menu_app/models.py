from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    url = models.CharField(max_length=200)
    menuName = models.CharField(max_length=100, default="") 

    def __str__(self):
        return self.name