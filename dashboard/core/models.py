from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=255)
    status = models.IntegerField(choices=
        (
            (1, "To Do"),
            (2, "On Progress"),
            (3, "Done")
        ),
        default = 1
    )
