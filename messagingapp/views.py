from django.shortcuts import render,redirect,get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.db.models import Q
from .models import Message

@login_required(login_url="/login/")
def showmessage(request):
    sent_messages = Message.objects.filter(sender=request.user).order_by("-created_at")

    received_messages = Message.objects.filter(receiver=request.user).order_by("-created_at")

    return render(request, "messagingapp/showmessage.html", {
        "sent_messages": sent_messages,
        "received_messages": received_messages
    })
    

@login_required(login_url="/login/")
def addmessage(request):
    if request.method == "POST":
        message = request.POST["message"]
        receiver_id = request.POST["receiver"]

        receiver = User.objects.get(id=receiver_id)

        allowed = models.MessageRequest.objects.filter(
            Q(sender=request.user, receiver=receiver) |
            Q(sender=receiver, receiver=request.user),
            accepted = True
        ).exists()
        
        if allowed:
            models.Message.objects.create(
                sender = request.user,
                receiver=receiver,
                message=message
            )

        return redirect("messagingapp:showmessage")

    else:
        friends_relations = models.MessageRequest.objects.filter(
            Q(sender=request.user) | Q(receiver=request.user),
            accepted = True
        )

        friends = []
        for f in friends_relations:
            if f.sender == request.user:
                friends.append(f.receiver)
            else:
                friends.append(f.sender)

        return render(request,"messagingapp/addmessage.html",{
            "users":friends
        })                    

    

@login_required
def send_request(request,user_id):
    receiver = User.objects.get(id=user_id)

    if receiver == request.user:
        return redirect("messagingapp:friends")
    

    models.MessageRequest.objects.get_or_create(
        sender=request.user,
        receiver=receiver
    )

    return redirect("messagingapp:friends")




@login_required(login_url="/login/")
def friends(request):
    user = request.user

    incoming_requests = models.MessageRequest.objects.filter(
        receiver = user,
        accepted = False
    )

    outgoing_requests = models.MessageRequest.objects.filter(
        sender = user,
        accepted = False
    )

    friends_relations = models.MessageRequest.objects.filter(
        Q(sender=user) | Q(receiver=user),
        accepted = True
    )

    friends = []
    for f in friends_relations:
        if f.sender == user:
            friends.append(f.receiver)
        else:
            friends.append(f.sender)

    friends_ids = [u.id for u in friends]

    request_ids = list(outgoing_requests.values_list("receiver_id", flat=True))
    received_ids = list(incoming_requests.values_list("sender_id",flat=True))

    users = User.objects.exclude(id=user.id)\
        .exclude(id__in=friends_ids)\
        .exclude(id__in=request_ids)\
        .exclude(id__in=received_ids)

    return render(request, "messagingapp/friends.html", {
        "incoming_requests": incoming_requests,
        "outgoing_requests": outgoing_requests,
        "friends": friends,
        "users": users
    })

@login_required
def accept_request(request, request_id):
    req = models.MessageRequest.objects.get(id=request_id)
    req.accepted = True
    req.save()
    return redirect("messagingapp:friends")

@login_required
def reject_request(request,request_id):
    models.MessageRequest.objects.get(id=request_id).delete()
    return redirect("messagingapp:friends")

@login_required
def remove_friend(request, user_id):
    other_user = User.objects.get(id=user_id)

    models.MessageRequest.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user),
        accepted=True
    ).delete()

    return redirect("messagingapp:friends")

@login_required
def delete_message(request,message_id):
    if request.method == "POST":
        message = get_object_or_404(models.Message, id=message_id)

        if message.sender == request.user:
            message.delete()
    return redirect("messagingapp:showmessage")    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self,form):
        user = form.save()

        login(self.request,user)

        messages.success(self.request,"Registration successful, logged in!")

        return super().form_valid(form)
    

def logout_view(request):
    logout(request)
    return redirect("login")    