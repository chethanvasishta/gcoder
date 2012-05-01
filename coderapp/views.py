# Create your views here.
from django.shortcuts import render_to_response
from coderapp.models import Challenge

def index(request):
	return render_to_response("coderapp/index.html")

def challenges(request):
	challenge_list = Challenge.objects.all()
	return render_to_response("coderapp/challenges.html", {'challenge_list':challenge_list})

def challenge(request, challenge_id):
	challenge = Challenge.objects.get(pk=challenge_id)
	return render_to_response("coderapp/challenge.html", {'challenge':challenge})
