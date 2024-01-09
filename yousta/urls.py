from django.urls import path
from yousta.views import SignUpView,SignInView,CategoryCreateView,remove_category,\
    ClothCreateView,ClothListView,ClothUpdateView,remove_clothview,ClothVarientCreateView,ClothDetailView,ClothVarientUpdateView,remove_clothVarientview,OfferCreateView,remove_clothofferview,sign_outview,IndexView




urlpatterns=[path("register/",SignUpView.as_view(),name="signup"),
             path("",SignInView.as_view(),name="signin"),
             path("categories/add",CategoryCreateView.as_view(),name="category-add"),
             path("categories/<int:pk>/remove",remove_category,name="remove-category"),
             path("cloth/add",ClothCreateView.as_view(),name="cloth-add"),
             path("cloth/all",ClothListView.as_view(),name="cloth-list"),
             path("cloth/<int:pk>/change",ClothUpdateView.as_view(),name="cloth-change"),
             path("cloth/<int:pk>/remove",remove_clothview,name="cloth-remove"),
             path("cloths/<int:pk>/varients/add",ClothVarientCreateView.as_view(),name="add-varient"),
             path("cloths/<int:pk>",ClothDetailView.as_view(),name="cloth-detail"),
             path("varients/<int:pk>/change",ClothVarientUpdateView.as_view(),name="update-varient"),
             path("varients/<int:pk>/remove",remove_clothVarientview,name="remove-varient"),
             path("offer/<int:pk>/add",OfferCreateView.as_view(),name="offer-add"),
             path("offer/<int:pk>/remove",remove_clothofferview,name="offer-remove"),
             path("logout/",sign_outview,name="signout"),
             path("index/",IndexView.as_view(),name="index")



]