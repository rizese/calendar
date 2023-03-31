# Monthly Calendar Generator 🗓️

This is a Python script that generates an HTML calendar for a given month and year, with a simple CSS style. You can use this script to create printable calendars for personal or business use.

## Installation

1. Make sure you have Python 3 installed on your system.
2. Clone or download this repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt` or `make install` in the project directory.

## Usage

To generate a calendar for the current month, run the `generate_calendar.py` script or `make calendar`:

```bash
python generate_calendar.py
```

or

```bash
make current_calendar
```

This will create an HTML file in the `/calendars` directory, named in the format `<YYYY>-<M>-<Month>-Calendar.html`. These files are git ignored and can be deleted using the `make clean` command.

To generate a monthly calendar for a different time period than the system current, provide the month and year arguments by running the following command:

```bash
python generate_calendar.py <year> <month>
```

Replace `<month>` and `<year>` with the numerical values for the month and year you want to generate the calendar for. If you do not provide both arguments, it will default to the current system month and year as explained above.

For example, to generate a calendar for March 2023, you would run:

```bash
python generate_calendar.py 2023 3
```

This will create an HTML file in the same directory, named `2023-3-March-Calendar.html`. You can open this file in a web browser to view and print the calendar.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
