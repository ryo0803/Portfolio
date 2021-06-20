from django.db import models


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
