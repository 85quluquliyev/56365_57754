from django.shortcuts import render, redirect
from .models import Domain, Review
from .forms import DomainForm, ReviewForm

def home(request):
    if request.method == 'POST':
        domain_form = DomainForm(request.POST)
        if domain_form.is_valid():
            domain_form.save()
            return redirect('home')
    else:
        domain_form = DomainForm()

    domains = Domain.objects.all()
    return render(request, 'reviews/home.html', {'domain_form': domain_form, 'domains': domains})

def domain_detail(request, domain_id):
    domain = Domain.objects.get(id=domain_id)
    reviews = domain.reviews.all()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('domain_detail', domain_id=domain.id)
    else:
        review_form = ReviewForm(initial={'domain': domain})

    return render(request, 'reviews/domain_detail.html', {'domain': domain, 'reviews': reviews, 'review_form': review_form})
