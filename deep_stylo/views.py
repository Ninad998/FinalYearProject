# coding=utf-8
from models import Result
from django.shortcuts import render, get_object_or_404, redirect
from forms import QueryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def pred_list(request):
    results = Result.objects.all().order_by('upload_date')
    return render(request, 'deep_stylo/pred_list.html', {'results': results})

@login_required
def query_new(request):
    form = QueryForm()
    if request.method == "POST":
        form = QueryForm(request.POST.copy())
        if form.is_valid():
            query = form.save(commit=False)
            query.user = request.user
            query.save()
            return redirect('pred_list')
    else:
        form = QueryForm()
    return render(request, 'deep_stylo/query_edit.html', {'form': form})

@login_required
def query_remove(request, pk):
    query = get_object_or_404(Result, pk=pk)
    if query.completed != 1.0:
        query.delete()
    return redirect('pred_list')
