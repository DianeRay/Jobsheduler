# 1.Remove completed jobs from queue
# 2.Add existing jobs to queue
from lib import py
class remain(object):
    def __init__(self, queue, concur):
        # type: (object, object) -> object
        """
        :rtype: object
        """
        unfinished = self.find_jobs()
        return unfinished

    def find_jobs(self):
        job1 = py.job_py(proj_path='print "j1"')
        job2 = py.job_py(proj_path='print "j2"')
        job3 = py.job_py(proj_path='print "j3"')
        job4 = py.job_py(proj_path='print "j4"')
        return [job1, job2, job3, job4]