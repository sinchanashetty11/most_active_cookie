import unittest
from typing import Dict, List, Tuple

from datetime import datetime
from modules.models import CookieLog

from modules.active_cookie_monitor import ActiveCookieSelector


class TestActiveCookieFinder(unittest.TestCase):

    def test_calculate_most_active_cookie(self) -> None:
        test_cases: List[Dict[List[CookieLog], Tuple[str]]] = [
            {
                (
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:19:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:17:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00")
                    )
                ): [
                    "AtY0laUfhglK3lC7"
                ]
            },
            {
                (
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:19:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:17:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00"))
                ): [
                    "AtY0laUfhglK3lC7",
                    "AtY0laUfhglK3lC8"
                ]
            },
            {
                (
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-11T14:19:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-12T14:17:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-03T14:18:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-05T14:18:00+00:00"))
                ): [
                    "No logs found"
                ]
            },
            {
                (): ["No logs found"]
            }
        ]

        for test_case in test_cases:
            for input_logs, expected_output in test_case.items():
                find_cookie = ActiveCookieSelector(input_logs)
                result = find_cookie.get_most_active_cookie(datetime.fromisoformat("2018-12-09T14:19:00+00:00").date())
                self.assertCountEqual(result, expected_output)
