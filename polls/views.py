from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
<<<<<<< HEAD
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last three published questions
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        # Excludes any questions that aren't published yet
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
=======
from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
   question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
   return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
   question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
   return render(request, 'polls/results.html', {'question': question})
>>>>>>> 082cfaecc7804e96e9c162db17cbd14c9ce69de8

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

