# Holiday Config Generator

This node project generates a JSON configuration file with the dates of holidays for the next five years in the United States. It uses the date-holidays package to calculate the holidays.

All the python holiday packages were overengineered and/or wrong on US dates. So that's why theres Node in this parent Python project
¯\\\_(ツ)\_/¯

## Installation

To use this project, you will need to have Node.js and npm installed on your machine.

Node.js can be downloaded here.
npm comes bundled with Node.js, but you can check if you have it installed by running npm -v in your terminal.
Once you have Node.js and npm installed, you can install the project's dependencies by running:

```
npm install
```

This will install the required packages listed in the package.json file.

## Usage

To use this project, simply run the following command:

```
npm run generate-config
```

This will generate a file named `holiday-config.json` in the this directory. If the `holiday-config.json` file already exists, it will be deleted and a new file will be created. The file will contain a JSON array with the dates and names of holidays for the next five years.

Move this file up to the parent directory for use with the calendar generator

```
cp holiday-config.json ..
```
