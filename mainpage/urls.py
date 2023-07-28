from django.contrib.auth.views import LoginView
from django.urls import path
from .views import MyLogoutView, MainView, CalculatorView, registration, ProfileDetailView, ProfileUpdateView,CalculationDetailView, CalculationListView, My_Oreder_CalculationListView
from mainpage import views


app_name = "mainpage"
urlpatterns = [
    path('registration/', registration, name="register"),
    path('calculator/', CalculatorView.as_view(), name="calculator"),
    #path('main/<int:pk>/update/', ProfileUpdateView.as_view(), name="profile_update"),
    path('editprofile/', views.update_profile),
    path('calculation/<int:pk>/', CalculationDetailView.as_view(), ),
    path('calculation_list/', CalculationListView.as_view(), name="calculation"),
    path('mycalculations/', My_Oreder_CalculationListView.as_view(), name="calculation"),
    path('profile/', ProfileDetailView.as_view(), name="profile"),

    path('logout/', MyLogoutView.as_view(), name="logout"),
    path("",
         LoginView.as_view(
             template_name="mainpage/login.html",
             redirect_authenticated_user=True,
         ),
         name="login"),
    path('main/', MainView.as_view(), name="main"),
    ]
