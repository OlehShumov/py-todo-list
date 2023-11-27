from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-deadline"]

    def __str__(self):
        return (
            f"Task: {self.content}, "
            f"status: {'Done' if self.is_completed else 'Not done'}, "
        )
