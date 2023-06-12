from django.db import models

# Create your models here.
class Staff(models.Model):

    POSITION = [
        ("JR", "Junior"),
        ("MD", "Middle"),
        ("SR", "Senior")
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    position = models.CharField(max_length=12, choices=POSITION)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    experience = models.IntegerField()
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()

    def __str__(self) -> str:
        return self.first_name+' '+self.last_name