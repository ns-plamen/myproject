from django.db import models

import datetime

class Dirpath(models.Model):
    dirway = models.CharField(max_length=200)
    def __unicode__(self):
        return self.dirway
    is_dir = models.IntegerField()
class Target(models.Model):
    dirpath = models.ForeignKey(Dirpath)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.dirway
    target_type = models.IntegerField()
    size = models.IntegerField()
    creation = models.DateTimeField('cration time')
    modified = models.DateTimeField('last modified')
    accessed = models.DateTimeField('last accessed')
