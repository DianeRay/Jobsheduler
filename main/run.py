import schedule
import time
from os import getcwd,path,mkdir
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
    import todo_list
    what_should_i_do(todo_list.remain())

# 1.Show the jobs statistics
def report_job_list():
    pass



if __name__ == '__main__':
    schedule.every(10).minutes.do(check_job_list)
    schedule.every().hour.do(report_job_list)
    #schedule.every().day.at("10:30").do(job)
    #schedule.every().monday.do(job)
    #schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)