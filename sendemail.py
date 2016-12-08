import argparse
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.MIMEText import MIMEText
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sendmail')
    parser.add_argument('-i', '--input', help='Input of domains', required=True)
    args = parser.parse_args()
    input = args.input

with open(input, 'rU') as f:
  lines = f.read().splitlines()

for line in lines:
  # Open a plain text file for reading.  For this example, assume that
  # the text file contains only ASCII characters.
  fp = open("message.txt", 'rb')
  # Create a text/plain message
  msg = MIMEText(fp.read())
  fp.close()

  # me == the sender's email address
  # you == the recipient's email address
  msg['Subject'] = "Action required: Your website "+line+" has been hacked"
  msg['From'] = "info@topcodersonline.com"
  msg['To'] = "info@"+line

  # Send the message via our own SMTP server, but don't include the
  # envelope header.
  s = smtplib.SMTP('localhost')
  s.sendmail(msg['From'], msg['To'], msg.as_string())
  s.quit()
  print line+" sent\n"
