from django.urls import path

from api import views

urlpatterns = [
    path("user/", views.UserAPIView.as_view()),
    # path("register/", views.RegisterView.as_view({"get":check_user})),
    path("emp/", views.EmployeeView.as_view()),
    path("emp/<str:id>", views.EmployeeView.as_view()),
    # path("rate/", views.SendMessageAPIView.as_view()),
]
