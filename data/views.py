from django.shortcuts import render
import pandas as pd
from .models import *

def all_data(request):
    all_data = Data.objects.all()
    context = {
        'all_data' : all_data
    }

    return render(request, 'datas.html', context)


def data_show(request,id):

    data = Data.objects.get(id=id)

    df = pd.read_excel(data.file,encoding='utf-8')
    df = df.values.tolist()
    print(df)
    context = {
        'df' : df
    }
    return render (request,'data_show.html', context)