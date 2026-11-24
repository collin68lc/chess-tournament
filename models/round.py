from datetime import datetime

class round:
    """set rounds"""

    now = datetime.now()

    def __init__(self, name):

        now = datetime.now()
        self.name = name
        self.matches = []
        self.start_time = now.strftime("%d/%m/%Y %H:%M")
        self.end_time = None

    def finish(self):