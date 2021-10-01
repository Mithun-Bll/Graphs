from django.shortcuts import render
from django.views.generic import View
import numpy as np
import pandas as pd   
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DataSets
from django.db.models import Count
   
# Create your views here.   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class CreateDataSet(APIView):
    def get(self, request, format = None):
        #import pdb; pdb.set_trace()
        flag = request.query_params.get('fresh')
        message = ""
        if flag=='1':
            dataset = DataSets.objects.all().delete()
            # dataset.save()
        dataset = DataSets.objects.all()
        if len(dataset)==0:
            read_csv = pd.read_csv('adult_dataset.csv')
            csv_data = pd.DataFrame(read_csv)
            for i in csv_data.index:
                age = csv_data.loc[i,'age']
                work = csv_data.loc[i,'work']
                fnlwgt = csv_data.loc[i,'fnlwgt']
                education = csv_data.loc[i,'education']
                education_num = csv_data.loc[i,'education_num']
                marital_status = csv_data.loc[i,'marital_status']
                occupation = csv_data.loc[i,'occupation']
                relationship = csv_data.loc[i,'relationship']
                race = csv_data.loc[i,'race']
                sex = csv_data.loc[i,'sex']
                capital_gain = csv_data.loc[i,'capital_gain']
                capital_loss = csv_data.loc[i,'capital_loss']
                hours_per_week = csv_data.loc[i,'hours_per_week']
                native_country = csv_data.loc[i,'native_country']
                salary = csv_data.loc[i,'salary']
                try:
                    dataset = DataSets(
                        age = age,
                        work = work,
                        fnlwgt= fnlwgt,
                        education = education,
                        education_num = education_num,
                        marital_status= marital_status,
                        occupation = occupation,
                        relationship = relationship,
                        race = race,
                        sex = sex,
                        capital_gain = capital_gain,
                        capital_loss = capital_loss,
                        hours_per_week = hours_per_week,
                        native_country= native_country,
                        salary = salary
                    )
                    dataset.save()
                except Exception as e:
                    print(e)
        if flag=='1':
            dataset = DataSets.objects.all()
            message = "records are deleted and rebuild dataset and created {0} records".format(len(dataset))
        else:
            dataset = DataSets.objects.all()   #This will load all data in "dataset variable"
            message = "{0} records".format(len(dataset))
        
        response = {'data':message}
        return Response(response)


class ChartData(APIView):
    # authentication_classes = []
    # permission_classes = []
   
    def get(self, request, format = None):
        #import pdb; pdb.set_trace()
        counts = pd.DataFrame(DataSets.objects.filter().values('sex'))
        male_count = counts.loc[counts['sex']==' Male'].count()[0]
        female_count = counts.loc[counts['sex']==' Female'].count()[0]
        labels = [
            'Male',
            'Female'
            ]
        chartLabel = "Sex"
        chartdata = [male_count,female_count] 
        data ={
                    "labels":labels,
                    "chartLabel":chartLabel,
                    "chartdata":chartdata
            }
        return Response(data)   



class GraphData(APIView):
    # authentication_classes = []
    # permission_classes = []

    def get(self,request,format = None):
        relationship = pd.DataFrame(DataSets.objects.filter().values('relationship'))
        dataset = relationship.groupby('relationship').size().reset_index(name='count')
        labels, graph_data = [], []
        for i in dataset.index:
            labels.append(dataset.loc[i,'relationship'])
            graph_data.append(dataset.loc[i,'count'])
        GraphLabel = "relationship"
        data = {
                      "labels":labels,
                      "GraphLabel":GraphLabel,
                      "Graphdata":graph_data
        }
        return Response(data)




class PlotData(APIView):
    # authentication_classes = []
    # permission_classes = []

    def get(self,request,format = None):
        race = pd.DataFrame(DataSets.objects.filter().values('race'))
        dataset = race.groupby('race').size().reset_index(name='count')
        labels, plot_data = [], []
        for i in dataset.index:
            labels.append(dataset.loc[i,'race'])
            plot_data.append(dataset.loc[i,'count'])
        PlotLabel = "Race"
        data = {
                      "labels":labels,
                      "PlotLabel":PlotLabel,
                      "Plotdata":plot_data
        }
        return Response(data)

#race = models.CharField(max_length=100,null=True,blank=True)
#relationship = models.CharField(max_length=50,null=True,blank=True)

         # 'January','February', 'March', 'April' 'May',  'June', 'July'
         #5,10, 20, 30, 45]