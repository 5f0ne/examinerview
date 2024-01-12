class Timeline():
    def __init__(self) -> None:
        self.events = []

    def addEvent(self, event):
        obj = {
            "start_date": {},
            "text": {}
        }
        if(event.url != "" or event.caption != ""):
            obj["media"] = {}
            obj["media"]["url"] = event.url
            obj["media"]["caption"] = event.caption

        obj["start_date"]["day"] = event.getDay()
        obj["start_date"]["month"] = event.getMonth()
        obj["start_date"]["year"] = event.getYear()
        obj["start_date"]["hour"] = event.getHour()
        obj["start_date"]["minute"] = event.getMinute()
        obj["start_date"]["second"] = event.getSecond()
        obj["start_date"]["millisecond"] = 0
        obj["start_date"]["display_date"] = event.getTimestampStr()

        obj["text"]["headline"] = event.headline
        obj["text"]["text"] = "<b>Description:</b><br>" + event.description + "<br><b>Source:</b><br> " + event.source + " <br><b>Evidence:</b><br> " + event.evidence

        self.events.append(obj)