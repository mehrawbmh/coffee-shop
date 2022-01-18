class DBError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message

    def __str__(self):
        return "Some error happened while working with database.exact part:{} | related message:{}".format(self.field,
                                                                                                           self.message)


class FrontError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Some Error happened while connecting the back-end side to templates-or transfering requests- " \
               f"full message:{self.message}"
