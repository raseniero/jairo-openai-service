from django.db import models


# Create your models here.
class ChatGPT(models.Model):
    name = models.CharField(max_length=100, null=True, default="")
    system_input = models.CharField(max_length=100)
    user_input = models.CharField(max_length=100)
    bot_response = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "chatgpt"
        verbose_name = "ChatGPT"
        verbose_name_plural = "ChatGPTs"

    def __str__(self):
        return str(self.name)


class ApplicationSettings(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        db_table = "application_settings"
        verbose_name = "ApplicationSettings"
        verbose_name_plural = "ApplicationSettings"

    def __str__(self):
        return str(self.name)
