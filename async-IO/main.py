from sleep import sleep
import runner


def task(name):
    print(name, 1)
    yield sleep(1)
    print(name, 2)
    yield sleep(2)
    print(name, 3)


if __name__ == '__main__':
    runner.run((task('Kevin'), task('Jack')))

# output:
# Kevin 1
# Jack 1
# Kevin 2
# Jack 2
# Kevin 3
# Jack 3
# python main.py  3.04s user 0.03s system 99% cpu 3.087 total