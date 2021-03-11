from flask import render_template, request, redirect # ADDED
from app import app
from app.models.events_list import events, add_new_event
from app.models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title = 'Event List', events=events)

@app.route('/events', methods=['POST'])
def create():
    event_name = request.form['name']
    event_description = request.form['description']
    event_date = request.form['date']
    event_number_of_guests = request.form['number_of_guests']
    event_location = request.form['location']

    new_event = Event(event_name, event_description, event_date, event_number_of_guests, event_location)

    add_new_event(new_event)

    return redirect('/events')