import schedule
import time
from lib import py
from lib import controller
from os import getcwd,path,mkdir
from shutil import move
maxqueue = 100
working_queue = set()
complete_queue= set()
thread_control = controller.concurrent()

class remain(object):
    def __init__(self, concur):
        # type: (concur) -> unfinished
        """
        :concur: return the # of concurrent jobs
        :rtype: list[jobs]
        """
        unfinished = self.find_jobs()
        return unfinished[:concur]

    def find_jobs(self):
        job1 = py.job_py(True, proj_path='print "j1"')
        job2 = py.job_py(True, proj_path='print "j2"')
        job3 = py.job_py(True, proj_path='print "j3"')
        job4 = py.job_py(True, proj_path='print "j4"')
        return set(job1, job2, job3, job4)

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
    if len(working_queue) < maxqueue:
        working_queue.union(jobs)
    for i in working_queue:
        if i.debug:
            i.temp_path = getcwd()+'/tmp'
            move(i.proj_path, i.temp_path)

        if i.p.poll() == 0:
            working_queue.remove(i)
            complete_queue.add(i)



# 1.Find jobs that are not executed
# 2.Save jobs that are finished
def check_job_list():
    jobs = remain(thread_control.concur)
    what_should_i_do(jobs.find_jobs())

# 1.Show the jobs statistics
def report_job_list():
    pass


# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
schedule.every(10).minutes.do(check_job_list)
schedule.every().hour.do(report_job_list)
create_sandbox()
thread_control.start()

while True:
    schedule.run_pending()
    time.sleep(1)

thread_control.join()