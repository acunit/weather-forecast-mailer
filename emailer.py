import weather
import mailer
import getpass

# Get emails and assign to dictionary
def get_emails():
    # Reading emails from a file
    emails = {}

    # try block to handle problemsif the emails.txt file does not exist. This will allow the program to continue running as normal instead of just crashing.
    try:
        # need to open the emails text file to read from it.
        email_file = open('emails2.txt', 'r')
        # for loop to read each of the lines inthe emails.txt file
        for line in email_file:
            # Need to split up the line into email and name
            # It will take the first portion and assign to email
            # Then it will take the second as assign to name
            (email, name) = line.split(',')
            # Creating entires into our dictionary (key:email : val:name)
            emails[email] = name.strip()

    # Look for the FileNotFoundError and print out the error if it occurs
    except FileNotFoundError as err:
        print(err)

    # return to send the emails dictionary to whoever calls the function.
    return emails


def get_schedule():
    # Reading our schedule from a file
    try:
        # Opening the schedule to read so we can include in the email.
        schedule_file = open('schedule.txt', 'r')
        # assign the contents to schedule variable. .read() takes all content
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule


def main():
    emails = get_emails()

    schedule = get_schedule()

    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, schedule, forecast)


main()
