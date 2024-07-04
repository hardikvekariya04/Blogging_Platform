from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Model for Blog Post 
class Post(models.Model):
    title = models.CharField(_("Post title"), max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        null=True,
        on_delete=models.SET_NULL,
    )
    image = models.ImageField(null=True,upload_to='image/')
    description = models.TextField(_("Post description"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
