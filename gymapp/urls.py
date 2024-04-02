from django.urls import path
from gymapp import views

urlpatterns = [
    path('',views.Home, name="Home"),
    path('signup',views.Signup, name="signup"),
    path('login',views.handlelogin, name="hnadlelogin"),
    path('logout',views.handleLogout, name="handleLogout"),
    path('contact',views.contact, name="contact"),
    path('join',views.enroll, name="enroll"),
    path('profile',views.profile, name="profile"),
    path('gallery',views.gallery, name="gallery"),
    path('attendance',views.attendance, name="attendance"),
    path('services',views.services, name="services"),
    
    path('WeightGain',views.WeightGain, name="WeightGain"),
    path('WeightLoss',views.WeightLoss, name="WeightLoss"),
    path('strength',views.strength, name="strength"),
    path('basicplan',views.basicplan, name="basicplan"),
    path('intermediate',views.intermediate, name="intermediate"),
    path('pro',views.pro, name="pro"),

]


# Django Name - shivam
# Django Password - 123
# Django Email - er.shivamwallu@gmail.com







