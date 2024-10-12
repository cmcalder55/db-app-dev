from datetime import datetime, timedelta, timezone

def current_date():
    return datetime.now(timezone.utc)

def time_until_midnight_utc(pull_date, p= "%Y-%m-%d %H:%M:%S"):
    # Get the current datetime in UTC
    now_utc = current_date()

    # Get tomorrow's date
    tomorrow_date = (now_utc + timedelta(days=1)).date()
    # Create a datetime object for midnight of tomorrow's date in UTC
    midnight_utc_tomorrow = datetime.combine(tomorrow_date, datetime.min.time(), timezone.utc)
    # Calculate the time difference between now and midnight
    time_until_midnight = midnight_utc_tomorrow - now_utc
    print(f"Time until midnight UTC: {time_until_midnight}")

    if datetime.strptime(pull_date, p).date() != now_utc.date():
        return False
    return True

# Example usage
print(time_until_midnight_utc("2024-02-24 17:34:22"))

def go(json_data):

    if not json_data:
        json_data = {} # get from tsc

    pull_date = json_data["date"]

    # now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    now_utc = current_date().strftime("%Y-%m-%d %H:%M:%S")

    if now_utc != pull_date.split()[0]:
        json_data = {} # get from tsc

    return json_data


