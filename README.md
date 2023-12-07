# Tokyo restaurants Google maps display - API

A simple Flask API to return list of Tokyo restaurants.
WIP!

## Installation

### Setting up the app

Set up a virtual environment using:

```
python -m venv env
source env/bin/activate # to activate the venv
```

Then install dependencies:

```
pip install -r requirements.txt
```

## Running the API

Before starting the app, set the ENV variable manually:

```
export FLASK_ENV=development
```

Make sure to have generated a Google API Key giving you access to Google Maps services (Maps Javascript API at least) and to enable those services via the Google console.

Create a .env file with the content:

```
GOOGLE_PLACES_API_KEY=<YOUR_GOOGLE_API_KEY>
```

Then, simply run:

```
flask run
```

If you'd like to activate the debugger in dev mode (recommended while developping locally):

```
flask run --debug
```
