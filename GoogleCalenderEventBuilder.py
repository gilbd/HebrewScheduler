import datetime


class GoogleCalenderEventBuilder(object):
    def __init__(self, event_name, location=None, desc=None, color=5):
        self.event_name = event_name
        self.location = location
        self.desc = desc
        self.color = color

    def generate_event_body(self, date):
        event = {
            'summary': self.event_name,
            'location': self.location,
            'description': self.desc,
            'colorId': self.color,
            'start': {
                'date': str(date.to_pydate()),
                'timeZone': 'Asia/Jerusalem',
            },
            'end': {
                'date': str((date + 1).to_pydate()),
                'timeZone': 'Asia/Jerusalem',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        return event
