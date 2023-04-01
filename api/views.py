from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import *
from rest_framework import status
from keras.models import load_model
model = load_model('savedModels/xray_model.h5')
# Create your views here.
# @api_view(['GET'])
def index(request):
    form = ImageForm()
    return render(request,'api/index.html',{
        "form":form,
    })

@api_view(['POST'])
def compute(request):
    form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
        print("valid")
        form.save()
        img_object = form.instance
        predictions = model.predict([[None,180,180,3]])
        print(predictions)
        # print(img_object.image.url)
        return Response({
            "done":"done",
            "error":form.errors
        })
    return Response(status=status.HTTP_404_NOT_FOUND)