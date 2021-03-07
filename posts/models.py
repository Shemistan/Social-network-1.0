from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey("Group", models.SET_NULL, blank=True,
                              null=True, related_name="posts")

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        show_to = f'{self.author} {self.pub_date} {self.text}'
        return show_to


class Group(models.Model):
    title = models.CharField("Group name", max_length=200)
    slug = models.SlugField("Slug", max_length=200, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
