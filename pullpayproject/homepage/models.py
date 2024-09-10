from django.db import models


class ChurchName(models.Model):
    church_name_text = models.CharField(max_length=200)


class ChurchSize(models.Model):
    size_int = models.IntegerField(default=0)


class ChurchType(models.Model):
    church_type_text = models.CharField(max_length=200)
