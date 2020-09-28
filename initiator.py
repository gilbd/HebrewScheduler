import argparse
import datetime
from HebrewSchedulerGUI import HebrewSchedulerGUI
from DatesGenerator import DatesGenerator
from GoogleCalenderAPIHandler import GoogleCalenderAPIHandler
from GoogleCalenderEventBuilder import GoogleCalenderEventBuilder
import configuration


class Initiator(object):
    def __init__(self, args, gui_mode=False):
        self.gui_mode = gui_mode
        self.gui = None
        self.dates_gen = None
        self.api_handler = None
        self.event_creator = None
        self.args = args

    def verify_argument(self):
        try:
            datetime.datetime.strptime(self.args.date, configuration.DATE_FORMAT_CODE)
        except ValueError:
            print(f"Incorrect data format, should be {configuration.DATE_FORMAT}")
            return False
        return True

    def bootstrap(self):
        self.dates_gen = DatesGenerator(self.args.number_years)
        self.api_handler = GoogleCalenderAPIHandler(configuration.SCOPES)
        self.event_creator = GoogleCalenderEventBuilder(self.args.event_name,
                                                        self.args.event_desc,
                                                        self.args.event_loc,
                                                        self.args.color)
        if not self.gui_mode:
            self.input_handler(datetime.datetime.strptime(self.args.date, configuration.DATE_FORMAT_CODE),
                               self.args.event_name,
                               self.args.event_desc,
                               self.args.event_loc,
                               self.args.color,
                               self.args.number_years)
        if self.gui_mode:
            self.gui = HebrewSchedulerGUI(self.input_handler)
            self.gui.run_gui()

    def input_handler(self, date, name, desc, loc, color, num_of_years):
        self.dates_gen = DatesGenerator(num_of_years)
        self.event_creator = GoogleCalenderEventBuilder(name,
                                                        desc,
                                                        loc,
                                                        color)
        desired_dates = self.dates_gen(date)
        events = [self.event_creator.generate_event_body(desired_date) for desired_date in desired_dates]
        if not self.args.delete:
            self.api_handler.create_events(events)
        else:
            self.api_handler.delete_events(desired_dates, self.args.event_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', '-d',
                        required=False,
                        default=str(datetime.date.today()),
                        help=f"Desired Gregorian date in the following format: {configuration.DATE_FORMAT}\n"
                             f"Default: today")
    parser.add_argument('--number-years', '-n',
                        required=False,
                        metavar='[1-50]',
                        default=10,
                        type=int,
                        help="Number of years for further calculation")
    parser.add_argument('--event-name', '-e',
                        required=False,
                        default='Event created by HebrewScheduler',
                        type=str,
                        help="The created event's name")
    parser.add_argument('--event-desc', '-de',
                        required=False,
                        default='Event created by HebrewScheduler',
                        type=str,
                        help="The created event's description")
    parser.add_argument('--event-loc', '-l',
                        required=False,
                        default=None,
                        type=str,
                        help="The created event's location")
    parser.add_argument('--delete', '-del',
                        action='store_true',
                        help="if you want to delete the event")
    parser.add_argument('--gui-mode', '-g',
                        action='store_true',
                        help="If this flag set up - use the GUI")
    parser.add_argument('--color', '-c',
                        required=False,
                        metavar='[1-11]',
                        default=5,
                        type=int,
                        help="""
                        The Event's color code from the following map:
                        1 Lavender
                        2 Sage
                        3 Grape
                        4 Flamingo
                        5 Banana
                        6 Tangerine
                        7 Peacock
                        8 Graphite
                        9 Blueberry
                        10 Basil
                        11 Tomato
                        """)
    args = parser.parse_args()
    initiator = Initiator(args, gui_mode=args.gui_mode)
    if initiator.verify_argument():
        initiator.bootstrap()


if __name__ == '__main__':
    main()
