from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Location  # Import your Location model
from django.utils import timezone
import json


@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Ensure 'device_id', 'latitude', 'longitude' are present in the JSON data
            device_id = data.get('device_id')
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if not all([device_id, latitude, longitude]):
                raise KeyError("Required fields missing")

            # Try to get the existing location by device_id
            location, created = Location.objects.get_or_create(
                device_id=device_id,
                defaults={
                    'latitude': latitude,
                    'longitude': longitude,
                    'timestamp': timezone.now()
                }
            )

            if not created:
                # If location already exists, update its fields
                location.latitude = latitude
                location.longitude = longitude
                location.timestamp = timezone.now()
                location.save()

            return JsonResponse({'success': True})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': f'Invalid JSON: {e}'}, status=400)
        except KeyError as e:
            return JsonResponse({'success': False, 'error': f'Missing key: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Error: {e}'}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

def get_locations(request):
    device_id = request.GET.get('device_id')
    if device_id:
        locations = Location.objects.filter(device_id=device_id).order_by('-timestamp')
    else:
        locations = Location.objects.all().order_by('-timestamp')

    location_list = [
        {'latitude': loc.latitude, 'longitude': loc.longitude, 'device_id': loc.device_id, 'timestamp': loc.timestamp.strftime("%Y-%m-%d %H:%M:%S")}
        for loc in locations
    ]
    return JsonResponse(location_list, safe=False)


def index(request):
    devices = Location.objects.values_list('device_id', flat=True).distinct()
    return render(request, 'location/index.html', {'devices': devices})
