from datetime import datetime
import pytz

class TimeZoneManager:
    """A class to manage timezone operations and conversions."""

    def __init__(self, timezone="UTC"):
        """Initialize TimeZoneManager with a specific timezone.
        
        Args:
            timezone (str): The timezone to set (default is "UTC")
        """
        self.timezone = pytz.timezone(timezone)

    def convert(self, date_time, from_tz, to_tz):
        """Convert a datetime from one timezone to another.
        
        Args:
            date_time (str): The datetime string in format "YYYY-MM-DD HH:MM:SS"
            from_tz (str): Source timezone
            to_tz (str): Target timezone
            
        Returns:
            str: Converted datetime string in format "YYYY-MM-DD HH:MM:SS"
        """
        from_zone = pytz.timezone(from_tz)
        to_zone = pytz.timezone(to_tz)

        local_dt = from_zone.localize(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S"))
        return local_dt.astimezone(to_zone).strftime("%Y-%m-%d %H:%M:%S")

    def get_timezone(self):
        """Get the current timezone.
        
        Returns:
            timezone: Current timezone object
        """
        return self.timezone
    
    def set_timezone(self, timezone):
        """Set a new timezone.
        
        Args:
            timezone (str): The timezone to set
        """
        self.timezone = pytz.timezone(timezone)
    
    def current_time(self):
        """Get the current time in the set timezone.
        
        Returns:
            str: Current datetime string in format "YYYY-MM-DD HH:MM:SS"
        """
        return datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S")
    
    def list(self):
        """Get a list of all available timezones.
        
        Returns:
            list: List of all timezone strings
        """
        return pytz.all_timezones
    
    def info(self, timezone):
        """Get information about a specific timezone.
        
        Args:
            timezone (str): The timezone to get information about
            
        Returns:
            timezone: Timezone object
        """
        return pytz.timezone(timezone)