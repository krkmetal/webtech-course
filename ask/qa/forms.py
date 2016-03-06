from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question



class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.HiddenInput())

    def clean_question(self):
        question_id = self.cleaned_data['question']
        question = Question.objects.get(id=question_id)
        if not question:
            raise forms.ValidationError("Question is not found!")
        self.cleaned_data['question'] = question
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer