from django.db import models
from django.utils.functional import cached_property

class Studio(models.Model):
	"""
	Currently only used as a foreign key on bookings
	but can be extended for more functionality
	"""
	pass
	
class Booking(models.Model):
	"""
	Example booking from data source:
	{
	    "studioId": 1,
	    "startsAt": "2019-10-11T03:00:00.000Z",
	    "endsAt": "2019-10-11T06:00:00.000Z"
	}
	"""

	studio = models.ForeignKey('Studio', 
							   on_delete=models.CASCADE,
							   related_name='bookings')
	starts_at = models.DateTimeField()
	ends_at = models.DateTimeField()

	@cached_property
	def duration(self):
		# Return the booking duration as a timedelta object
		return self.ends_at - self.starts_at