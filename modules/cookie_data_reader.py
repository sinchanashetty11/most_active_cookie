import csv
from datetime import datetime
from io import TextIOWrapper
from typing import List

from .models import CookieLog


class CookieDataParser:
    """
    A class to represent a single cookielog.
    CookieDataParser: is used to parse the cookies log file and map the data into interal list of CookieLog type.
    ...

    Attributes
    ----------
    file : TextIOWrapper
        csv text data read from the cli file arg.
    -------
    
    """

    def __init__(self, file: TextIOWrapper) -> None:
        self.file = file

    def parse(self) -> List[CookieLog]:
        '''parse(self) -> List[CookieLog]:
        Parse the csv data and return a list of system know CookieLog objest.'''

        file_data = self.file.read()
        csv_reader = csv.reader(file_data.split("\n"))
        next(csv_reader)  # skip the titles row

        cookie_logs = [
            CookieLog(
                cookie=row[0],
                timestamp=datetime.fromisoformat(row[1])
            ) for row in csv_reader
        ]
        self.file.close()
        return cookie_logs
