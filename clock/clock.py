class Clock:
    _MINNUTE_DAY = 24 * 60

    def __init__(self, hour: int, minute: int):
        time = (hour * 60 + minute) % self._MINNUTE_DAY
        self._time = time if time >= 0 else self._MINNUTE_DAY + time

    def __repr__(self):
        return '%02d:%02d' % (self._time / 60, self._time % 60)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self._time == other._time

    def __add__(self, minutes):
        return Clock(0, self._time + minutes)

    def __sub__(self, minutes):
        return Clock(0, self._time - minutes)
