class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        if minutes == 60:
            minutes = 0
            hour += 1
            if hour > 12:
                hour = hour - 12
            
        hour_a = 0.5*(hour*60 + minutes)
        minute_a = 6 * minutes
        a = abs(hour_a - minute_a)
        a = min(360-a,a)
        return a