import calendar
import jinja2
import argparse
import datetime
import os

calendar.setfirstweekday(calendar.SUNDAY)


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
                days.append(str(day))
        weeks.append(row_template.render(days=days))

    calendar_table = template.render(
        weeks=weeks,
        month=calendar.month_name[month],
        year=year
    )

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
                        default=datetime.datetime.now().year)
    parser.add_argument('month', type=int, help='The month of the calendar (1-12) (default: current month)',
                        default=datetime.datetime.now().month)
    args = parser.parse_args()

    print(args.year.length)

    if not 1 <= args.month <= 12:
        print('Error: Month must be between 1 and 12. Exiting without calendar generation.')
    elif not 1000 <= args.year <= 9999:
        print('Error: Year must be 4 digits. Exiting without calendar generation.')
    else:
        generate_calendar(args.year, args.month)
