import schedule
import time
from lib import todo_list
from lib import controller
from os import getcwd,path,mkdir

queue = []
thread_control = controller.concurrent()

# 1.Create folder under tmp
# 2.Move executable to tmp
# 3.Move executable back
# 4.Review result
# ?.Delete everything
def create_sandbox():
    sandbox = getcwd() + '/tmp'
    if not path.exists(sandbox):
        mkdir(sandbox)

# 1.Do something for the jobs remains
def what_should_i_do(jobs):
    create_sandbox()
    pass


# 1.Find jobs that are not executed
# 2.Save jobs that are finished
def check_job_list():
    jobs = todo_list.remain(queue, thread_control.concur)
    what_should_i_do(jobs)

# 1.Show the jobs statistics
def report_job_list():
    pass


# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
schedule.every(10).minutes.do(check_job_list)
schedule.every().hour.do(report_job_list)

thread_control.start()

while True:
    schedule.run_pending()
    time.sleep(1)

thread_control.join()