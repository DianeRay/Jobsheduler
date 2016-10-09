import threading

settings = 'concur = '
class concurrent(threading.Thread):
    def __init__(self, concur=4):
        threading.Thread.__init__(self)
        self.concur = concur
    # 1. Receive user input to control the system
    def run(self):
        while True:
            print settings+str(self.concur)
            command = raw_input()
            if command.isdigit():
                d = int(command)
                self.concur = d if d > 0 and d < 100 else 4
            else:
                self.dying()
    # 1.Save the current state
    # 2.Notify program to exit
    def dying(self):
        exit(0);