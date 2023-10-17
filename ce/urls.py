from django.urls import path
from ce.views import SampleAPIView

urlpatterns = [
    path("sample/", SampleAPIView.as_view(), name="sample"),
]