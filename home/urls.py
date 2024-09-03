from django.urls import path,include 
#from .views import home
from . import views
urlpatterns=[
    #path('',home,name='home')
    #path('',views.Indexview,name="Index")

    # path('',views.InsertPageView,name="insertpage"),
    # path('insert/',views.InsertData,name='insert'),
    # path('Showpage/',views.Showpage,name='Showpage'),
    # path('EditPage/<int:pk>',views.EditPage,name='EditPage'),
    # path('Update/<int:pk>',views.UpdateData,name='Update'),
    # path('delete/<int:pk>',views.DeleteData,name='delete'),


    path("",views.IndexPage,name="index"),
    path("upload/",views.UploadImage,name="imageupload"),
    path("showing/",views.ImageFetch,name="show"),
]