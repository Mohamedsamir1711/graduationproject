from django.shortcuts import render
from .models import Ftable
from .models import Stable
from django.http import JsonResponse
import numpy as np
# from .ml_model import predict



def patients(request):
   patientsinfo1 = Ftable.objects.all()
   patientsinfo2 = Stable.objects.all()
   print(patientsinfo1)
   print(patientsinfo2)
   return render(request, 'patients/patients.html' ,{'Ftable':patientsinfo1,
    'Stable': patientsinfo2 })
   
   # my_app/views.py

# def predict_view(request):
#     if request.method == 'POST':
#         # Example: input from form or JSON
#         input_values = request.POST.getlist('inputs[]')  # e.g. [5.1, 3.5, 1.4, 0.2]
#         input_data = np.array([input_values], dtype=np.float32)  # Ensure shape (1, n)

#         result = predict(input_data)

#         return JsonResponse({'prediction': result.tolist()})
#     return JsonResponse({'error': 'POST request required'})
