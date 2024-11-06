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


class BlogsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ['-id']
