from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Logistics
from random import randint


class LandingPage(View):
    def get(self, request):
        template_name = "logistics/landingpage.html"
        return render(request, template_name, context={})
        

    def post(self, request):
        senders_name = request.POST["senders_name"]
        senders_phone_number = request.POST["senders_phone_number"]
        senders_email = request.POST["senders_email"]
        pick_up_city = request.POST["pick_up_city"]
        pick_up_state = request.POST["pick_up_state"]

        receivers_name = request.POST["receivers_name"]
        receivers_phone_number = request.POST["receivers_phone_number"]
        receivers_email = request.POST["receivers_email"]


        destination_city = request.POST["destination_city"]
        destination_state = request.POST["destination_state"]
        item = request.POST["item"]
        tracking_id = randint(10000000000, 100000000000)

        import random

        number_list = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 4500, 9500, 3400]

        delivery_fee = random.choice(number_list)


        Logistics.objects.create(senders_name=senders_name, senders_phone_number=senders_phone_number ,senders_email=senders_email, pick_up_city=pick_up_city,
        pick_up_state = pick_up_state, receivers_name=receivers_name,
        receivers_phone_number=receivers_phone_number, receivers_email=receivers_email,
        destination_city=destination_city, destination_state=destination_state,
        item=item, tracking_id=tracking_id, delivery_fee=delivery_fee
        )
        messages.success(request, "Item has been booked for shipping from {} to {} your tracking id is {} and delivery fee is ₦ {}".format(pick_up_state, destination_state, tracking_id,delivery_fee))
        return redirect("logistics:landing")

