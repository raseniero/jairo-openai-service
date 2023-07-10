from django.urls import path
from srt_converter_app import views

urlpatterns = [
    path('generate-fcpxml/', views.convert_text_to_fcpxml, name='generate-fcpxml'),
]