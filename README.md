# Pirate Studios code test

Studio booking API with two endpoints:

- One endpoint that exposes the data source in a paginated format
- One endpoint that calculates the total percentage of time that each studio has been booked for, over the total time span of the data set.


### Prerequisites

Requires Python 3.7, pip3 and virtualenv

### Installing

Clone this repository:

```
git clone git@github.com:beckys57/pirate-studios.git
cd pirate-studios
```

Install Python 3.7: [Instructions](https://realpython.com/installing-python/)

Install pip for Python 3 and create a virtual environment: [Instructions](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Install dependencies:

```
pip3 install -r requirements.txt
```

Load the initial data:

```
python3 manage.py  import_booking_data -f ./initial_data.json
```

Run the server on port 8000:

```
python3 manage.py runserver 8000
```

Make a request with curl or in the browser.

Get booking list for all studios with optional page parameter:
```
curl -X GET http://127.0.0.1:8000/booking/list/?page=3
```

Get percentage of time booked for studio ID 20:
```
curl -X GET http://127.0.0.1:8000/booking/20/percent/
```

## Running the tests

Run with the command:

```
python3 manage.py test booking
```

Note: Tests are incomplete, currently tests the import of data and that the correct response codes are returned from the booking list


## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The REST API framework
* [Pip](https://pypi.org/project/pip/) - Dependency Management

