from django import forms
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from dddemo.celery import app


class RunItFormDummy(forms.Form):
    arg1 = forms.IntegerField()
    arg2 = forms.IntegerField()


class RunItView(FormView):
    form_class = RunItFormDummy
    template_name = 'runit/runit.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        app.send_task('dddemo.add', args=(
            form.cleaned_data.get('arg1'),
            form.cleaned_data.get('arg2')))
        return super(RunItView, self).form_valid(form)
