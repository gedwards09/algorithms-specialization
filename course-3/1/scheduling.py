import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')
from ScheduledJobList import ScheduledJobList

def alg(filename):
    job_list = ScheduledJobList(filename)
    return [job_list.get_weighted_completion_time_bad(), job_list.get_weighted_completion_time_greedy()]

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./scheduling.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()