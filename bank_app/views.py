# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from .models import District, Branch, Material
# from .forms import AccountForm
# # Create your views here.

#
#
#
# def account_registration(request):
#     districts = District.objects.all()
#     materials = Material.objects.all()
#
#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect to a success page
#     else:
#         form = AccountForm()
#
#     return render(request, 'registration_form.html', {'form': form, 'districts': districts, 'materials': materials})
#
# def get_branches(request):
#     district_id = request.GET.get('district_id')
#     branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
#     return JsonResponse(list(branches), safe=False)
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import District, Branch, Material
from .forms import AccountForm


def index(request):
    return render(request, 'index.html')


def account_registration(request):
    districts = District.objects.all()
    materials = Material.objects.all()

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.district = District.objects.get(pk=request.POST.get('district'))
            account.branch = Branch.objects.get(pk=request.POST.get('branch'))
            account.save()
            return redirect('after_reg')  # Redirect to a success page
    else:
        form = AccountForm()

    return render(request, 'registration_form.html', {'form': form, 'districts': districts, 'materials': materials})

def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)


def new_index(request):
    return render(request, 'new_index.html')


def after_reg(request):
    return render(request, 'after_reg.html')