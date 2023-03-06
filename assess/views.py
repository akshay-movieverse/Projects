from django.shortcuts import redirect, render
from . import calculate,charts

# Create your views here.
def home(request):

    return render(request,"google.html",{'range': range(1,11)})

def eval(request):
    if request.method=="POST":
        sem = int(request.POST["sem"])
        return render(request,"sgpa.html",{'range':range(1,sem+1),'sem':sem})
    else:
        return redirect(home)


def result(request):

    if request.method=="POST": 
        data = request.POST.dict()
        #print(data)
        sg = calculate.sgpaRes(data)
        #print(sg)
        cg = calculate.cgpaRes(sg)
        #print(cg)

        graph_div = charts.plotChart(cg)

        return render(request,"result.html",{"data":cg,'graph_div':graph_div})


    else:
        return redirect(home)