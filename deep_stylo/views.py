from django.shortcuts import render
from models import Result
from forms import QueryForm

# Create your views here.

def pred_list(request):
    results = Result.objects.all().order_by('upload_date')
    return render(request, 'deep_stylo/pred_list.html', {'results': results})

def query_new(request):
    form = QueryForm()
    return render(request, 'deep_stylo/query_edit.html', {'form': form})
