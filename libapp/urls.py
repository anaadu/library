from django.urls import path
from libapp import views

urlpatterns = [
    path('addbook',views.addbook),
    path('admn',views.adminpage),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('home',views.homepage),
    path('adminlogin',views.adminlogin),
    path('issuebook',views.Issuebook),
    path('issuedbook',views.Issued_book),
    path('delete1/<rid>',views.deleteissuebook),
    path('statfilter/<sf>',views.statfilter),
    path('catfilter/<cf>',views.catfilter),
]
