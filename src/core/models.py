from django.db import models


class ToDo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created', )
