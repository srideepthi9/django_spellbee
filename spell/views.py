from django.shortcuts import render
from textblob import TextBlob

# Create your views here.
def base(request):
    return render(request,'input.html')

def mispell(request):
    word=request.POST['word']
    convert_word=TextBlob(word)
    corrected_word=convert_word.correct()
    return render(request,'result.html',{'result':corrected_word})

