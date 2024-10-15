from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from web.models import *



from django.shortcuts import redirect

from django.http import JsonResponse




@login_required(login_url='/login')
def index(request):
    user = request.user
    items = Item.objects.filter(user=user, is_complete=False)
    doneitems = Item.objects.filter(user=user, is_complete=True)

    if request.method == 'POST':
        item_name = request.POST.get('item')

        
        itemn = Item.objects.create(
            name=item_name,
            user=user
        )
        itemn.save()
        
        return HttpResponseRedirect(reverse('web:index'))
    else:
        context = {
            "items": items,
            "doneitems": doneitems,
        }

        return render(request, 'web/index.html', context=context)




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.save()
        return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')

    


def login(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            
            error_message = 'Invalid name or pass.'
    
    return render(request, 'web/login.html', {'error_message': error_message})

    

def logout(request):
    auth_logout(request)

    return HttpResponseRedirect(reverse('web:login'))




@login_required(login_url='/login')
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('web:index'))


@login_required(login_url='/login')
def edit_item(request, id):
    user = request.user
    itemnow = Item.objects.get(id=id, user=user)

    if request.method == 'POST':
        item_name = request.POST.get('item')
        itemnow.name = item_name
        itemnow.save()
        return HttpResponseRedirect(reverse('web:index'))
    else:
        context = {
            'itemnow': itemnow
        }

    return render(request, 'web/index.html', context=context)


@login_required(login_url='/login')
def item_done(request, id):
    item = Item.objects.get(id=id, is_complete=False)
    item.is_complete = True
    item.save()
    
    return HttpResponseRedirect(reverse('web:index'))
