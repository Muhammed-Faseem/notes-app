from django.db import models

# Placeholder model for Django's admin and ORM
class Note(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50] if self.body else "Empty Note"