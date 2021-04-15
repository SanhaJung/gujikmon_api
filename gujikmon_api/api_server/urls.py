from django.urls import path
from . import views

urlpatterns =[
    path('companies/',views.companies),
    path('company/search/<str:keyword>',views.searchCompany),
    path('user/favorite/update/',views.favorite_Company_Update),
    path('user/favorite/list/<int:user_pk>',views.favorite_Companies),
]