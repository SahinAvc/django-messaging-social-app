from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MessageRequest(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sent_requests")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="received_requests")    
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.accepted})"

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sent_messages")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="received_messages")
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.message}"