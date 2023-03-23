import calendar
import jinja2
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Generate an HTML calendar for a given month and year.')
parser.add_argument('month', type=int, help='The month (1-12) to generate a calendar for.')
parser.add_argument('year', type=int, help='The year to generate a calendar for.')
args = parser.parse_args()

# Generate the calendar HTML using Jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template("calendar_template.html")

cal = calendar.monthcalendar(args.year, args.month)
cal_html = template.render(month=calendar.month_name[args.month], year=args.year, cal=cal)

print(cal)

# Write the HTML to a file
with open(f"{args.month}_{args.year}_calendar.html", "w") as f:
    f.write(cal_html)

print(f"Calendar written to {args.month}_{args.year}_calendar.html")
