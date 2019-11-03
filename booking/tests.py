from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from booking.models import Booking
from booking.views import BookingList

class StudioBookingTests(TestCase):
	def setUp(self):
		self.factory = APIRequestFactory()

	def test_import_worked(self):
		call_command('import_booking_data', f="initial_data.json")
		self.assertEqual(Booking.objects.all().count(),1060)

	def test_booking_list(self):
		# Check that a get request returns status code 200
		request = self.factory.get(reverse('booking_list'))
		view = BookingList.as_view()
		response = view(request)
		assert response.status_code == 200
		# Check that POST requests are not allowed
		request = self.factory.post(reverse('booking_list'))
		response = view(request)
		assert response.status_code == 405

	def test_pagination(self):
		# Check that page size is 20
		# Check that going to next page provides different data
		pass

	def test_percent_booked(self):
		# With a sample set of data check that the correct % of booked time is returned
		pass