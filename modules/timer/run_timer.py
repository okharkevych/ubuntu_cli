# this separate file is needed for scripts.timer to be able to run
# timer in a new terminal window instead of the current one
from modules.timer.base import Timer

if __name__ == '__main__':
    timer = Timer()
    timer.main()
