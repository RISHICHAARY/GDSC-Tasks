from django.shortcuts import render
import smtplib
from django.contrib import messages

def Home(request):
	return render(request,'Home.html',{})
def About(request):
	return render(request,'About.html',{})
def Work(request):
	return render(request,'Works.html',{})
def Contact(request):
	if request.method=="POST":
		Mail=str(request.POST.get("Mail"))
		Subject=str(request.POST.get("Subject"))
		Message=str(request.POST.get("Message"))
		with smtplib.SMTP('smtp.gmail.com',587) as smtp:
			smtp.starttls()
			smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
			sub=Mail+" "+Message
			bod=Subject
			msg=f"subject:{sub}\n\n{bod}"
			smtp.sendmail('manageladen01@gmail.com','rishichaary1903@gmail.com',msg)
		messages.success(request, 'Message Sent  ')
		return render(request,'Contact.html',{})
	else:
		return render(request,'Contact.html',{})