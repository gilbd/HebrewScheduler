from __future__ import print_function

import datetime
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from pyluach import dates


class GoogleCalenderAPIHandler(object):
    """
    Manage Google Calender's API for events creations
    """

    def __init__(self, scopes, token_path='token.pickle', credentials_path='credentials.json'):
        self.calender_id = 'primary'
        self.client_secrets_file = credentials_path
        self.credentials = None
        self.scopes = scopes
        self.token_path = token_path

        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                self.credentials = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.client_secrets_file, self.scopes)
                self.credentials = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(token_path, 'wb') as token:
                pickle.dump(self.credentials, token)

        self.service = build('calendar', 'v3', credentials=self.credentials)

    def create_events(self, events):
        """
        Create given events in the calendar.
        """

        # Call the Calendar API
        for event in events:
            self.service.events().insert(calendarId=self.calender_id, body=event).execute()
            print(f"Event created in the date: {event['start']['date']}")

    def delete_events(self, desired_dates, summary):
        """
        Delete the events in given dates which fit to event's summary
        """

        # Call the Calendar API
        for date in desired_dates:
            now = datetime.datetime.strptime(str(date.to_pydate()),
                                             '%Y-%m-%d').isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming events in:', now)
            events_result = self.service.events().list(calendarId=self.calender_id, timeMin=now,
                                                       maxResults=10, singleEvents=True,
                                                       orderBy='startTime').execute()
            events = events_result.get('items', [])
            if not events:
                print('No upcoming events found.')
            for event in events:
                if event['summary'] != summary:
                    continue
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                self.service.events().delete(calendarId=self.calender_id, eventId=event['id']).execute()
                print(f"Event deleted in the date: {event['start']['date']}")
