from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from models import Question
from forms import AskForm, AnswerForm, SignupForm
from django.views.decorators.http import require_POST
from django.forms.models import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


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
    form = AnswerForm(initial={'question': qid})
    form._user = request.user
    return render(request, 'question_details.html', {
        'question': question,
        'form': form
        })


def question_add(request):
    if request.method =='POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        form._user = request.user
    return render(request, 'question-add.html', {
        'form': form
        })

@require_POST
def answer_question(request):
    form = AnswerForm(request.POST)
    form._user = request.user
    if form.is_valid():
        answer = form.save()
        url = answer.question.get_url()
        return HttpResponseRedirect(url)
    else:
        return HttpResponseBadRequest()


def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        form._user = request.user
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form
        })