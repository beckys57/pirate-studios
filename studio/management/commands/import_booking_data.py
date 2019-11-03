import json
import logging
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from booking.models import Booking, Studio

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = """
            Imports JSON booking data
            Expects keys:
            'studioId' as an int
            'startsAt', 'endsAt' in the format YYYY-MM-DDThh:mm:ss.000Z
            """

    def add_arguments(self, parser):
        parser.add_argument('-f',
                            type=str,
                            help="Relative or absolute file path of JSON data")

    def handle(self, *args, **options):
        file_path = options.get('f')
        if not file_path:
            logger.warn('Please provide a file -path to JSON data with the -f option')
            return

        # Read the json file
        with open(file_path) as json_file:
            count = 0
            data = json.load(json_file)
            for booking in data:
                # Create the studio if not already exists
                studio_id = booking['studioId']
                Studio.objects.get_or_create(pk=studio_id)
                # Parse start and end datetimes
                starts_at = datetime.strptime(booking['startsAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                ends_at = datetime.strptime(booking['endsAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                # Save the booking; duplicates can't be valid so check it exists first
                Booking.objects.get_or_create(
                    studio_id=studio_id,
                    starts_at=booking['startsAt'],
                    ends_at=booking['endsAt'],
                    )
                count += 1

        print('Imported {} bookings'.format(str(count)))
