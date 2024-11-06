from django.db import models


class UsersModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-id']
