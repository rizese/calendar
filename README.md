# Monthly Calendar Generator

This is a Python script that generates an HTML calendar for a given month and year, with a simple CSS style. You can use this script to create printable calendars for personal or business use.

## Installation

1. Make sure you have Python 3 installed on your system.
2. Clone or download this repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt` in the project directory.

## Usage

To generate a calendar, run the `generate_calendar.py` script with the following arguments:

```bash
python generate_calendar.py <month> <year>
```


Replace `<month>` and `<year>` with the numerical values for the month and year you want to generate the calendar for. For example, to generate a calendar for March 2023, you would run:

```bash
python generate_calendar.py 3 2023
```

This will create an HTML file in the same directory, named `calendar_2023_3.html`. You can open this file in a web browser to view and print the calendar.

## Customization

You can customize the CSS style of the calendar by modifying the `style` variable in the `generate_calendar.py` script. You can also modify the HTML template directly if you want to add more content or change the layout of the calendar.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
