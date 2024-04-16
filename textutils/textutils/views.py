# i have created this project Prince
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>Hello, Prince<h1>
#      <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt"> Node Js by prince </a>                  ''')

# def about(request):
#     return HttpResponse("Hello Prince jaiswal This is about")

def index(request):
    
    return render(request,'index.html')
    # return HttpResponse("Home")

def analyze(request):
   djtext=request.GET.get('text','default')
   removepunc=request.GET.get('removepunc','off')
   print(removepunc)
   print(djtext)
   if removepunc=="on":
        punctuations ='''!()-[]{};:'"\,<>./?@#$%^*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
   else:
       return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("new line remove first")
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("capitalize first")

