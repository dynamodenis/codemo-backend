from django.core.mail import EmailMultiAlternatives
from  django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def send_results(score,quiz,description,questions,status,receiver):
    subject='CodeMo Results'
    text_content=render_to_string('email/results.txt',{'score':score,'quiz':quiz,'description':description,'status':status,'questions':questions})
    html_content=render_to_string('email/results.html',{'score':score,'quiz':quiz,'description':description,'status':status,'questions':questions})
    
    msg=EmailMultiAlternatives(subject,text_content,settings.EMAIL_HOST_USER,[receiver])
    msg.attach_alternative(html_content,'text/html')
    
    msg.send()