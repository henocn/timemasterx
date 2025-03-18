from datetime import datetime, timedelta

class TimeMasterX:
    """
    TimeMasterX is a class for easily manipulating time and dates.

    Attributes:
    -----------
    date_time : datetime
        The current or manually set date and time.
    format : str
        The format used to display dates and times.

    Methods:
    ----------
    now() -> str :
        Returns the current date and time as a string.
    
    add_time(days=0, hours=0, minutes=0, seconds=0) -> str :
        Adds a time interval to the current date.

    subtract_time(days=0, hours=0, minutes=0, seconds=0) -> str :
        Subtracts a time interval from the current date.

    compare(other_date: str) -> str :
        Compares the current date with another date provided as argument.
    """

    def __init__(self, date_time: str = None, format: str = "%Y-%m-%d %H:%M:%S"):
        """
        Initializes a TimeMasterX object with a specific date or the current date.

        Parameters:
        ------------
        date_time : str, optional
            The date as a string (e.g., "2025-03-18 12:30:45").
            If None, current time is used.
        
        format : str, optional
            Date format used for display and conversion (default "%Y-%m-%d %H:%M:%S").
        """
        self.format = format
        self.date_time = datetime.strptime(date_time, format) if date_time else datetime.now()

    def now(self) -> str:
        """
        Returns the current date and time in the specified format.

        Returns:
        --------
        str : The formatted current date and time.
        """
        return datetime.now().strftime(self.format)

    def add_time(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
        """
        Adds a time interval to the current date.

        Parameters:
        ------------
        days : int, optional
            Number of days to add.
        hours : int, optional
            Number of hours to add.
        minutes : int, optional
            Number of minutes to add.
        seconds : int, optional
            Number of seconds to add.

        Returns:
        --------
        str : The new date after addition.
        """
        self.date_time += timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        return self.date_time.strftime(self.format)

    def subtract_time(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
        """
        Subtracts a time interval from the current date.

        Parameters:
        ------------
        days : int, optional
            Number of days to subtract.
        hours : int, optional
            Number of hours to subtract.
        minutes : int, optional
            Number of minutes to subtract.
        seconds : int, optional
            Number of seconds to subtract.

        Returns:
        --------
        str : The new date after subtraction.
        """
        self.date_time -= timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        return self.date_time.strftime(self.format)

    def compare(self, other_date: str) -> str:
        """
        Compares the current date with another provided date.

        Parameters:
        ------------
        other_date : str
            The date to compare as a string (must follow the same format as `self.format`).

        Returns:
        --------
        str : "Future" if current date is after `other_date`, "Past" if before, "Equal" if identical.
        """
        other = datetime.strptime(other_date, self.format)
        if self.date_time > other:
            return "Future"
        elif self.date_time < other:
            return "Past"
        return "Equal"