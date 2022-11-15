from django.urls import path,include
from .views import ProductsList,CategoryList,ProductDetails,CategoryDetails,ProductPostSearch

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetails.as_view()),
    path('products/', ProductsList.as_view()),
    path('product_details/', ProductDetails.as_view()),
    path('product_search/', ProductPostSearch.as_view()),
]