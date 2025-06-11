from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest 
from rest_framework.decorators import api_view 
from rest_framework.generics import RetrieveUpdateDestroyAPIView
import json
import joblib
from rest_framework import viewsets 
from rest_framework.pagination import PageNumberPagination
from .management.commands.models import Result
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .serializers import ResultSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    
class ResultDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ResultSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    
    def get_queryset(self):
        # Make sure you return a valid queryset
        return Result.objects.all()

class ResultPagination(PageNumberPagination):
    page_size = 8


class OpenApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        reports = Result.objects.all()  # استعلام قاعدة البيانات
        serializer = ResultSerializer(reports, many=True, context={'request': request})  # تحويلها إلى JSON
        return Response(serializer.data) 

@csrf_exempt 
def show_reports(request):
   if request.method == 'POST':
    try:
     age = float(request.POST.get('Age'))
     sex = float(request.POST.get('Sex'))
     chestPainType = float(request.POST.get('ChestPainType'))
     restingBP = float(request.POST.get('RestingBP'))
     cholesterol = float(request.POST.get('Cholesterol'))
     fastingBS = float(request.POST.get('FastingBS'))
     restingECG = float(request.POST.get('RestingECG'))
     maxHR = float(request.POST.get('MaxHR'))
     exerciseAngina = float(request.POST.get('ExerciseAngina'))
     oldpeak = float(request.POST.get('Oldpeak'))
     st_slope = float(request.POST.get('ST_Slope'))
     heartdisease = float(request.POST.get('Heartdisease'))  # Field name made lowercase.
     patientid = float(request.POST.get('Patientid'))  # Field name made lowercase.
     timestep = float(request.POST.get('Timestep'))  # Field name made lowercase.
     heartrate = float(request.POST.get('Heartrate'))  # Field name made lowercase.
     bloodpressure = float(request.POST.get('Bloodpressure'))  # Field name made lowercase.
     oxygensaturation = float(request.POST.get('Oxygensaturation'))
     
     featurelist = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR',
                     'ExerciseAngina', 'Oldpeak', 'ST_Slope','Heartdisease','Patientid','Timestep','Heartrate','Bloodpressure','Oxygensaturation']
        
     print([age, sex , chestPainType, restingBP, cholesterol, fastingBS, restingECG, maxHR,
                     exerciseAngina, oldpeak, st_slope, heartdisease, patientid,timestep,heartrate, bloodpressure,oxygensaturation])
     
    #  prediction = round(model.predict([featurelist])[0])
            
            # Return prediction as JSON response
    #  checks = {
    #             'Check Result': prediction
    #         }
     return render(request,'Show Reports/show_reports.html')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
   else:

    return render(request,'Show Reports/show_reports.html')

@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def result_list(request, format=None):
    if request.method == 'GET':
        
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        try:
            
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
        
        
        serializer = ResultSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        else:
            
            return JsonResponse(serializer.errors, status=400)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def result_detail(request, pk, format=None):
    try:
        result = Result.objects.get(pk=pk)
    except Result.DoesNotExist:
        return JsonResponse({'error': 'Result not found'}, status=404)

    if request.method == 'GET':
       
        serializer = ResultSerializer(result)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")

        serializer = ResultSerializer(result, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        result.delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=204)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
