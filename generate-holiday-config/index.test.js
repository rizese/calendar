const assert = require('assert');
const fs = require('fs');
const { generateHolidayConfig, saveHolidayConfigToDisk } = require('./index');

describe('generateHolidayConfig()', () => {
  let holidays;
  const year = 2023
  const yearString = year.toString();

  beforeEach(() => {
    holidays = generateHolidayConfig('US', 1, year);
  });

  it('returns a non-empty holidays object for the specified year', () => {
    expect(holidays[yearString]).toBeTruthy();
    expect(Object.keys(holidays[yearString]).length).toBeGreaterThan(0);
  });

  it('should generate a holiday object with New Year\'s Day', () => {
    const newYearsDay = holidays[yearString].find(h => h.title === "New Year's Day");
    assert.ok(newYearsDay, 'New Year\'s Day not found');
    assert.strictEqual(newYearsDay.date.month, '01', 'New Year\'s Day is in the wrong month');
    assert.strictEqual(newYearsDay.date.day, '01', 'New Year\'s Day is on the wrong day');
  });

  it('should generate a holiday object with Christmas', () => {
    const christmas = holidays[yearString].find(h => h.title === "Christmas Day");
    assert.ok(christmas, 'Christmas Day not found');
    assert.strictEqual(christmas.date.month, '12', 'Christmas Day is in the wrong month');
    assert.strictEqual(christmas.date.day, '25', 'Christmas Day is on the wrong day');
  });
});

describe('saveHolidayConfigToDisk', () => {
  const filename = 'test-config.json';
  const holidayConfig = { "test": "test" }

  beforeEach(() => {
    if (fs.existsSync(filename)) {
      fs.unlinkSync(filename);
    }
  });

  afterEach(() => {
    if (fs.existsSync(filename)) {
      fs.unlinkSync(filename);
    }
  });

  it('should write the holiday config to a file', () => {
    saveHolidayConfigToDisk(holidayConfig, filename);
    expect(fs.existsSync(filename)).toBe(true);
  });

  it('should write the correct data to the file', () => {
    saveHolidayConfigToDisk(holidayConfig, filename);
    const data = fs.readFileSync(filename);
    expect(JSON.parse(data)).toEqual(holidayConfig);
  });
});
