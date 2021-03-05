from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey("Group", models.SET_NULL, blank=True,
                              null=True, related_name="group_posts")

    # class Meta:
        # sorted_post = Post.objects.order_by("-pub_date")[:10]


    def __str__(self):
        return self.author


class Group(models.Model):
    title = models.CharField("Group name", max_length=200)
    slug = models.SlugField("Page address", max_length=200, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
