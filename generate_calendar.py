import calendar
import jinja2
import argparse
import datetime
import os
import json

# Load holiday_config file
with open('./holiday-config.json', 'r') as f:
    holiday_config = json.load(f)

# Set the first day of the week to Sunday (this is not default)
calendar.setfirstweekday(calendar.SUNDAY)

day_template = "<number>{{day_number}}</number><p>{{holiday}}</p>"


def day_template_render(day_number, holiday=""):
    formatted_day = f"<number>{day_number}</number><p>{holiday}</p>"
    return formatted_day


def find_holiday_in_config(year, month, day):
    for holiday in holiday_config.get(str(year), []):
        holiday_date = holiday.get("date", {})
        if (holiday_date.get("year") == str(year) and
            holiday_date.get("month") == str(month).zfill(2) and
                holiday_date.get("day") == str(day).zfill(2)):
            return holiday
    return None


def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.get_template('calendar_template.html')
    row_template = env.get_template('row_template.html')

    weeks = []
    for week in cal:
        days = []
        for day in week:
            if day == 0:
                days.append('')
            else:
                holiday = find_holiday_in_config(year, month, day)

                if holiday:
                    days.append(
                        f"<number>{day}</number><p>{holiday['title']}</p>")
                else:
                    days.append(f"<number>{day}</number>")
        weeks.append(row_template.render(days=days))

    calendar_table = template.render(
        weeks=weeks,
        month=calendar.month_name[month],
        year=year
    )

    return calendar_table


def save_calendar(year, month, calendar_table):
    # Create a calendars subdirectory if it doesn't exist
    if not os.path.exists('calendars'):
        os.makedirs('calendars')

    # Save the file in the calendars subdirectory
    filename = f'calendars/{year}-{month}-{calendar.month_name[month]}-Calendar.html'
    with open(filename, 'w') as f:
        f.write(calendar_table)

    print(f'Calendar written to {filename}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a monthly calendar in HTML format')
    parser.add_argument('year', type=int, help='The year of the calendar (default: current year)',
                        nargs='?', default=datetime.datetime.now().year)
    parser.add_argument('month', type=int, help='The month of the calendar (1-12) (default: current month)',
                        nargs='?', default=datetime.datetime.now().month)
    args = parser.parse_args()

    # usage_message = "Usage: \n\
    #         python generate_calendar.py[year][month]\n \
    #     Parameters: \n\
    #         year(optional): The year of the calendar(default: current year) \n\
    #         month(optional): The month of the calendar(1-12)(default: current month)\n"

    usage_message = """Usage:
    python generate_calendar.py [year] [month]

Parameters:
    year (optional): The year of the calendar (default: current year)
    month (optional): The month of the calendar (1-12) (default: current month)
"""

    if not 1 <= args.month <= 12:
        print(
            f"Error: Month must be between 1 and 12. Exiting without calendar generation.\n\n{usage_message}\n")
    elif not 1000 <= args.year <= 9999:
        print(
            f"Error: Year must be 4 digits. Exiting without calendar generation.\n\n{usage_message}\n")
    else:
        calendar_html = generate_calendar(args.year, args.month)
        save_calendar(args.year, args.month, calendar_html)
