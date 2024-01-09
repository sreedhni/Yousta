from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions

from api.serializers import Userserializer,ClothSerializer,CartSerializer,OrderSerializer,ReviewSerializer
from yousta.models import Cloths,ClothVarients,Carts,Orders
# Create your views here.


class UsercreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class ClothsView(ModelViewSet):
    # authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ClothSerializer
    model=Cloths
    queryset=Cloths.objects.all()

    @action(methods=["post"],detail=True)
    def cart_add(self,request,*args,**kwargs):
        vid=kwargs.get("pk")
        varient_obj=ClothVarients.objects.get(id=vid)
        user=request.user
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(clothvarient=varient_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    @action(methods=["post"],detail=True)
    def place_order(self,request,*args,**kwargs):
        vid=kwargs.get("pk")
        varient_obj=ClothVarients.objects.get(id=vid)
        user=request.user
        serilizer=OrderSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save(clothvarient=varient_obj,user=user)
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)
    
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        cid=kwargs.get("pk")
        obj=Cloths.objects.get(id=cid)
        user=request.user
        serilizer=ReviewSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save(cloth=obj,user=user)
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)

        
class OrderView(ViewSet):
    # authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Orders.objects.filter(user=request.user)
        serializer=OrderSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Orders.objects.get(id=id)
        if instance.user==request.user:
            instance.delete()
            return Response(data={"msg":"deleted"})
        else:
            return Response(data={"message":"permission denied"})

        
class CartsView(ViewSet):
    # authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CartSerializer

    def list(self,request,*args,**kwargs):
        qs=Carts.objects.filter(user=request.user)
        serializer=CartSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Carts.objects.get(id=id)
        if instance.user==request.user: #only the user can delete their cart product
            instance.delete()
            return Response(data={"msg":"deleted"})
        else:
            return Response(data={"message":"permission denied"})
        
        