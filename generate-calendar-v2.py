import calendar
import jinja2
import argparse

calendar.setfirstweekday(calendar.SUNDAY)

def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.get_template('calendar_template.html')

    # no phantom html ['\n \n \n \n \n \n \n ...
    # weeks = generate_week(year=year, month=month, week_index=0)

    weeks = []
    for i in enumerate(cal):
      weeks.append(generate_week(year=year, month=month, week_index=i[0]))

    calendar_table = template.render(weeks=weeks, month=calendar.month_name[month], year=year)

    filename = f'{year}-{calendar.month_name[month]}-Calendar.html'
    with open(filename, 'w') as f:
        f.write(calendar_table)

    print(f'Calendar written to {filename}')

def generate_week(year, month, week_index):
    cal = calendar.monthcalendar(year, month)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    row_template = env.get_template('row_template.html')

    week = cal[week_index]

    days = []
    for day in week:
        if day == 0:
            days.append('')
        else:
            days.append(str(day))

    return row_template.render(days=days)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a monthly calendar in HTML format')
    parser.add_argument('year', type=int, help='The year of the calendar')
    parser.add_argument('month', type=int, help='The month of the calendar (1-12)')
    args = parser.parse_args()

    generate_calendar(args.year, args.month)
