# Swasthik created file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     s=''' Navigation Bar <br> </h2>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>'''
#     return HttpResponse(s)

# def about(request):
#     return HttpResponse('''<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">DJANGO CODE WITH HARRY''')


def index(request):
    # return HttpResponse("Home")
    # params={"name":"spa","place":"india"}
    return render(request, 'index.html')
# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("removepunc")
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("new line remover")
# def spaceremover(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("count character")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    nlremover = request.POST.get('nlremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    print(removepunc)
    print(djtext)
    # analyzed=djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == 'on':
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'remove punctuation', 'analyzed_text': analyzed}
        djtext=analyzed
    if fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to upper case', 'analyzed_text': analyzed}
        djtext=analyzed
    if nlremover=='on':
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params = {'purpose': 'Remove newliner', 'analyzed_text': analyzed}
        djtext=analyzed
    if spaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if djtext[index]==' 'and djtext[index+1]==' ':
                continue
            else:
                analyzed=analyzed+char
        params = {'purpose': 'Remove Extra space', 'analyzed_text': analyzed}
    if(removepunc != 'on' or spaceremover!='on' or nlremover!='on' or fullcaps!='on'):
        return HttpResponse("ERROR")
    

    # return HttpResponse("removepunc")
    return render(request, 'analyze.html', params)
