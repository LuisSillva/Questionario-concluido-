from django import forms

class QuestionarioForm(forms.Form):
    PERGUNTAS_QUALITATIVAS = [
        "Qual é o seu livro favorito?",
        "Qual o seu gênero literário favorito?",
        "Qual foi o último livro que você leu?",
        "Qual foi a última comic/mangá que você leu?",
        "Qual é a sua comic/mangá favorito(a)?",
    ]

    PERGUNTAS_QUANTITATIVAS = [
        "Quantos livros, em média, você lê por mês?",
        "Qual foi o maior número de páginas que você já leu em um único livro?",
        "Quantos livros você comprou nos últimos 6 meses?",
        "Quantos livros você possui?",
        "Quantas páginas você geralmente lê em uma única sessão de leitura?",
    ]

    for i, pergunta in enumerate(PERGUNTAS_QUALITATIVAS):
        locals()[f'pergunta_qualitativa_{i}'] = forms.CharField(label=pergunta, widget=forms.Textarea)

    for i, pergunta in enumerate(PERGUNTAS_QUANTITATIVAS):
        locals()[f'pergunta_quantitativa_{i}'] = forms.IntegerField(label=pergunta)
