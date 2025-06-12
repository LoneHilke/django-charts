from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Data, Year
from .forms import DataForm, YearForm
 
from rest_framework.views import APIView
from rest_framework.response import Response
 
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartinput/index.html')
    

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
 
    def get(self, request, format = None):
        labels = [
            'January',
            'February', 
            'March', 
            'April', 
            'May', 
            'June', 
            'July'
            ]
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)
    
def new_data(request):
    data = Data.objects.all()
    form = DataForm()
  
    if request.method == 'POST':
      form = DataForm(request.POST)
      if form.is_valid():
        form.save()
      return redirect('/new_data')
      
    context = {'data': data, 'form': form}
    return render(request, 'chartinput/new_data.html', context)

class Chart(APIView):
    authentication_classes = []
    permission_classes = []
 
    def get(self, request, format = None):
        year = Year.objects.all()#filter(item__in__contains = 'year')
        sail = Data.objects.all().values()
        form = YearForm()
        context = {
            #'month': month,
            #'salg': salg,
            'year': year,
            'form':form
        }
        
        month = "Month"
        salg = 'Salg'
        sail ={
                "month":month,
                "Salg":salg,
             }
        return Response(sail)
    
    def post(self, request, *args, **kwargs):
    
        form = YearForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('/')
        
        year = Year.objects.all()
        context = {
        
            'form': form,
            'year': year,
        
        }
        return render(request, 'chartinput/chart.html', context)