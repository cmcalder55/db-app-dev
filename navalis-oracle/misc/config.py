import os

class settings():

    def __init__(self) -> None:
        self.DB_URL=os.environ["URI"]