from django.shortcuts import render, redirect
from .models import Domain, Review
from .forms import DomainForm, ReviewForm, SearchForm

def home(request):
    message = ""
    search_results = None

    if 'search' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            name = search_form.cleaned_data['name']
            search_results = Domain.objects.filter(name__icontains=name)
    else:
        search_form = SearchForm()

    if request.method == 'POST':
        domain_form = DomainForm(request.POST)
        if domain_form.is_valid():
            name = domain_form.cleaned_data['name']
            domain, created = Domain.objects.get_or_create(name=name)
            if created:
                message = f'Domain "{name}" başarıyla eklendi.'
            else:
                message = f'Domain "{name}" zaten mevcut.'
            return redirect('home')
    else:
        domain_form = DomainForm()

    domains = Domain.objects.all()
    return render(request, 'reviews/home.html', {
        'domain_form': domain_form,
        'domains': domains,
        'message': message,
        'search_form': search_form,
        'search_results': search_results
    })

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

    return render(request, 'reviews/domain_detail.html', {
        'domain': domain,
        'reviews': reviews,
        'review_form': review_form
    })
