from Article import Article

class Email(Article):
    def color_pair(self):
        return {"text":"WHITE", "back":"BLUE"}

    def get(self):
        print("Email::get")

        timeline = [
                ("Email", "04"),
                ("Email", "11"),
                ("Email", "16"),
                ("Email", "17"),
                ("Email", "18"),
                ("Email", "19"),
                ("Email", "28"),
                ("Email", "33"),
                ]
        return timeline
