const fs = require('fs');
const Holidays = require('date-holidays');

//  change these values to generate a different country's holidays, or more years
const COUNTRY_CODE = 'US';
const YEARS_TO_GENERATE = 5;
const FILENAME = 'holiday-config.json';

// generates a holiday object for the given country and years
function generateHolidayConfig(countryCode = COUNTRY_CODE, yearsToGenerate = YEARS_TO_GENERATE, startYear = new Date().getFullYear()) {
  const hd = new Holidays();
  hd.init(countryCode);
  const holidays = {};

  for (let i = 0; i < yearsToGenerate; i++) {
    const year = startYear + i;
    const yearHolidays = hd.getHolidays(year);
    yearHolidays.forEach(({ name, date }) => {
      const [year, month, day] = date.split(' ')[0].split('-');
      const formattedHoliday = {
        title: name,
        date: {
          year, month, day,
        }
      }

      if (!holidays.hasOwnProperty(year)) {
        holidays[year] = [formattedHoliday];
      } else if (!Array.isArray(holidays[year])) {
        console.log(formattedHoliday)
        throw new Error(`Error: Invalid holiday-config.json: holidays[${year}] is not an array`);
      } else {
        holidays[year].push(formattedHoliday);
      }
    });
  }
  return holidays
}

// writes the holiday object to a file
function saveHolidayConfigToDisk(holidays, filename = FILENAME) {
  try {
    if (fs.existsSync(filename)) {
      fs.unlinkSync(filename);
    }
    fs.writeFileSync(filename, JSON.stringify(holidays, null, 2));
  } catch (err) {
    console.error(`Error writing to ${filename}: ${err}`)
  }

  console.log(`Configuration file saved to ${filename}`);
}

const holidays = generateHolidayConfig();
saveHolidayConfigToDisk(holidays);

module.exports = {
  generateHolidayConfig, saveHolidayConfigToDisk
};
