from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FeedbackCreateForm
from .models import Feedback
from .utils import get_client_ip


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = 'Спасибо за отзыв!'
    template_name = 'feedback.html'
    extra_context = {'title': 'Контактная форма'}
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            if self.request.user.is_authenticated:
                feedback.user = self.request.user
        return super().form_valid(form)
