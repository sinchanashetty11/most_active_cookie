import argparse
from datetime import datetime

from modules.cookie_data_reader import CookieDataParser
from modules.active_cookie_monitor import ActiveCookieSelector

if __name__ == '__main__':
    # cli parser
    cli_parser = argparse.ArgumentParser(
        prog='CookieFinder',
        usage='Process cookie log file to find the most active cookie in a day.',
        description="Find the most active cookie(s) for a specified day."
    )
    cli_parser.add_argument("file_path", type=argparse.FileType('r', encoding='UTF-8'), help="Path to the cookie log file")
    cli_parser.add_argument("-d", "--date", type=str, required=True, help="Date in the format YYYY-MM-DD")

    args = cli_parser.parse_args()
    input_date = datetime.fromisoformat(args.date).date()

    # application logic
    cookie_parser = CookieDataParser(args.file_path)
    cookie_finder = ActiveCookieSelector(cookie_logs=cookie_parser.parse())
    most_active_cookies = cookie_finder.get_most_active_cookie(input_date)
    print(*most_active_cookies, sep="\n")
