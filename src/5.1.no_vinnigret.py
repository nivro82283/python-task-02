"""Choose a random date within an inclusive date range."""
import datetime
import random


def no_vinnigret(start_date, end_date):
    """Return a random date; raise ValueError for invalid or reversed dates."""
    start = datetime.date.fromisoformat(start_date)
    end = datetime.date.fromisoformat(end_date)
    if start > end:
        raise ValueError("Start date must not be later than end date.")
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))


no_vinnigrete = no_vinnigret


def main():
    """Read dates and print the selected date and Monday message."""
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    try:
        chosen = no_vinnigret(start, end)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return
    print(chosen)
    if chosen.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    main()
