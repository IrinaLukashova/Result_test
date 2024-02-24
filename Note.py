import datetime
import json


class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "date": self.date}
        )


def from_json(json_string):
    data = json.loads(json_string)
    note = Note(data["id"], data["title"], data["body"], data["date"])
    return note


