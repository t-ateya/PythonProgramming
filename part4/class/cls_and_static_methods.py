"""
    Static Methods
    - A function in a class that can never be bound to any object when called

    class Circle:
        @staticmethod
        def help():
            return 'help available'


    -A class method will always be bound to the class and never the instance

    class MyClass:
        def hello():
            print('hello_)
        
        def inst_hello(self):
            print(f'hello from {self})

        @classmethod
        def cls_hello(cls):
            print(f'hello from {cls})

"""

import datetime
from time import timezone



class TimerError(Exception):
    """A custom exception used for Timer class"""
class Timer:
    tz = timezone.utc 

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    def start(self):
        self._time_start = self.current_dt_utc()
        self._time_end = None 

    def stop(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before it can be stopped')
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        if self._time_end is None:
            raise TimerError("Time has not been stopped.")
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped.')
        return self._time_end.astimezone(self.tz)

    @property
    def elasped(self):
        if self._time_start is None:
            raise TimerError("Timer must be started before an elapsed time can be calculated.")
        if self._time_end is None:
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            elapsed_time = self._time_end - self._time_start
        return elapsed_time.total_seconds()

from time import sleep

t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f"Start time: {t1.start_time}")
print(f"End time: {t1.end_time}")