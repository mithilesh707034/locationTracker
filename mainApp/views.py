from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
import json
import io


@csrf_exempt
def add_member(Request):
    if (Request.method=="POST"):
        data=Member()
        data.name=Request.POST.get('name')
        data.email=Request.POST.get('email')
        data.phone=Request.POST.get('phone')
        data.latitude=Request.POST.get('latitude')
        data.longitude=Request.POST.get('longitude')
        data.save()
        msg={'status':True,'message':"Record Added Successfully..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")
          

@csrf_exempt
def get_member(Request):
     if (Request.method=="POST"):
          phone=Request.POST.get('phone')
          try:
               data=Member.objects.get(phone=phone)
               if(data):
                 dataSerializer=MemberSerializer(data,many=False)
                 realData={'status':True,'message':"Data Got Successfully...",'data':[dataSerializer.data]}
                 return HttpResponse(json.dumps(realData),content_type="application/json")
          except:
               msg={'status':False,'message':"Invalid Phone Number ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def get_all_member(Request):
    
    data=Member.objects.all().order_by('id').reverse()
    if(data):
      dataSerializer=MemberSerializer(data,many=True)
      realData={'status':True,'message':"Data Got Successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
    else:
        msg={'status':False,'message':"No Data Found ..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def update_member(Request):
    if (Request.method=="POST"):
        phone=Request.POST.get('phone')
        try:
            data=Member.objects.get(phone=phone)
            if(data):
                data.name=Request.POST.get('name')
                data.email=Request.POST.get('email')
                data.phone=phone
                data.latitude=Request.POST.get('latitude')
                data.longitude=Request.POST.get('longitude')
                data.save()
                msg={'status':True,'message':"Record Updated Successfully..."}
                jsonData=JSONRenderer().render(msg)
                return HttpResponse(jsonData,content_type="application/json")
        except:
               msg={'status':False,'message':"No Data Found ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")