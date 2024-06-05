import pywhatkit as pyw

def get_time_and_format():
  """Prompts the user for desired time format (12 or 24) and individual time components.

  Returns:
    A tuple containing the desired format (string) and a dictionary with hour, minute, and second (int).
  """
  format = input("Enter desired time format (12 or 24): ")
  while format not in ("12", "24"):
    format = input("Invalid format. Please enter 12 or 24: ")

  hour = int(input("Enter hour (0-23 for 24-hour, 1-12 for 12-hour): "))
  if format == "24":
    while hour < 0 or hour > 23:
      hour = int(input("Invalid hour. Please enter a value between 0 and 23: "))
  else:
    while hour < 1 or hour > 12:
      hour = int(input("Invalid hour. Please enter a value between 1 and 12: "))

  minute = int(input("Enter minute (0-59): "))
  while minute < 0 or minute > 59:
    minute = int(input("Invalid minute. Please enter a value between 0 and 59: "))

  # Second is not used by pywhatkit.sendwhatmsg, so we'll omit it
  # second = int(input("Enter second (0-59): "))  # Commented out

  return format, {"hour": hour, "minute": minute}

def convert_to_desired_format(time_dict, format):
  """Converts the time components to the desired format (12-hour or 24-hour).

  Args:
    time_dict: A dictionary containing hour and minute (int).
    format: A string representing the desired format ("12" or "24").

  Returns:
    A string representing the converted time in the desired format (HH:MM).
  """
  hour = time_dict["hour"]
  minute = time_dict["minute"]

  if format == "12":
    if hour == 0:
      hour_str = "12"
      am_pm = "AM"
    elif hour > 12:
      hour_str = str(hour - 12)
      am_pm = "PM"
    else:
      hour_str = str(hour)
      am_pm = "AM"
    time_string = f"{hour_str:02}:{minute:02} {am_pm}"
  else:
    time_string = f"{hour:02d}:{minute:02d}"

  return time_string

# Main program flow
format, time_info = get_time_and_format()
converted_time = convert_to_desired_format(time_info, format)

print(f"The converted time in {format}-hour format is: {converted_time}")

number = input("Enter the number (including country code) You want to send the message to: ")
message = input("Enter the Message You want to send: ")

try:
  # Schedule the message using pywhatkit.sendwhatmsg
  pyw.sendwhatmsg(number, message, time_info["hour"], time_info["minute"])
  print("Message scheduled successfully!")
except Exception as e:
  print(f"An error occurred: {e}")
  print("**Please ensure you have WhatsApp Web open and logged in.**")
