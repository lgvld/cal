import os
import sys
import time

import bottle
import ics
import requests
import yaml

#------------------------------------------------------------------------------

CALDAV_URL = "https://cal.ufr-info-p6.jussieu.fr:443/caldav.php/"
CALDAV_USERNAME = "student.master"
CALDAV_PASSWORD = "guest"

SMSAPI_URL = ""

DIR_DATA = "data/"
DIR_ICS = DIR_DATA + "ics/"

#------------------------------------------------------------------------------

def update_ics_file(master, if_older_than):
    if master in MASTERS.keys():
        ics_file = DIR_ICS + master + ".ics"
        if not os.path.isfile(ics_file) or os.path.getmtime(ics_file) + if_older_than < time.time():
            with open(ics_file, "w+") as ics_file_:
                ics_file_.write(requests.get(CALDAV_URL + MASTERS[master] + "/" + master, auth=(CALDAV_USERNAME, CALDAV_PASSWORD)).text)

# def update_everything():
#     for master in MASTERS:
#         update_ics_file(master, 0)

def get_coming_events(ics_file, gap_before=3600):
    with open(ics_file, "r") as ics_file_:
        events = [e for e in ics.Calendar(ics_file_).events if e.begin.timestamp >= time.time() - gap_before]
    return events

#------------------------------------------------------------------------------

@bottle.route("/static/<file:path>")
def static(file):
    return bottle.static_file(file, root="static")

@bottle.route("/")
def index():
    return bottle.template("masters", MASTERS=MASTERS)

@bottle.route("/<masters>")
def masters_events(masters):
    events = []
    for master in list(set(masters.split("+"))):
        update_ics_file(master, 3600 * 2)
        ics_file = DIR_ICS + master + ".ics"
        events += get_coming_events(ics_file)
        events.sort(key=lambda e: e.begin.timestamp)
    return bottle.template("events", master=master, events=events)

@bottle.route("/sms")
def sms():
    if SMSAPI_URL is not None:
        return "SMS envoyé ;-)"
    return ""

#------------------------------------------------------------------------------

application = bottle.default_app()

if __name__ == "__main__":
    with open(DIR_DATA + "masters.yml", "r") as yml_file:
        MASTERS = yaml.safe_load(yml_file)
    bottle.run(port=8080, debug=True, reloader=True)
    # bottle.run(port=80, debug=True)
