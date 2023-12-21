from django.shortcuts import render,redirect
from django.http import HttpResponse
from libapp.models import Book
from libapp.models import IssueBooks


# Create your views here.

def homepage(request):
    return render(request,'home.html')

def adminlogin(request):
        
            return redirect('/admn')
    
        


    






def addbook(request):
    #return render(request,'addbook.html')
    if request.method == 'POST':
        name=request.POST['bname']
        cat=request.POST['cat']
        author=request.POST['author']
        price=request.POST['amt']
        status=request.POST['status']

        p=Book.objects.create(name=name,cat=cat,author=author,price=price,status=status)
        print(p)
        p.save()
        return redirect('/admn')
        #return HttpResponse("record successfully inserted")

    else:
        print("GET request in POST section")
        return render(request,'addbook.html')



def adminpage(request):
    qset=Book.objects.all()
    content={}
    content['data']=qset
    return render(request,'admin.html',content)

def delete(request,rid):
    p=Book.objects.filter(id=rid)
    p.delete()
    return redirect('/admn')

def edit(request,rid):

    if request.method == 'POST':
        name=request.POST['bname']
        cat=request.POST['cat']
        author=request.POST['author']
        price=request.POST['amt']
        status=request.POST['status']

        p=Book.objects.filter(id=rid)
        p.update(name=name,cat=cat,author=author,price=price,status=status)
        return redirect('/admn')

    else:
        p=Book.objects.filter(id=rid)
        content={}
        content['data']=p
        return render(request,'edit.html',content)



def Issuebook(request):
    if request.method == 'POST':
        Student_name=request.POST['sname']
        #Student_id=request.POST['sid']
        book_name=request.POST['bname']
        Issue_date=request.POST['idate']

        p=IssueBooks.objects.create(Student_name=Student_name,book_name=book_name,issued_date=Issue_date)
        p.save()
        return redirect('/issuedbook')
        #return HttpResponse("record successfully inserted")
    
    else:
        print("get request in post section")
        return render(request,'issue_book.html')


    #return render(request,'issue_book.html')


def Issued_book(request):
    iset=IssueBooks.objects.all()
    content={}
    content['data']=iset
    return render(request,'issued_book.html',content)


def deleteissuebook(request,rid):
    p=IssueBooks.objects.filter(id=rid)
    p.delete()
    return redirect('/issuedbook')

def statfilter(request,sf):
    p=Book.objects.filter(status=sf)
    content={}
    content['data']=p
    return render(request,'admin.html',content)

def catfilter(request,cf):
    p=Book.objects.filter(cat=cf)
    content={}
    content['data']=p
    return render(request,'admin.html',content)


