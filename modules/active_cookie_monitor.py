from datetime import date
from typing import Dict, List
from collections import defaultdict
from .models import CookieLog


class ActiveCookieSelector:
    """
    This class represents the activity of cookies on a specific date.
    ActiveCookieSelector utilizes the data parsed from CookieDataParser to determine the most active cookies for each given date.
    ...

    Attributes
    ----------
    cookie_logs : List[CookieLog]
        A list containing CookieLog objects representing cookie activities.

    """

    def __init__(self, cookie_logs: List[CookieLog]) -> None:
        self.cookie_logs = cookie_logs
        self.cookies_activities_per_day: Dict[date, Dict[CookieLog, int]] = {}
        self.most_active_cookies_per_day: Dict[date, Dict[int, List[CookieLog]]] = {}

        self.__process_logs()
        self.compute_daily_cookie_activity()

    def __process_logs(self) -> None:

        '''
        Parses the list of CookieLog objects to calculate the activities per day. The result is stored in the form of
        a dictionary where each date maps to a dictionary containing CookieLog objects and their corresponding activity counts.'''

        for i in self.cookie_logs:
            log_date = i.timestamp.date()
            if log_date not in self.cookies_activities_per_day.keys():
                self.cookies_activities_per_day[log_date] = defaultdict(int)
            self.cookies_activities_per_day[log_date][i.cookie] += 1
            
    def compute_daily_cookie_activity(self) -> None:

        '''
        Iterate over each date and its corresponding cookie logs to find the most active cookies.
        Store the list of most active cookies for each date in the class attribute.'''
        for log_date, cookielogs in self.cookies_activities_per_day.items():
            max_occurrences = max(cookielogs.values())
            most_active_cookies = []
            for cookie, occurrences in cookielogs.items():
                if occurrences == max_occurrences:
                    most_active_cookies.append(cookie)
            self.most_active_cookies_per_day[log_date] = most_active_cookies

    def get_most_active_cookie(self, log_date: date) -> List[str]:

        """If no logs are found for the specified date, return a message indicating so."""

        return self.most_active_cookies_per_day.get(log_date, ["No logs found"])
