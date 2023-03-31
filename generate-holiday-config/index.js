const fs = require('fs');
const Holidays = require('date-holidays');

const hd = new Holidays();

const countryCode = 'US';
const today = new Date();
const currentYear = today.getFullYear();
const yearsToGenerate = 5;
const filename = 'holiday-config.json';


hd.init(countryCode);
const holidays = [];

for (let i = 0; i < yearsToGenerate; i++) {
  const year = currentYear + i;
  const yearHolidays = hd.getHolidays(year);
  yearHolidays.forEach((holiday) => {
    const dateString = holiday.date.split(' ')[0];
    const month = dateString.split('-')[1];
    const day = dateString.split('-')[2];
    holidays.push({
      title: holiday.name,
      date: {
        year,
        month,
        day,
      },
    });
  });
}
fs.unlinkSync(filename); // delete file if it exists
fs.writeFileSync(filename, JSON.stringify(holidays, null, 2));

console.log(`Configuration file saved to ${filename}`);
