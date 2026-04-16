from django.urls import path
from . import views

app_name = "messagingapp"

urlpatterns = [
    path('',views.showmessage,name="showmessage"),
    path('addmessage/',views.addmessage,name="addmessage"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path("friends/",views.friends,name="friends"),
    path("send_request/<int:user_id>/", views.send_request, name="send_request"),
    path("accept_request/<int:request_id>/", views.accept_request, name="accept_request"),
    path("reject_request/<int:request_id>/", views.reject_request, name="reject_request"),
    path("remove_friend/<int:user_id>/", views.remove_friend, name="remove_friend"),
    path("delete_message/<int:message_id>/", views.delete_message, name="delete_message")
]
