from django.shortcuts import render
import requests
from .models import *

# Create your views here.
def home(request):
    # this is for initial fetching
    # url = "https://freetestapi.com/api/v1/weathers"
    # response = {}
    # response["response"] = requests.get(url).json()
    response = {}
    response["response"] = Temperature.objects.all()[:10]
    return render(request, "index.html",response)

# these are keys
# id
# city
# country
# latitude
# logintude
# temperature
# weather_desciption
# humidity
# wind_speed
# forecast
