import json
from django.contrib import messages
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib.auth.hashers import make_password
from store.models import order, product, orderTracker
from . import forms, models
import store
from django.contrib.auth.decorators import login_required



def loginPage(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            user = authenticate(username=uname, password=pas)
            if user is not None:
                login(request, user)
                # messages.success(
                #     request, f'Hello! {uname} You have been logged in')
                return redirect('homepage')
            else:
                messages.error(request, 'Login Failed!')
    return render(
        request, '../templates/login.html', context={'form': form}
    )


@login_required
def logoutPage(request):
    logout(request)
    return redirect('login')


def signupPage(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Woho!!! Registration Successfull!!')
            return redirect('login')
        else:
            print(form.errors)
            messages.error(request, 'Registration failed!')
    return render(request, '../templates/signup.html', context={'form': form})


@login_required
def homePage(request):
    products = product.objects.all()
    params = {'products': products}
    return render(request, '../templates/homepage.html', params)


@login_required
def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        filteredProducts = product.objects.filter(
            category__name__icontains=query)
        params = {'products': filteredProducts, 'query': query}
    else:
        params = {}
    return render(request, '../templates/temp.html', params)


@login_required
def searchURL(request, id):
    products = product.objects.filter(category=id)
    params = {'products': products}
    return render(request, '../templates/temp.html', params)


@login_required
def contact(request):
    form = forms.contactForm(request.POST or None)
    message = 'Contact us'
    return render(request, '../templates/contact.html', context={'form': form, 'message': message})


@login_required
def preview(request, id):
    products = product.objects.filter(id=id)
    params = {'products': products[0]}
    return render(request, '../templates/preview.html', params)


@login_required
def aboutUs(request):
    return render(request, '../templates/aboutus.html')


@login_required
def checkOut(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address1')+' '+request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        itemsJSON = request.POST.get('itemsJSON')
        orders = order(name=name, address=address, phone=phone,
                       city=city, state=state, zip=zip, items_json=itemsJSON)
        orders.save()
        update = orderTracker(orderId=orders.order_id,
                              updateDesc="Order has been placed")
        update.save()
        message = True
        return render(request, '../templates/checkout.html', {'message': message, 'orders': orders})
    return render(request, '../templates/checkout.html')


@login_required
def orderTrack(request):
    if request.method == "POST":
        orderid = request.POST.get("orderId")
        # print(orderId)
        try:
            orders = order.objects.filter(order_id=orderid)
            # print("orders:", orders)
            if len(orders) > 0:
                update = orderTracker.objects.filter(orderId=orderid)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.updateDesc, 'time': item.timestamp})
                    # print("first: "+orders[0].items_json)
                    response = json.dumps(
                        [updates, orders[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as exception:
            # print(exception)
            return HttpResponse("exception")

    return render(request, '../templates/tracking.html')
