from Article import Article

class Email(Article):
    def color_pair(self):
        return {"text":"WHITE", "back":"BLUE"}

    def get(self):
        return [
                ("Email", "04", "2017-10-19 10:00:00"),
                ("Email", "11", "2017-10-19 10:00:01"),
                ("Email", "16", "2017-10-19 10:00:02"),
                ("Email", "17", "2017-10-19 10:00:03"),
                ("Email", "18", "2017-10-19 10:00:04"),
                ("Email", "19", "2017-10-19 10:00:05"),
                ("Email", "28", "2017-10-19 10:00:09"),
                ("Email", "33", "2017-10-19 10:00:06"),
                ]
