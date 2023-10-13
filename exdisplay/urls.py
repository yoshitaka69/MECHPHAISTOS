from django.urls import path
from exdisplay.views import SampleAPIView

urlpatterns = [
    path("sample/", SampleAPIView.as_view(), name="sample"),
]
