from django.urls import path
from shopapi.views import CategoryAPIView, ProductAPIView, SubscriberAPIView   


urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('subscribers/', SubscriberAPIView.as_view()),
]