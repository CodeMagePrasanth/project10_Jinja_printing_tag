from django.shortcuts import render

# Create your views here.
def data_render(request):

    d={'anime':'Naruto','episodes':700}

    return render(request,'data_render.html',context=d)