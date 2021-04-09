from django.urls import path
from . import views

urlpatterns =[
    path('companies/',views.companies),
    path('company/search/<str:keyword>',views.searchCompany),
    path('dbsave/',views.companyDbInsert),
]