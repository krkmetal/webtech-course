from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, queryset):
    try:
        limit = int(request.GET.get('limit',10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404
    paginator = Paginator(queryset, limit)
    return (paginator, page)

def home(request, *args, **kwargs):
    new_questions = Question.objects.new()
    paginator, page = paginate(request, new_questions)
    paginator.baseurl = reverse('home') + '?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator
    })

def popular(request, *args, **kwargs):
    new_questions = Question.objects.popular()
    paginator, page = paginate(request, new_questions)
    paginator.baseurl = reverse('popular') + '?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator
    })

def question_details(request, qid, *args, **kwargs):
    question = get_object_or_404(Question, id=qid)
    return render(request, 'question_details.html', {
        'question': question,
        })
