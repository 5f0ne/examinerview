import datetime

class Event():
    def __init__(self, timestamp, headline, description, url, caption, evidence, source, formatStr) -> None:
        self.timestamp = self.__processTimestamp(timestamp, formatStr)
        self.headline = headline
        self.description = description
        self.url = url
        self.caption = caption
        self.evidence = evidence
        self.source = source

    def __processTimestamp(self, timestamp, formatStr):
        return datetime.datetime.strptime(timestamp, formatStr)

    def getTimestampStr(self):
        return self.timestamp.strftime("%d.%m.%Y, %H:%M:%S")    
    
    def getDay(self):
        return self.timestamp.day

    def getMonth(self):
        return self.timestamp.month

    def getYear(self):
        return self.timestamp.year

    def getHour(self):
        return self.timestamp.hour

    def getMinute(self):
        return self.timestamp.minute

    def getSecond(self):
        return self.timestamp.second

    def getMilliseconds(self):
        return self.timestamp.microsecond