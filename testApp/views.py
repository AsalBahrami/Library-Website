from .models import *
__author__ = 'AsalBahrami'
from .decorators import *
from .filters import *
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.http import  HttpResponseNotFound
from django.contrib.auth.decorators import login_required
UserModel = get_user_model()
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



def homePage(request):
    return render(request, 'Home.html')

# @login_required('/contact')
# @allowed_users(allowed_roles='admin')


def contact(request):
    return render(request,'Contact.html')


#-------apply later
@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def user_creates(request):
    form = ManipulationForm()
    if request.method == 'POST':
        form = ManipulationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,' Datei wurde erfolgreich hinzugefügt!')
        else:
            messages.error(request,'Form ist ungültig')

    return render(
        request,
        'User_cud.html',
        {'form':form}
    )


@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
# @unauth_user
def user_updates(request,pk):
    books = Setup2.objects.get(id=pk)
    form = ManipulationForm(instance=books)
    if request.method == 'POST':
        form = ManipulationForm(request.POST,instance=books)
        if form.is_valid():
            form.save()
            messages.success(request, ' Datensatz wurde erfolgreich aktualisiert!')
        else:
            messages.error(request, 'Form ist ungültig')

    return render(
        request,'User_cud.html',{'form':form})


@login_required(login_url='/login')
def loan(request,pk):

    book = Setup2.objects.get(id=pk)
    current_user = request.user
    if request.method == 'POST':
        bemerkung = request.POST.get('bemerkung')
        # if Setup2.objects.filter(status__exact=''):
        # if Setup2.objects.filter(status__isnull=True):
        if book.entleiher is '' or book.entleiher is None:
            book.entleiher = str(current_user)
            book.entleiher_bem = bemerkung
            book.save()
    context = {'book': book}
    return render(request, 'df.html',context)


@login_required(login_url='/login')
def return_book(request,pk):
    book = Setup2.objects.get(id=pk)
    current_user = request.user
    user_entleiher = book.entleiher
    user_admin = User.objects.filter(groups__name='admin')
    # user_admin = User.objects.filter(groups__name='admin').exists()
    if request.method == 'POST':
        if user_entleiher is not '' or book.entleiher is not None:
            if (user_entleiher == str(current_user))or (current_user in user_admin):
                book.entleiher_bem = ''
                book.entleiher =''
                book.save()

            elif user_entleiher != str(current_user) and (current_user not in user_admin):
                print(user_admin)
                return render(request,'return_denied.html')



    context = {'book': book, 'user':user_entleiher, 'userAdmin':user_admin}
    return render(request, 'returnBook.html', context)



@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def user_deletes(request,pk):
    books = Setup2.objects.get(id=pk)
    if request.method == 'POST':
        books.delete()
    return render(request,'delete.html')


def user_logout(request):
    logout(request)
    return render(request,'Home.html')


# data advance filter func
@login_required(login_url='/login')
def data_filter(request):

    query = Setup2.objects.all()
    filtering = AD_Filter(request.GET or None, queryset=query)
    # filtering = AD_Filter(request.GET, queryset=query)
    filtering = AD_Filter(request.GET, queryset=Setup2.objects.all())
    q = request.GET.get('q')
    submitbutton = request.GET.get('submit')
    form = ManipulationForm()
    auflagen = request.GET.get('auflagen')
    author = request.GET.get('author')
    bemerkung = request.GET.get('bemerkung')
    betreuer = request.GET.get('betreuer')
    dk_kennzeichnung = request.GET.get('dk_kennzeichnung')
    dk_nummer = request.GET.get('dk_nummer')
    dk_etikett_buch = request.GET.get('dk_etikett_buch')
    dk_etikett_andere = request.GET.get('dk_etikett_andere')
    entleiher =request.GET.get('entleiher')
    entleiher_bem = request.GET.get('entleiher_bem')
    erfasserkuerzel = request.GET.get('erfasserkuerzel')
    erscheinungsort = request.GET.get('erscheinungsort')
    inventarnummer = request.GET.get('inventarnummer')
    isbn_nummer = request.GET.get('isbn_nummer')
    sprache = request.GET.get('sprache')
    standort = request.GET.get('standort')
    titel = request.GET.get('titel')
    dokumenttyp = request.GET.get('dokumenttyp')
    verlag = request.GET.get('verlag')
    verlagsnummer = request.GET.get('verlagsnummer')
    zustand = request.GET.get('zustand')
    freies_stichwort = request.GET.get('freies_stichwort')
    medium = request.GET.get('medium')
    merker = request.GET.get('merker')
    erscheinungsdatum = request.GET.get('erscheinungsdatum')

    if sprache != '' and sprache is not None:
        query = query.filter(sprache__icontains=sprache).distinct()

    if erscheinungsdatum != '' and erscheinungsdatum is not None:
        query = query.filter(erscheinungsdatum__icontains=erscheinungsdatum).distinct()

    if bemerkung != '' and bemerkung is not None:
        query = query.filter(bemerkung__icontains=bemerkung).distinct()

    if auflagen != '' and auflagen is not None:
        query = query.filter(auflagen__icontains=auflagen).distinct()

    if betreuer != '' and betreuer is not None:
        query = query.filter(betreuer__icontains=betreuer).distinct()

    if dk_kennzeichnung != '' and dk_kennzeichnung is not None:
        query = query.filter(dk_kennzeichnung__icontains=dk_kennzeichnung).distinct()

    if dk_nummer != '' and dk_nummer is not None:
        query = query.filter(dk_nummer__icontains=dk_nummer).distinct()

    if dk_etikett_buch != '' and dk_etikett_buch is not None:
        query = query.filter(dk_etikett_buch__icontains=dk_etikett_buch).distinct()

    if verlagsnummer != '' and verlagsnummer is not None:
        query = query.filter(verlagsnummer__icontains=verlagsnummer).distinct()

    if dk_etikett_andere != '' and dk_etikett_andere is not None:
        query = query.filter(dk_etikett_andere__icontains=dk_etikett_andere).distinct()

    if entleiher != '' and entleiher is not None:
        query = query.filter(entleiher__icontains= entleiher).distinct()

    if entleiher_bem != '' and entleiher_bem is not None:
        query = query.filter(entleiher_bem__icontains= entleiher_bem).distinct()

    if erfasserkuerzel != '' and erfasserkuerzel is not None:
        query = query.filter(erfasserkuerzel__icontains= erfasserkuerzel).distinct()

    if erscheinungsdatum != '' and erscheinungsdatum is not None:
        query = query.filter(erscheinungsdatum__icontains= erscheinungsdatum).distinct()

    if erscheinungsort != '' and erscheinungsort is not None:
        query = query.filter(erscheinungsort__icontains= erscheinungsort).distinct()

    if inventarnummer != '' and inventarnummer is not None:
        query = query.filter(inventarnummer__icontains= inventarnummer).distinct()

    if isbn_nummer != '' and isbn_nummer is not None:
        query = query.filter(isbn_nummer__icontains= isbn_nummer).distinct()

    if standort != '' and standort is not None:
        query = query.filter(standort__icontains= standort).distinct()

    if verlag != '' and verlag is not None:
        query = query.filter(verlag__icontains=verlag).distinct()

    if dokumenttyp != '' and dokumenttyp is not None:
        query = query.filter(dokumenttyp__icontains=dokumenttyp).distinct()

    if freies_stichwort != '' and freies_stichwort is not None:
        query = query.filter(freies_stichwort__icontains= freies_stichwort).distinct()

    if medium != '' and medium is not None:
        query = query.filter(medium__icontains=medium).distinct()

    if merker != '' and merker is not None:
        query = query.filter(merker__icontains=merker).distinct()

    if zustand != '' and zustand is not None:
        query = query.filter(zustand__icontains=zustand).distinct()

    if titel != '' and titel is not None:
        query = query.filter(titel__icontains=titel).distinct()

    if author != '' and author is not None:
        query = query.filter(author__icontains=author).distinct()

    content = {'query':query,'filtering':filtering,'form':form,'q':q,'submitbutton':submitbutton}
    return render(request,'AdvanceFilter.html',content)




@login_required (login_url='/login')
def return_data(request):
    books = Setup2.objects.all()
    # filter setting
    dataFilter=Setup2Filter(request.GET,queryset=books)
    books = dataFilter.qs
    books = Setup2.objects.order_by('author')
    # pagination setting
    paginator = Paginator(books,13)
    last_page = (paginator.num_pages)

    # request of the page
    page_num = request.GET.get('page')
    # converting to the same type to compare
    pageNumSize = str(page_num)
    lastPageSize = str(last_page)
    try:
        page = paginator.page(page_num)

    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = 1
    except InvalidPage:
        return HttpResponseNotFound("Page not found")
    except TypeError:
        return HttpResponseNotFound("Page not found")
    content = {'books': page, 'dataFilter': dataFilter, 'lastPage': last_page,
               'page_num': page_num}  # 'myFilter':myFilter}

    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')

    if query is not None:
        lookups = Q(titel__icontains=query) | Q(author__icontains=query) | \
                  Q(dokumenttyp__icontains=query) | Q(dk_nummer__icontains=query)\
                    | Q(dk_kennzeichnung__icontains=query)\
                    | Q(auflagen__icontains=query)\
                    | Q(dk_nummer__icontains=query)\
                    | Q(dk_kennzeichnung__icontains=query)\
                    | Q(dk_etikett_buch__icontains=query)\
                    | Q(dk_etikett_andere__icontains=query)\
                    | Q(sprache__icontains=query)\
                    | Q(medium__icontains=query)\
                    | Q(bemerkung__icontains=query)\
                    | Q(betreuer__icontains=query)\
                    | Q(standort__icontains=query)\
                    | Q(erfasserkuerzel__icontains=query)\
                    | Q(erscheinungsdatum__icontains=query)\
                    | Q(erscheinungsort__icontains=query)\
                    | Q(inventarnummer__icontains=query)\
                    | Q(isbn_nummer__icontains=query)\
                    | Q(verlag__icontains=query)\
                    | Q(verlagsnummer__icontains=query)\
                    | Q(entleiher__icontains=query)\
                    | Q(entleiher_bem__icontains=query)\

        results = Setup2.objects.filter(lookups).distinct()
        content = {'results': results,
                   'submitbutton': submitbutton,'books': page, 'dataFilter': dataFilter, 'lastPage': last_page,
                   'page_num': page_num}  # 'myFilter':myFilter}

    return render(request,'Buecher.html',content)


def user_is_already_registered(request):
    #check if the method is post
    if request.method=='POST':
        #grab the username and password and give the user authentication
        username = request.POST.get('username')
        password = request.POST.get('password')
        # making them authenticate
        user = authenticate(request,username=username, password=password)
        # authenticate if user is there
        if user is not None:
            # log this specific user in
            login(request,user)
            # redirect it to home page (change it)
            return render(request,'Home.html')
        if username or password is None:
            messages.error(request,
                          'Benutzername oder Passwort ist falsch')
        else :
            messages.error(request,
                          'Benutzername oder Passwort ist falsch')
    return render(request,'Login2.html')


@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Ihr Passwort wurde aktualisiert')
            return redirect('password')
        else:
            messages.error(request, 'Fehlermeldung! Bitte Eingaben überprüfen')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

