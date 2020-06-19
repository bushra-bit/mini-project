# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    img_path = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.name

