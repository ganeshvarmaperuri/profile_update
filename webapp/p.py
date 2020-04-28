from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import AttachForm
# Create your views here.
def MailAttachment(request):
    if request.method=='POST':
        form=AttachForm(request.POST,request.FILES)
        if form.is_valid():
            Name=form.cleaned_data['Name']
            Subject=form.cleaned_data['Subject']
            Email=form.cleaned_data['Email']
            Message=form.cleaned_data['Message']
            ImgAtta=request.FILES['ImgAtta']
            try:
                mail=EmailMessage('got mail form'+str(Email),
                "Name:"+str(Name)+"\n"
                "Subject:"+str(Subject)+"\n"
                "Email:"+str(Email)+"\n"
                "Message:"+str(Message),
                settings.EMAIL_HOST_USER,
                ['ksrajupy@gmail.com','ksubbaraju.tm@gmail.com','pythondjango.in@gmail.com'])
                mail.attach(ImgAtta.name,ImgAtta.read(),ImgAtta.content_type)
                mail.send()
                return HttpResponseRedirect('/GoodBye')
            except:
                return HttpResponse("Sorry Attachment Error..!!")
    else:
        form=AttachForm()
    return render(request,'MyApp/AttachMail.html',{'form':form})

def GoodBye(request):
    return render(request,'MyApp/GoodBye.html')