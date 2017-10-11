# weather-forecast-mailer

This is a python project which is a mailer that sends the forecast and schedule to a list of emails

## Getting Started

See below for what you need in order to use the code in this repository.

### Prerequisites

1. Make sure Python 3 is installed on your machine.
(I was using Python version 3.6.3)

2. Make sure the requests module is installed on your machine.

3. Get an API key from openweathermap.org by signing up on their site.

### Setting Up

1. Create a file in the root directory of the repository named emails2.txt

2. Inside the file, add emails addresses and names separated by a comma. For example:

  ```
  email.one@test.com, Person one
  email.two@test.com, Person two
  email.three@test.com, Person three
  ```

3. Create a file in the root directory of the repository named schedule.txt

4. Inside the file, add a schedule in the same format as below. For example:
  ```
  Hiking - 9:00am
  Taco Lunch - 12:00pm
  Surfing - 2:00pm
  Happy Hour - 5:00pm
  ```

5. It would also be a good idea to create a config.py file. Inside this file you will want to store two things:
  ```
  openweathermap_app_id = "YOUR_APP_ID"
  my_email_address = 'YOUR_EMAIL_ADDRESS'
  ```

6. be sure to include a .gitignore and ignore the files I mentioned about.

## Notes

1. In the mailer.py file, edit the message to whatever you would like to send.