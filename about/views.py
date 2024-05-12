from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView
from .models import *
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


# Account Utils
def go_back(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class HomeView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'


def agency(request, slug):
    agent = get_object_or_404(Agent, slug=slug)
    context = {'agent': agent}
    return render(request, 'agency-single.html', context)


def connect(request):
    
    state_inp = request.GET.get('state')
    search_inp = request.GET.get('q')

    if search_inp:
        search_inp = search_inp.lower().strip()
    if state_inp and state_inp.lower() == 'all nigeria':
        state_inp = None

    categories = Category.objects.all()
    category = Category(id=1)
    # category = get_object_or_404(Category, slug=slug)

    results = []

    # get results from search input with tags
    for service in Agent.objects.all():
        search_tags = service.get_search_tags()
        search_inp_tags = str(search_inp).split()
        if duplicate_count(search_tags, search_inp_tags):
            results.append(service.id)

    if search_inp and not state_inp:
        services = Agent.objects.filter(id__in=results).order_by('name')
    elif state_inp and not search_inp:
        state = get_object_or_404(State, name=state_inp)
        services = Agent.objects.filter(states__id=state.id).order_by('name')
    elif state_inp and search_inp:
        all_state = get_object_or_404(State, name='All Nigeria')
        state = get_object_or_404(State, name=state_inp)
        state_results = [all_state.id, state.id]

        services = Agent.objects.filter(states__in=state_results, id__in=results).order_by('name')
    else:
        services = Agent.objects.all().order_by('name')

    page_count = 12
    paginator = Paginator(services, page_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    states = State.objects.all().order_by('-priority')
    context = {'states': states,'categories': categories, 'category': category,
               'services': services, 'page_obj': page_obj, 'page_count': page_count}
    return render(request, 'agency-list.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    slug_results = []
    # get results from search input with tags
    for service in Agent.objects.all():
        search_tags = service.get_tags()
        # print('\n\nSearch Tags:', slug, search_tags, slug in search_tags)
        if slug.replace('-', '_') in search_tags:
            slug_results.append(service.id)

    services = Agent.objects.filter(id__in=slug_results).order_by('name')

    # Form handling
    state_inp = request.GET.get('state')
    search_inp = request.GET.get('q')

    if search_inp:
        search_inp = search_inp.lower().strip()
    if state_inp and state_inp.lower() == 'all nigeria':
        state_inp = None

    results = []

    # get results from search input with tags
    for service in services:
        search_tags = service.get_search_tags()
        search_inp_tags = str(search_inp).split()
        if duplicate_count(search_tags, search_inp_tags):
            results.append(service.id)

    if search_inp and not state_inp:
        services = Agent.objects.filter(id__in=results).order_by('name')
    elif state_inp and not search_inp:
        state = get_object_or_404(State, name=state_inp)
        services = Agent.objects.filter(id__in=slug_results, states__id=state.id).order_by('name')
    elif state_inp and search_inp:
        all_state = get_object_or_404(State, name='All Nigeria')
        state = get_object_or_404(State, name=state_inp)
        state_results = [all_state.id, state.id]

        services = Agent.objects.filter(states__in=state_results, id__in=results).order_by('name')

    page_count = 4
    paginator = Paginator(services, page_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = category.children.all()
    states = State.objects.all().order_by('-priority')
    context = {'states': states, 'category': category, 'categories': categories,
               'services': services, 'page_obj': page_obj, 'page_count': page_count}
    return render(request, 'agency-list.html', context)


def sub_category(request, category, slug):
    category = get_object_or_404(Category, slug=slug)
    state_inp = request.GET.get('state')
    search_inp = str(request.GET.get('q')).lower()
    # Add code to filter input
    if search_inp:
        search_inp = search_inp.lower().strip()
    if state_inp and state_inp.lower() == 'all nigeria':
        state_inp = None

    if search_inp and not state_inp:
        services = Agent.objects.filter(name=search_inp).order_by('name')
    elif state_inp and not search_inp:
        state = get_object_or_404(State, name=state_inp)
        services = Agent.objects.filter(states__id=state.id).order_by('name')
    elif state_inp and search_inp:
        state = get_object_or_404(State, name=state_inp)
        services = Agent.objects.filter(states__id=state.id, name=search_inp).order_by('name')
    else:
        services = Agent.objects.all().order_by('name')

    paginator = Paginator(services, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    states = State.objects.all()
    context = {'states': states, 'category': category, 'services': services, 'page_obj': page_obj}
    return render(request, 'agency-list.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def pricing(request):
    price1 = get_object_or_404(Pricing, id=1)
    context = {'price1': price1}
    return render(request, 'pricing.html', context)


def store(request):
    categories = Category.objects.all()
    services = Agent.objects.all().order_by('name')
    context = {'categories': categories, 'services': services}
    return render(request, 'store.html', context)
    # return render(request, 'find-agencies.html', context)


def add_review(request):
    form = request.POST

    # if form.is_valid():
    #     data = form.cleaned_data
    print(form)
    owner = get_object_or_404(Agent, id=form['inputowner'])
    name = form['inputname']
    email = form['inputemail']
    message = form['inputmessage']
    position = form['inputposition']
    status = 0
    rating = form['inputrating']
    new_review = Review(owner=owner, name=name, email=email, message=message, status=status, rating=rating, position=position)
    new_review.save()
    return go_back(request)
