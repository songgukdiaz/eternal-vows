from django.db import models

# Create your models here.

class InvitationCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code