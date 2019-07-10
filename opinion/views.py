from django.shortcuts import render,get_object_or_404
from .models import Opinion,Comment
from django.utils import timezone
from .forms import OpinionForm,CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def opinion_list(request):
	opinions=Opinion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'opinion/opinion_list.html',{'opinions':opinions})
def opinion_detail(request,pk):
	opinion=get_object_or_404(Opinion,pk=pk)
	return render(request,'opinion/opinion_detail.html',{'opinion':opinion})
@login_required
def opinion_new(request):
	if request.method == "POST":
		form = OpinionForm(request.POST)
		if form.is_valid():
			opinion = form.save(commit=False)
			opinion.author = request.user
			#opinion.published_date = timezone.now()
			opinion.save()
			return redirect('opinion_detail', pk=opinion.pk)
	else:
		form = OpinionForm()
	return render(request, 'opinion/opinion_edit.html', {'form': form})
@login_required
def opinion_edit(request, pk):
    opinion = get_object_or_404(Opinion, pk=pk)
    if request.method == "POST":
        form = OpinionForm(request.POST, instance=opinion)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.author = request.user
            #opinion.published_date = timezone.now()
            opinion.save()
            return redirect('opinion_detail', pk=opinion.pk)
    else:
        form = OpinionForm(instance=opinion)
    return render(request, 'opinion/opinion_edit.html', {'form': form})
@login_required
def opinion_draft_list(request):
    opinions = Opinion.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'opinion/opinion_draft_list.html', {'opinions': opinions})
@login_required
def opinion_publish(request, pk):
    opinion = get_object_or_404(Opinion, pk=pk)
    opinion.publish()
    return redirect('opinion_detail', pk=pk)
@login_required
def opinion_remove(request, pk):
    opinion = get_object_or_404(Opinion, pk=pk)
    opinion.delete()
    return redirect('opinion_list')
def add_comment_to_opinion(request, pk):
    opinion = get_object_or_404(Opinion, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.opinion = opinion
            comment.save()
            return redirect('opinion_detail', pk=opinion.pk)
    else:
        form = CommentForm()
    return render(request, 'opinion/add_comment_to_opinion.html', {'form': form})
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('opinion_detail', pk=comment.opinion.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('opinion_detail', pk=comment.opinion.pk)