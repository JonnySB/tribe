from datetime import datetime


class Peep:
    # initialise peep object with associated attributes
    def __init__(self, id, message, date_created, user_id):
        self.id = id
        self.message = message
        self.date_created = date_created
        self.user_id = user_id

    # ensure two object with identical attrs will be found equal
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # return nicely formatted string version of peep object
    def __repr__(self):
        return f"Peep({self.id}, {self.message}, {self.date_created}, {self.user_id})"
