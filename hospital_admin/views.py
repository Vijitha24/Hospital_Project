from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.urls import reverse

from hospital_admin.models import HospitalAdmin,AdminManagement,Article
from doctor import models as doctor_models
from base import models as base_models
from patient import models as patient_models
from .forms import HospitalAdminForm,ArticleForm
from django.db.models import Sum


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Article added successfully!")  # Success message
            return redirect('hospital_admin:article_list')  # Redirect to the article list after saving
        else:
            messages.error(request, "Failed to add the article. Please correct the errors below.")  # Error message
    else:
        form = ArticleForm()
    return render(request, 'hospital_admin/add_article.html', {'form': form})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'hospital_admin/article_list.html', {'articles': articles})

@login_required
def dashboard(request):
    total_doctors = doctor_models.Doctor.objects.count()
    doctors_list = doctor_models.Doctor.objects.all()
    total_patients = patient_models.Patient.objects.count()
    total_bill_amount = base_models.Billing.objects.aggregate(total=Sum('total'))['total'] or 0
    services = base_models.Service.objects.all()
    appointments = base_models.Appointment.objects.select_related('patient', 'doctor', 'service')

    context = {
        'total_doctors': total_doctors,
        'doctors_list': doctors_list,
        'total_patients': total_patients,
        'total_bill_amount': total_bill_amount,
        'services': services,
        'appointments': appointments,
    }
    return render(request, 'hospital_admin/dashboard.html', context)
def hospital_admin_list(request):
    admins = HospitalAdmin.objects.all()  # Use the correct model
    return render(request, 'hospital_admin/hospital_admin_list.html', {'admins': admins})

@login_required
def profile(request):
    if request.method == "POST":
        form = HospitalAdminForm(request.POST)
        if form.is_valid():
            # Save the admin profile
            hospital_admin = form.save(commit=False)
            hospital_admin.user = request.user  # Assuming this is linked to the logged-in user
            hospital_admin.save()
            return HttpResponseRedirect(reverse('hospital_admin_list'))
    else:
        form = HospitalAdminForm()
    return render(request, 'hospital_admin/create_hospital_admin.html', {'form': form})

