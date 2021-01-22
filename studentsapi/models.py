from django.db import models


class Student(models.Model):
    scores = (
        ('2', 'неуд'),
        ('3', 'уд'),
        ('4', 'хор'),
        ('5', 'отл'),
    )
    fio = models.CharField(max_length=100)
    birthdate = models.DateField(default='1900-01-01', null=True)
    record_status = models.CharField(max_length=4, choices=scores, default='неуд')
