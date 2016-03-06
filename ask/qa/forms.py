from django import forms
from models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        self.cleaned_data['author_id'] = self._user.pk
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean_question(self):
        question_id = self.cleaned_data['question']
        question = Question.objects.get(id=question_id)
        if not question:
            raise forms.ValidationError("Question is not found!")
        self.cleaned_data['question'] = question
        return question

    def save(self):
        self.cleaned_data['author_id'] = self._user.pk
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError('There is another user with that name, sorry.')
        return username

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user