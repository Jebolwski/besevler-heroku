from django.shortcuts import render
from django.http import request
from django.shortcuts import redirect, render
from .models import Announcement, Contact, IstekOneri, Person,Responser
from .forms import AddForm, IstekOneriForm, RegisterForm, ContactForm, ResponseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.core.paginator import Paginator
from .filters import PersonFilter
# Create your views here.


#!BULUNAMADI (404)
def Bulunamadi(request,exception):
    return render(request,'base/404.html')

#!HATA (500)
def Hata(request):
    return render(request,'base/500.html')
#!LOGIN REGISTER
def CustomLoginView(request):
    
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == "Admin":
            return redirect('admin-home')
        else:
            return redirect('citizen-home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        person = authenticate(
            request, username=username, password=password)

        if person is not None:
            login(request, person)
            messages.success(request, 'Başarıyla giriş yapıldı.')
            if request.user.groups.all()[0].name == "Admin":
                return redirect('admin-home')
            else:
                return redirect('citizen-home')
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı.')

    return render(request, 'base/loginregister/login.html')


def RegisterPersonView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            group = Group.objects.get(name='Citizen')
            form.save().groups.add(group)
            messages.success(request, 'Başarıyla kayıt olundu.')
            return redirect('login')
        else:
            messages.error(request, "Kayıt başarı ile gerçekleştirilemedi.")

    context = {
        'form': form
    }
    return render(request, 'base/loginregister/register.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def AdminHomeView(request):
    persons = Person.objects.all().order_by('-update_time')
    p = Paginator(persons,10)
    page = request.GET.get('page')
    person = p.get_page(page)
    if request.method=='GET':
        myfilter = PersonFilter(request.GET,queryset=persons)
        persons=myfilter.qs
        p = Paginator(persons,10)
        page = request.GET.get('page')
        person = p.get_page(page)
    context = {'persons':person,'persondetails':persons,'myfilter':myfilter}
    return render(request,'base/home.html',context)


#!INBOX
@login_required(login_url='login')
@allowed_users(allowed_roles=['Citizen','Admin'])
def InboxCitizenView(request,user_id):
    messages=Responser.objects.filter(user_id=user_id).order_by('-date')
    context={'text':messages}
    return render(request,'base/inbox/inboxcitizen.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Citizen','Admin'])
def InboxCitizenDeleteView(request,inbox_id):
    text=Responser.objects.filter(pk=inbox_id)
    text.delete()
    return redirect('inbox-citizen',request.user.id)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def InboxAdminView(request):
    messages=Contact.objects.all().order_by('-date')
    context={'text':messages}
    return render(request,'base/inbox/inboxadmin.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def InboxAdminDeleteView(request,inbox_id):
    text=Contact.objects.filter(pk=inbox_id)
    text.delete()
    return redirect('inbox-admin')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def InboxAdminResponseView(request,inbox_id):
    form =ResponseForm()
    if request.method=='POST':
        data = request.POST.copy()
        data['name']=inbox_id
        data['user']=inbox_id
        form=ResponseForm(data)
        if form.is_valid():
            form.save()
            
            messages.success(request,"Cevap başarıyla iletildi.")
            return redirect('inbox-admin')
    context={'form':form}
    return render(request,'base/inbox/inboxadminresponse.html',context)






#!KİŞİ CRUD
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def AddPersonView(request):
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # form.instance.user = 'Jebolwski'
            form.save()
            messages.success(request, 'Kişi başarıyla eklendi.')
            return redirect('admin-home')
    context = {'form': form}
    return render(request, 'base/kisi/addperson.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def LookPersonView(request, pk):
    persons = Person.objects.get(id=pk)
    context = {'persons': persons}
    return render(request, "base/kisi/lookperson.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def EditPersonView(request, pk):
    persons = Person.objects.get(id=pk)
    form = AddForm(instance=persons)

    if request.method == 'POST':
        form = AddForm(request.POST, instance=persons)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kişi başarıyla düzenlendi.')
            return redirect('admin-home')
    context = {'persons': persons, 'form': form}
    return render(request, 'base/kisi/editperson.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def DeletePersonView(request, pk):
    persons = Person.objects.get(id=pk)
    context = {'persons': persons}
    if request.method == 'POST':
        persons.delete()
        messages.success(request, 'Kişi başarıyla silindi.')
        return redirect('admin-home')
    return render(request, 'base/kisi/deleteperson.html', context)


#!DUYURU CRUD
def Duyurular(request):
    duyurular = Announcement.objects.all().order_by('-update_time')
    p = Paginator(duyurular,10)
    page = request.GET.get('page')
    duyuru = p.get_page(page)
    if request.method=='POST':
        arama=request.POST['arama']
        duyurular=Announcement.objects.filter(title__icontains=arama).order_by('-update_time')
        p = Paginator(duyurular,10)
        page = request.GET.get('page')
        duyuru = p.get_page(page)
    context = {'duyurular':duyuru}
    return render(request,'base/duyuru/duyurular.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def DuyuruOlustur(request):
    if request.method == 'POST':
        Announcement.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc'],
        image=request.FILES.get('file'),
        )
        messages.success(request, 'Duyuru başarıyla oluşturuldu.')
        return redirect('duyurular')
        
    return render(request, 'base/duyuru/duyuru-ekle.html')



def DuyuruDetay(request, pk):
    duyuru = Announcement.objects.get(id=pk)
    context = {'duyuru': duyuru}
    return render(request, "base/duyuru/duyuru-detay.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def DuyuruDuzenle(request, pk):
    duyuru = Announcement.objects.get(id=pk)
    context={'duyuru':duyuru}
    if request.method == 'POST':
            duyuru.title=request.POST['title']
            duyuru.desc=request.POST['desc']
            temizle=request.POST.get('temizle')
            if temizle=='on':
                duyuru.image.delete()
            if request.FILES:
                duyuru.image=request.FILES['file']
            duyuru.save()
            messages.success(request, 'Duyuru başarıyla düzenlendi.')
            return redirect('duyurular')
    return render(request, 'base/duyuru/duyuru-duzenle.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def DuyuruSil(request, pk):
    duyuru = Announcement.objects.get(id=pk)
    context = {'duyuru': duyuru}
    if request.method == 'POST':
        duyuru.delete()
        messages.success(request, 'Duyuru başarıyla silindi.')
        return redirect('duyurular')
    return render(request, 'base/duyuru/duyuru-sil.html', context)


#!ÖNERİ VE ŞİKAYET
def OneriVeSikayet(request):
    form = IstekOneriForm()
    if request.method=='POST':
        data = request.POST.copy()
        form=IstekOneriForm(data=data,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Mesaj başarıyla iletilmiştir.")
            return redirect('citizen-home')
    istek=IstekOneri.objects.all().order_by('-update_time')
    context={'istek':istek,'form':form}
    return render(request,'base/oneri/oneri.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def OneriVeSikayetDetay(request,pk):
    istek=IstekOneri.objects.get(id=pk)
    context={'istek':istek}
    return render(request,'base/oneri/oneridetay.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Citizen', 'Admin'])
def OneriVeSikayetSil(request,pk):
    istek=IstekOneri.objects.all().filter(id=pk)
    istek.delete()
    return redirect('onerivesikayet')


#!VATANDAŞ EKRANI
def CitizenHomeView(request):
    duyurular = Announcement.objects.all().order_by('-update_time')
    p = Paginator(duyurular,5)
    page = request.GET.get('page')
    duyuru = p.get_page(page)
    context = {'duyurular':duyuru}
    return render(request, 'base/citizen/citizenhome.html', context)


def CitizenContactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if request.user.is_authenticated:
            form.instance.user = request.user
            
        if form.is_valid():
            form.save()
            messages.success(request,"Mesajınız başarıyla iletildi.")
            return redirect('citizen-contact')

    return render(request, 'base/citizen/citizencontact.html', context={'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Citizen', 'Admin'])
def CitizenSettingsView(request):
    return render(request, 'base/citizen/settings.html')



def bulunamadi(request,exception):
    return render('base/404.html')
