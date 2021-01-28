# coding: utf-8

import subprocess
import typing
import time
import _thread as thread


class ProcessesController:
    def __init__(self):
        self.processes = []

    def create_process(self, process_name, *args, **kwargs):
        kwargs['stdin'] = subprocess.PIPE
        kwargs['stdout'] = subprocess.PIPE
        kwargs['stderr'] = subprocess.PIPE

        self.processes.append(
            [process_name, subprocess.Popen(*args, **kwargs), b""])
        thread.start_new_thread(
            self.__class__.subthread_read_stdout, (self, len(self.processes) - 1))
        thread.start_new_thread(
            self.__class__.subthread_read_stderr, (self, len(self.processes) - 1))

        return len(self.processes) - 1

    def subthread_read_stdout(self, pid):
        time.sleep(0.1)
        try:
            while True:
                self.processes[pid][2] += self.processes[pid].stdout.read()
        except:
            return

    def subthread_read_stderr(self, pid):
        time.sleep(0.1)
        try:
            while True:
                self.processes[pid][2] += self.processes[pid].stderr.read()
        except:
            return

    def get_processes(self):
        return self.processes

    def kill_process(self, process_id):
        return self.processes[process_id][1].kill()

    def read_stdout(self, process_id):
        now = self.processes[process_id][2]
        self.processes[process_id][2] = b''
        return now

    def read_flush(self, process_id):
        return b""

    def put_stdin(self, process_id, s):
        return self.processes[process_id][1].stdin.write(s)
