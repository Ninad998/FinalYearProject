from django.shortcuts import render
from models import Result

# Create your views here.

def pred_list(request):
    results = Result.objects.all().order_by('upload_date')
    return render(request, 'blog/pred_list.html', {'results': results})
