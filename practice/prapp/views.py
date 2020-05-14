from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    text_typed = text
    no_blank = len(text.strip())
    word_count = len(text.split())
    return render(request, 'result.html', {
        'total_len' : total_len,
        'text_typed' : text_typed,
        'no_blank' : no_blank,
        'word_count' : word_count,
    })