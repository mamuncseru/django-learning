import challenges
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.


# def january(request):
#     return HttpResponse("This is January!")

# def february(request):forword_month
#     return HttpResponse("This is february...")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day.")

monthly_challenges = {
    "january": 'Eat no meat for the entire month',
    "february": 'Walk for at least 20 minutes',
    "march": 'Learn Django for at least 20 minutes every day!',
    "april": 'Learn python for at least 20 minutes every day!',
    "May": 'Learn Javascript for at least 20 minutes every day!',
    "june": 'Learn php for at least 20 minutes every day!',
    "july": 'Learn c for at least 20 minutes every day!',
    "august": 'Learn c++ for at least 20 minutes every day!',
    "september": 'Learn java for at least 20 minutes every day!',
    "october": 'Learn tensorflow for at least 20 minutes every day!',
    "november": 'Learn pytorch for at least 20 minutes every day!',
    "december": 'Learn Kotlin for at least 20 minutes every day!',
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]

    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

