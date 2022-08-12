from django.views.generic import ListView

from .models import Form


class FormListView(ListView):
    model = Form
    paginate_by = 10
    
    
    