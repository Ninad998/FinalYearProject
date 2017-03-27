from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Result(models.Model):
    user = models.ForeignKey('auth.User')
    doc_id = models.IntegerField()
    authorList = models.CharField(max_length=200)
    predicted_author = models.CharField(max_length=200, null=True)
    train_accuracy = models.DecimalField(max_digits=11, decimal_places=10, null=True)
    validation_accuracy = models.DecimalField(max_digits=11, decimal_places=10, null=True)
    test_accuracy = models.DecimalField(max_digits=11, decimal_places=10, null=True)
    test_binary = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    upload_date = models.DateTimeField(default=timezone.now, null=False)
    status = models.DecimalField(max_digits=2, decimal_places=1, null=False, default=0.0)

    def running(self):
        self.completed = 1.0
        self.save()

    def complete(self, predicted_author, train_accuracy, validation_accuracy, test_accuracy, test_binary):
        self.predicted_author = predicted_author
        self.train_accuracy = train_accuracy
        self.validation_accuracy = validation_accuracy
        self.test_accuracy = test_accuracy
        self.test_binary = test_binary
        self.completed = 2.0
        self.save()

    def __str__(self):
        return str("User: %5s     Doc: %3s     Authors: %s" % (self.user, self.doc_id, self.authorList))