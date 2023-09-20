from django.db import models


class City(models.Model):
    name_en = models.CharField(max_length=32)
    name_uk = models.CharField(max_length=32)

    def __str__(self):
        return self.name_uk + ' | ' + self.name_en
