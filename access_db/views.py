import json
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import redis
from rest_framework import permissions
from .models import Term, HocPhan
from .serializers import TermSerializer, HocPhanSerializer
from django.core.cache import cache
import random
# Create your views here.


redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)

class TermView(APIView):
    
    #1. List all
    
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('searchTerm')
        if search_term == None:
            terms = Term.objects.all()
        else:
            terms = Term.objects.filter(name__contains=search_term)
        serializer = TermSerializer(terms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class HocPhanView(APIView):
    # List all
    
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        result = redis_instance.get('all')
        if result:
            return Response(json.loads(result), status=status.HTTP_200_OK)
        else:
            hocphans = HocPhan.objects.all()
            serializer = HocPhanSerializer(hocphans, many=True)
            json_data = json.dumps(serializer.data)
            redis_instance.set('all',json_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClearCache(viewsets.ViewSet):
    def cleanCache(self, request, *args, **kwargs):
        result = redis_instance.delete('all')
        data = {
            "success" : True,
            "data": result
        }
        return Response(data=data)
    
class LoadData(viewsets.ViewSet):
    def loadData(self, request, *args, **kwargs):
        terms = Term.objects.all()
        serializer = TermSerializer(terms, many=True)
        print(len(serializer.data))
        for record in serializer.data:
            cache.set(record['class_id'], record)
        return Response(serializer.data[1])
    def getTerm(self, request, *args, **kwargs):
        term_code = request.GET.get("term-code")
        print(term_code)
        data = cache.get(term_code)
        print(data)
        if data != None:
            return Response(data)
        else:
            return Response({
                "success": False
            })
class MultiConnect(viewsets.ViewSet):
    def connectDB(self, request, *args, **kwargs):
        terms = Term.objects.all()
        serializer = TermSerializer(terms, many=True)
        number_student = request.GET.get('number-student')
        for i in range(int(number_student)):
            term = random.choice(serializer.data)
            myTerm = Term.objects.get(id=int(term['id']))
            quantity = term['quantity']
            registered = term['registered']
            if registered < quantity:
                myTerm.registered = myTerm.registered + 1
                myTerm.save()
        return Response(serializer.data)
    def connectRedis(self, request, *args, **kwargs):
        all_key = cache.keys('*')
        number_student = request.GET.get('number-student')
        for stu in range(int(number_student)):
            term_code = random.choice(all_key)
            term = cache.get(term_code)
            quantity = term['quantity']
            registered = term['registered']
            if quantity > registered:
                term['registered'] = term['registered'] + 1
                cache.set(term_code, term)
            print(term)
            print(type(term))
        return Response({'success': term})
    
