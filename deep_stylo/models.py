from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Result(models.Model):
    user = models.ForeignKey('auth.User')
    doc_id = models.IntegerField()
    authorList = models.CharField(max_length=200)
    test_acc = models.DecimalField(max_digits=11, decimal_places=10, null=True)
    test_bin = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    upload_date = models.DateTimeField(default=timezone.now, null=False)
    completed = models.DecimalField(max_digits=2, decimal_places=1, null=False, default=0.0)

    def complete(self, test_acc, test_bin):
        self.test_acc = test_acc
        self.test_bin = test_bin
        self.completed = 2.0
        self.save()

    def __str__(self):
        return str("User: %5s     Doc: %3s     Authors: %s" % (self.user, self.doc_id, self.authorList))