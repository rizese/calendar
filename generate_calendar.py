import platform
import subprocess
import calendar
import jinja2
import argparse
import datetime
import os
import json
from html2image import Html2Image


# Load holiday_config file
with open('./config/holiday-config.json', 'r') as f:
    holiday_config = json.load(f)

# Set the first day of the week to Sunday (this is not default)
calendar.setfirstweekday(calendar.SUNDAY)

day_template = "<number>{{day_number}}</number><p>{{holiday}}</p>"

unknown_printer = "<Unknown, possibly nonexistent, default printer>"


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


def convert_html_to_image_and_print(filename):
    output_path = '/'.join(filename.split('/')[:-1])
    image_filename = filename.replace('.html', '.png').split('/')[-1]
    hti = Html2Image(output_path=output_path, size=(1150, 800))

    try:
        # Convert HTML to Image
        hti.screenshot(html_file=filename, save_as=image_filename)
        # Print the Image using lpr command
        result = subprocess.check_call(['lpr', image_filename])
        if result != 0:
            raise Exception(
                f"Error occurred while executing 'lpr {image_filename}'")
    except Exception as e:
        print(f"{e}")
        raise


def get_default_printer_name():
    system = platform.system()
    printer_name = unknown_printer
    try:
        if system == "Windows":
            output = subprocess.check_output(
                ["wmic", "printer", "where", "default='true'", "get", "name"], stderr=subprocess.DEVNULL).decode()
            printer_name = output.split("\n")[1].strip()
        elif system == "Linux" or system == "Darwin":
            output = subprocess.check_output(
                ["lpstat", "-d"], stderr=subprocess.DEVNULL).decode()
            printer_name = output.split(":")[1].strip()
        else:
            print(f"Unsupported platform: {system}")
        return printer_name
    except Exception as e:
        print(f"Couldn't find a default printer")
        return printer_name


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

    return filename


def print_calendar(filename):
    user_input = input(f"Do you want to print the file '{filename}'? (y/n): ")
    default_printer_name = get_default_printer_name()

    if default_printer_name == unknown_printer:
        print(f"Error: Couldn't find a printer")
    elif user_input.lower() == 'y':
        try:
            if os.name == 'nt':  # Windows
                os.system(f'print {filename}')
            elif os.name == 'posix':  # Unix-based (e.g., macOS, Linux)
                # convert_html_to_pdf_and_print(filename)
                convert_html_to_image_and_print(filename)
            else:
                raise Exception("Printing is not supported on this platform.")
            print(
                f"Successfully sent to the '{default_printer_name}.")
        except Exception as e:
            print(f"{e}")


# todo - make the argument order flexible
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a monthly calendar in HTML format')
    parser.add_argument('year', type=int, help='The year of the calendar (default: current year)',
                        nargs='?', default=datetime.datetime.now().year)
    parser.add_argument('month', type=int, help='The month of the calendar (1-12) (default: upcoming month)',
                        nargs='?', default=datetime.datetime.now().month + 1)
    args = parser.parse_args()

    usage_message = """Usage:
    python generate_calendar.py [year] [month]

Parameters:
    year (optional): The year of the calendar (default: current year)
    month (optional): The month of the calendar (1-12) (default: upcoming month)
"""

    if not 1 <= args.month <= 12:
        print(
            f"Error: Month must be between 1 and 12. Exiting without calendar generation.\n\n{usage_message}\n")
    elif not 1000 <= args.year <= 9999:
        print(
            f"Error: Year must be 4 digits. Exiting without calendar generation.\n\n{usage_message}\n")
    else:
        calendar_html = generate_calendar(args.year, args.month)
        filename = save_calendar(args.year, args.month, calendar_html)
        print_calendar(filename)
