from django.shortcuts import render, redirect
from .forms import QuestionarioForm
from .models import Resposta


def questionario_view(request):
    if request.method == 'POST':
        print("Recebi um POST")
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            print("O formulário é válido")
            for field_name, field_value in form.cleaned_data.items():
                if 'qualitativa' in field_name:
                    pergunta = QuestionarioForm.PERGUNTAS_QUALITATIVAS[int(field_name.split('_')[-1])]
                    Resposta.objects.create(pergunta=pergunta, resposta_texto=field_value)
                elif 'quantitativa' in field_name:
                    pergunta = QuestionarioForm.PERGUNTAS_QUANTITATIVAS[int(field_name.split('_')[-1])]
                    Resposta.objects.create(pergunta=pergunta, resposta_numero=field_value)
            return redirect('questionario_sucesso')
        else:
            print("O formulário não é válido")

    else:
        form = QuestionarioForm()
    
    return render(request, 'questionario_form.html', {'form': form})

def questionario_sucesso(request):
    respostas_qualitativas = Resposta.objects.filter(resposta_texto__isnull=False)
    respostas_quantitativas = Resposta.objects.filter(resposta_numero__isnull=False)
    return render(request, 'questionario_sucesso.html', {'respostas_qualitativas': respostas_qualitativas, 'respostas_quantitativas': respostas_quantitativas})
    # return render(request, 'questionario_sucesso.html')
