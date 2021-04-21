from django.db import models


class Task(models.Model):
    title = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:20]
