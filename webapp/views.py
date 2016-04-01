from django.shortcuts import render
from django.http import HttpResponse
from webapp.forms import SaddleForm
from webapp.tasks import saddle_find_ts

def webapp_index(request):
    return render(request, "webapp/saddle_home.html")    
    #return HttpResponse("<h2>Hey!</h2>")

def select_ic(request):
    valid = False
    if request.method == "POST":
        data_form = SaddleForm(request.POST, request.FILES)
        if data_form.is_valid():
            data = data_form.save(commit=False)
            data.save()
            valid = True
            reactant_path = data.reactant.path.encode('ascii','ignore')
            product_path = data.product.path.encode('ascii', 'ignore')
            ratio = float(data.ratio)
            if data.auto_ic == u'on':
                autoic = True
            else:
                autoic = False
            result = saddle_find_ts.delay(reactant_path, product_path, ratio, autoic)
            context ={
                'pk': data.pk,
                'result':result.id,
            }

        else:
            context = {
                # 'reactant': data_form.reactant,
                # 'product': data_form.product,
                # 'ratio': request.FILES,
                'post': data_form.fields
            }
    return render(request, 'webapp/select_ic.html', {"valid":valid, "context":context})        

