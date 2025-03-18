from datetime import datetime, timedelta

class TimeDuration:
    """
    Class to calculate the duration between two dates/times.
    """

    def __init__(self, start_time: str, end_time: str, format: str = "%Y-%m-%d %H:%M:%S"):
        """
        Initialize the object with a start and end date.

        Args:
            start_time (str): Start date and time.
            end_time (str): End date and time.
            format (str): Date/time format (default: "%Y-%m-%d %H:%M:%S").
        """
        self.start = datetime.strptime(start_time, format)
        self.end = datetime.strptime(end_time, format)

    def duration_seconds(self) -> float:
        """
        Calculate the duration in seconds.

        Returns:
            float: Duration in seconds.
        """
        return (self.end - self.start).total_seconds()

    def duration_minutes(self) -> float:
        """
        Calculate the duration in minutes.

        Returns:
            float: Duration in minutes.
        """
        return (self.end - self.start).total_seconds() / 60

    def duration_hours(self) -> float:
        """
        Calculate the duration in hours.

        Returns:
            float: Duration in hours.
        """
        return (self.end - self.start).total_seconds() / 3600
    
    def duration_days(self) -> float:
        """
        Calculate the duration in days.

        Returns:
            float: Duration in days.
        """
        return (self.end - self.start).total_seconds() / 86400
    
    def duration_weeks(self) -> float:
        """
        Calculate the duration in weeks.

        Returns:
            float: Duration in weeks.
        """
        return (self.end - self.start).total_seconds() / 604800
    
    def duration_months(self) -> float:
        """
        Calculate the duration in months.

        Returns:
            float: Duration in months.
        """
        return (self.end - self.start).total_seconds() / 2592000
    
    def duration_years(self) -> float:
        """
        Calculate the duration in years.

        Returns:
            float: Duration in years.
        """
        return (self.end - self.start).total_seconds() / 31536000

    def complete_duration(self) -> str:
        """
        Calculate and return the complete duration as a string.

        Returns:
            str: Formatted duration with years, months, days, hours, minutes and seconds.
        """
        delta = self.end - self.start
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = delta.days % 30
        hours = delta.seconds // 3600
        minutes = (delta.seconds // 60) % 60
        seconds = delta.seconds % 60
        
        parts = []
        if years > 0:
            parts.append(f"{years} years")
        if months > 0:
            parts.append(f"{months} months")
        if days > 0:
            parts.append(f"{days} days")
        if hours > 0:
            parts.append(f"{hours} hours")
        if minutes > 0:
            parts.append(f"{minutes} minutes")
        if seconds > 0 or not parts:
            parts.append(f"{seconds} seconds")
            
        return ", ".join(parts)