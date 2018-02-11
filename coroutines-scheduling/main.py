'''
假设你的手头上会有多个任务，每个任务耗时很长，
而你又不想同步处理，而是希望能像多线程一样交替执行。
这时，你就需要一个调度器来协调流程了。
这里我们用一个队列（deque）储存任务列表。
其中的 run 是一个重要的方法：
它通过轮转队列依次唤起任务，
并将已经完成的任务清出队列，
简洁地模拟了任务调度的过程。
'''
from collections import deque


def task(name, times):

    for i in range(times):
        yield
        print(name, i)


class Runner(object):

    def __init__(self, tasks):
        self.tasks = deque(tasks)

    def next(self):
        return self.tasks.pop()

    def run(self):
        while len(self.tasks):
            task = self.next()
            try:
                next(task)
            except StopIteration:
                pass
            else:
                self.tasks.appendleft(task)


if __name__ == "__main__":
    Runner([
        task('Kevin', 5),
        task('Jack', 4),
        task('Bob', 6)
    ]).run()
