from lib import job
from subprocess import Popen
class job_py(job):
    # command is the compile command
    # proj_path is the whole folder of project
    # exec_path is the executable relative path to proj_path front '/' is excluded
    def __init__(self, debug, command='python', proj_path='', exec_path=''):
        self.debug = debug
        self.exec_command = command
        self.exec_path = exec_path
        self.proj_path = proj_path
        self.temp_path = ''

    # Python do not need compile.
    def compile(self):
        pass

    def run_job(self):
        self.p = Popen([self.exec_command, self.proj_path + self.exec_path])

    def alive(self):
        return self.p.poll()
