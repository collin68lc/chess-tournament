from datetime import datetime

class round:
    """set rounds"""

    def __init__(self, name):
        self.name = name



maintenant = datetime.now()
print(maintenant)                          # 2026-11-24 10:48:12.345678
print(maintenant.strftime("%d/%m/%Y %H:%M"))  # 24/11/2026 10:48