import datetime

from django.db.models import F, Sum
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from booking.serializers import BookingSerializer
from booking.models import Booking


class BookingList(views.APIView):
    """
    List all bookings with pagination
    """
    def get(self, request, format=None):
        bookings = Booking.objects.all().order_by('-starts_at')
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


def get_total_time_span():
    """
    Calculate the total time span of all bookings
    """
    earliest = Booking.objects.order_by('starts_at').first()
    latest = Booking.objects.order_by('ends_at').last()
    time_span = latest.ends_at - earliest.starts_at
    return time_span


def get_total_booked_duration(studio_id):
    """
    Calculate the sum total of booking durations for selected studio
    """
    # Get bookings for selected studio
    studio_bookings = Booking.objects.filter(studio_id=studio_id)
    # Calculate total booked time for the studio
    durations = [booking.duration for booking in studio_bookings]
    total_booked_duration = sum(durations, datetime.timedelta())
    return total_booked_duration


@api_view(['GET'])
def percentage_booked(request, studio_id):
    """
    Return the booked times for a studio as a percentage
    of total time span of all bookings
    """
    if request.method == 'GET':
        total_booked_duration = get_total_booked_duration(studio_id)
        time_span = get_total_time_span()
        percentage_booked = (total_booked_duration/time_span) * 100

        data = {
            "studio_id": studio_id,
            "percentage_booked": percentage_booked,
        }
        return JsonResponse(data, status=200)
