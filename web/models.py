from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    class Item:
        db_table = "web_item"
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ["-id"]


    def __str__(self):
        return self.name
  


class DoneItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class DoneItems:
        db_table = "web_doneitems"
        verbose_name = "doneitems"
        verbose_name_plural = "doneitemss"
        ordering = ["-id"]


    def __str__(self):
        return self.name
  