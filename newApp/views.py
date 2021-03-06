from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User
# from .forms import AddAlumniForm
from django.views.generic import View
from .filters import AlumniFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, 'home.html')


def AlumniListView(request):
    total = User.objects.filter(Verified=True).filter(is_alumni=True).all()
    alfilter = AlumniFilter(request.GET, queryset=total)
    template_name = 'showalumni.html'
    paginator = Paginator(alfilter.qs, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, template_name, {'filter': alfilter, 'page_obj': page_obj})


class AlumniDetailView(View):
    def get(self, request, *args, **kwargs):
        alumni = get_object_or_404(User, pk=kwargs['pk'])
        context = {'alumni': alumni}
        return render(request, "alumni.html", context)



 
    
    