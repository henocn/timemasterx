import time

class Scheduler:
    """
    A class for scheduling and executing tasks with delays.
    """
    def __init__(self):
        pass

    def delay_task(self, func, delay_seconds):
        """
        Delays the execution of a function for a specified number of seconds.

        Args:
            func: The function to execute
            delay_seconds: The delay in seconds before execution
        """
        time.sleep(delay_seconds)
        func()

    def schedule_task(self, func, delay_seconds):
        """
        Schedules the execution of a function after a specified delay.

        Args:
            func: The function to execute
            delay_seconds: The delay in seconds before execution
        """
        time.sleep(delay_seconds)
        func()
    
    def schedule_task_with_args(self, func, delay_seconds, *args, **kwargs):
        """
        Schedules the execution of a function with arguments after a specified delay.

        Args:
            func: The function to execute
            delay_seconds: The delay in seconds before execution
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
        """
        time.sleep(delay_seconds)
        func(*args, **kwargs)