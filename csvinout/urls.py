from django.urls import path
from .views import (
   #PizzaListView,
   FileUploadView,# 追加
)
app_name = 'csvinout'
urlpatterns = [
   #path('pizzalist/', PizzaListView.as_view(), name='pizzalist'),  
   path('fileupload/', FileUploadView.as_view(), name='file-upload'),
]