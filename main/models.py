from django.db import models
from django.contrib.auth.models import User


class Guide(models.Model):

    title = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.title


class CommunityPost(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(
        CommunityPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"


class Phrase(models.Model):

    english_text = models.CharField(max_length=200)

    turkish_text = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    def __str__(self):
        return self.english_text