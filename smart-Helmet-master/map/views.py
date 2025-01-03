from django.shortcuts import render

def map_view(request):
    destination = {
        'latitude': 15.8415757,  # Replace with your destination latitude
        'longitude': 74.5346099   # Replace with your destination longitude
    }
    return render(request, 'map.html', {'destination': destination})
