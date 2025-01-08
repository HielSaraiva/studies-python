from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """A página inicial para o registro de aprendizagem"""
    return render(request, 'learning_logs/index.html')

def topics(request  ):
    """"Mostra todos os tópicos"""
    topics = Topic.objects.order_by('date_added')
    content = {'topics':topics}
    return render(request, 'learning_logs/topics.html', content)

def topic(request, topic_id):
    """"Mostra um único tópico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """"Adiciona um novo topico"""
    if request.method != 'POST':
        # Nenhum dado enviado; cria um formulario em branco
        form = TopicForm()
    else:
        # Dados POST enviados; processa os dados
        form = TopicForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # Exibe um formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
        
    
    