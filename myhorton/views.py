from django.shortcuts import render
from myhorton.forms import HortonForm
from myhorton.tasks import hf_calculation
# Create your views here.
def horton_index(request):
    return render(request, 'myhorton/home.html')

def horton_calculation(request):
    valid = False
    if request.method == "POST":
        data_form = HortonForm(request.POST, request.FILES)
        if data_form.is_valid():
            data = data_form.save(commit=False)
            data.save()
            valid = True
            molecule_path = data.molecule.path.encode('ascii','ignore')
            basis_set = data_form.cleaned_data["basis"].encode('ascii', 'ignore')
            alpha = float(data_form.cleaned_data["alpha"])
            beta = float(data_form.cleaned_data['beta'])
            scf = data_form.cleaned_data['scf'].encode('ascii', 'ignore')
            result = hf_calculation.delay(molecule_path, basis_set, alpha, beta, scf)
            context = {
                'data': (result, molecule_path, basis_set, alpha, beta, scf)
                # 'data':data_form.cleaned_data["basis"]
            }
        else:
            context = {
               # 'data':data_form,
                "post": request.POST,
                "file": request.FILES,
            }
    return render(request, 'myhorton/calculation.html', {"valid":valid, "context":context })
