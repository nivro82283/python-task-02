"""Choose a random date between two dates entered by the user."""

import datetime
import random


def no_vinnigret(start_date, end_date):
    """
    Return a random date between the given dates, including both ends.

    :param start_date: Start date in YYYY-MM-DD format.
    :param end_date: End date in YYYY-MM-DD format.
    :return: A randomly selected date.
    """
    start = datetime.date.fromisoformat(start_date)
    end = datetime.date.fromisoformat(end_date)

    if start > end:
        raise ValueError("Start date must not be later than end date.")

    days_between = (end - start).days
    random_days = random.randint(0, days_between)
    return start + datetime.timedelta(days=random_days)


def main():
    """Read two dates and display a randomly selected date."""
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        chosen_date = no_vinnigret(start_date, end_date)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print(chosen_date)

    if chosen_date.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    main()
