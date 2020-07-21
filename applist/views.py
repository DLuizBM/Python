# http://pythonclub.com.br/class-based-views-django.html
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .models import Reservation
from .forms import ReservationForm


class ReservationView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ReservationView, self).get_context_data(**kwargs)
        context['Reservation'] = Reservation.objects.all()
        return context


class NewReservation(FormView):
    template_name = 'reservation.html'
    success_url = '/'
    form_class = ReservationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


"""

def NewReservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()
            form = ReservationForm()
        else:
            pass
    else:
        form = ReservationForm()

    context = {
        'form': form
    }
    return render(request, 'reservation.html', context)

"""