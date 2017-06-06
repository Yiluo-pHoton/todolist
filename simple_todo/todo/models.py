from django.db import models
from django_openid_auth.models import User
from datetime import datetime
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User)
    todo = modelsCharField(max_length=200)
    flag = models.CharField(max_length=2, default='1')
    priority = models.CharField(max_length=2, default='0')
    pubtime = models.DataTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)

    class Meta:
        ordering = ['priority', 'pubtime']
