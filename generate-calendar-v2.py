import calendar
import jinja2
import argparse

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
        print(weeks)
        weeks.append(row_template.render(days=days))
    calendar_table = template.render(weeks=weeks, month=calendar.month_name[month], year=year)

    filename = f'{calendar.month_name[month]}_{year}_calendar.html'
    with open(filename, 'w') as f:
        f.write(calendar_table)

    print(f'Calendar written to {filename}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a monthly calendar in HTML format')
    parser.add_argument('year', type=int, help='The year of the calendar')
    parser.add_argument('month', type=int, help='The month of the calendar (1-12)')
    args = parser.parse_args()

    generate_calendar(args.year, args.month)
