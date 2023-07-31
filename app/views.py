from django.shortcuts import render

# Create your views here.
def data_render(request):

    d={'anime':'Naruto','episodes':700}

    return render(request,'data_render.html',context=d)

def conditional(request):

    d={'a':1000,'b':233,'c':200,'anime':['natruo','attack on titans']}
    return render(request,'conditional.html',context=d)