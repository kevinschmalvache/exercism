class Clock:
    DAY_MINUTES = 1440

    def __init__(self, hour, minute):

        m = (hour * 60) + minute
        self.minute_of_day = m % Clock.DAY_MINUTES
        
    def __repr__(self):
        #HH:MM
        h = int(self.minute_of_day / 60)
        m = self.minute_of_day % 60
        return f"{h:02}:{m:02}"

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        if minutes < 0:
            raise ValueError("Need a positive value for minutes.")
        
        return Clock(0, self.minute_of_day + minutes)
        

    def __sub__(self, minutes):
        if minutes < 0:
            raise ValueError("Need a positive value for minutes.")

        return Clock(0, self.minute_of_day - minutes)