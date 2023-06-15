class Task:
    def __init__(self, description, deadline):
        self._description = description
        self._deadline = deadline
        self._completed = False

    def set_description(self, text):
        self._description = text

    def get_description(self):
        return self._description

    def set_status(self, status):
        self._completed = status

    def get_status(self):
        return self._completed

    def set_deadline(self, date):
        self._deadline = date

    def get_deadline(self):
        return self._deadline
