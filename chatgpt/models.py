from django.db import models


# Create your models here.
class ChatGPT(models.Model):
    system_input = models.CharField(max_length=100)
    user_input = models.CharField(max_length=100)
    bot_response = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "chatgpt"
        verbose_name = "ChatGPT"
        verbose_name_plural = "ChatGPTs"

    def __str__(self):
        return self.user_input
