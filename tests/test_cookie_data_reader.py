import io
import unittest
from datetime import datetime
from typing import Dict, List

from modules.cookie_data_reader import CookieDataParser
from modules.models import CookieLog


class TestCookieFileParser(unittest.TestCase):

    def test_parse_csv_file_correctly(self) -> None:
        test_cases: List[Dict[str, List[CookieLog]]] = [{
            "cookie,timestamp\nAtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\nAtY0laUfhglK3lC8,2018-12-09T14:18:00+00:00":
            [CookieLog(
                cookie="AtY0laUfhglK3lC7", timestamp=datetime.fromisoformat("2018-12-09T14:19:00+00:00")),
             CookieLog(
                cookie="AtY0laUfhglK3lC8", timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00"))]},
            {"": []},
            {"cookietimestampAtY0laUfhglK3lC7": []}]

        for test_case in test_cases:
            for input_data, expected_output in test_case.items():
                fh_bytes = io.BytesIO(str.encode(input_data))
                fh = io.TextIOWrapper(fh_bytes, encoding='utf-8', newline='\n')
                cookie_parser = CookieDataParser(fh)
                result = cookie_parser.parse()

                self.assertCountEqual(result, expected_output)
