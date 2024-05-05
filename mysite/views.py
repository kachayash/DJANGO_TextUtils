# create by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):   
    return render(request , 'bootstrap.html')

def analyze(request):

    # get text to index.html mathi and te text ne remove ma add kari chhi  "2 line "
    # Get Request
    # djtext=(request.GET.get('text','default'))
    # r=(request.GET.get('remove','off'))
    # upercase=(request.GET.get('upercase','off'))
    # deletenewline=(request.GET.get('deletenewline','off'))
    # charcount=(request.GET.get('charcount','off'))
    # spaceremover=(request.GET.get('spaceremover','off'))

    djtext=(request.POST.get('text','default'))
    r=(request.POST.get('remove','off'))
    upercase=(request.POST.get('upercase','off'))
    deletenewline=(request.POST.get('deletenewline','off'))
    charcount=(request.POST.get('charcount','off'))
    spaceremover=(request.POST.get('spaceremover','off'))


    # print(r)
    # disc no data  html ma jova mate "line 3"
    # analyzed = djtext
    # check karshe checkboc clicled chhe k nai

    if r == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            # symbol remove karva mate not in atale k j nathi
            if char not in punctuations:
                analyzed = analyzed +char
        params = {'purpose': "Remove Punc" , 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    # #data ne upper case ma karva no

    elif upercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Change to uppercase" , 'analyzed_text':analyzed}        
        return render(request,'analyze.html',params)
    
    #new line delete karshe
    elif deletenewline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': "Remove New line" , 'analyzed_text':analyzed}        
        return render(request,'analyze.html',params)    
   
    
    #space remove 
    elif spaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': "Space Removver" , 'analyzed_text':analyzed}        
        return render(request,'analyze.html',params)  

    #char count
    elif charcount == "on":
        a =0
        for i in djtext:
            a=a+1
        params = {'purpose': "Count" , 'analyzed_text':a}        
        return render(request,'analyze.html',params)  
    