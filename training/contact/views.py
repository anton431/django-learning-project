from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactView(CreateView):
    model = Contact
    from_class = ContactForm
    success_url = "/"
    fields = '__all__'