import threading

settings = 'queue_size, q to exit'
class concurrent(threading.Thread):
    def __init__(self, concur=4):
        threading.Thread.__init__(self)
        self.concur = concur

    def run(self):
        while True:
            print settings
            command = raw_input()
            if command.isdigit():
                d = int(command)
                self.concur = d if d > 0 and d < 100 else 4
            else:
                self.dying()

    def dying(self):
        pass