from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from foodcatalog.models import Food

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_foods = Food.objects.all().count()
    num_visits= request.session.get('num_visits',0)
    request.session['num_visits']= num_visits+1;
    context = {
        'num_foods': num_foods,'num_visits':num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class FoodListView(generic.ListView):
    model = Food

class FoodDetailView(generic.DetailView):
    model = Food
    

class FoodCreate(CreateView):
    model = Food
    fields = '__all__'
   
from django.db.models import Q
def AddtoDiary(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(foodname__icontains=query) | Q(id__icontains=query)

            results= Food.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'addtodiaryfood.html', context)

        else:
            return render(request, 'addtodiaryfood.html')

    else:
        return render(request, 'addtodiaryfood.html')

  
    
