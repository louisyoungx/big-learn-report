import datetime

class Log():

    def __init__(self):
        self.log_data = []

    def update(self, log_message):
        TIME = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = "[{}] {}".format(TIME, log_message)
        print(log_message)
        self.log_data.append(log_message)
        if len(self.log_data) > 30:
            self.log_data.pop()
<<<<<<< HEAD
=======
            
>>>>>>> 6f53f41ff1c9f2af7dfc201f0e058d71a7105f49
    def get_data(self):
        return self.log_data

log = Log()
log.update("(Log): Append Module Success")
