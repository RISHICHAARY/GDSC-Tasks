from django.shortcuts import render
import sqlite3
from datetime import date
from django.contrib import messages
con=sqlite3.connect('Posts.db',check_same_thread=False)
curs=con.cursor()
de=date.today()
fg=de.strftime("%Y-%m-%d")
curs.execute("create table if not exists Details(Name varchar(30),Email varchar(50),Subject varchar(100),Body varchar(1000),date date)")
con.commit()
def Home(request):
	curs.execute("select * from Details")
	nm=[]
	em=[]
	sb=[]
	bd=[]
	dt=[]
	final=[]
	ad=curs.fetchall()
	for i in range(0,len(ad)):
		nm1=ad[i][0]
		em1=ad[i][1]
		sb1=ad[i][2]
		bd1=ad[i][3]
		dt1=str(ad[i][4])
		dit={'Name':nm1,'Email':em1,'Subject':sb1,'Body':bd1,'Date':dt1}
		final.append(dit)
	return render(request,'Main.html',{'dict':final})
def Post(request):
	Name=str(request.POST.get("Name"))
	Email=str(request.POST.get("Email"))
	Subject=str(request.POST.get("Subject"))
	Body=str(request.POST.get("Body"))
	Date=fg
	if request.method=="POST":
		if((Name!= None) and (Email!=None) and (Subject!=None) and (Body!=None)):
			curs.execute("insert into Details values('{}','{}','{}','{}','{}')".format(Name,Email,Subject,Body,Date))
			con.commit()
			messages.success(request, 'Blog Posted')
			return render(request,'Sub.html',{})
		else:
			pass
	else:
		return render(request,'Sub.html',{})
# Create your views here.
