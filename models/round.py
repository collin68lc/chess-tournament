from datetime import datetime
import time


class Round:
    """Display the start time and the end time of a round."""

    def __init__(self, name):

        now = datetime.now()
        self.name = name
        self.matches = []
        self.start_time = now.strftime("%d/%m/%Y %H:%M:%S")
        self.end_time = None

    def finish(self):
        """Set the end time of a round."""
        now = datetime.now()
        self.end_time = now.strftime("%d/%m/%Y %H:%M:%S")


if __name__ == "__main__":
    r = Round("Round 1")
    print(r.start_time)
    time.sleep(2)
    r.finish()
    print(r.end_time)
