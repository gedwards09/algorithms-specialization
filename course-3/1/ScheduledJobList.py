class ScheduledJobList:
    def __init__(self, filename):
        self._max_weight = 0
        self._list = self.init_list(filename)

    def init_list(self, filename):
        n = 0
        id = 0
        list = []
        with open(filename, 'r') as f:
            for line in f:
                if n != 0:
                    weight, length = [int(num) for num in line.split()]
                    list.append({"id":id, "weight":weight, "length":length})
                    if weight > self._max_weight:
                        self._max_weight = weight
                    id += 1
                else:
                    n = int(line)
        return list

    def get_weighted_completion_time_greedy(self):
        sort_strategy = lambda job: job["weight"] / job["length"]
        return self.get_weighted_completion_time(sort_strategy)

    def get_weighted_completion_time(self, sort_strategy):
        self._list.sort(key = sort_strategy, reverse=True)
        s = 0
        completion_time = 0
        for job in self._list:
            completion_time += job["length"]
            s += job["weight"] * completion_time
        return s
    
    def get_weighted_completion_time_bad(self):
        sort_strategy = lambda job: job["weight"] - job["length"] + (job["weight"]/self._max_weight)
        return self.get_weighted_completion_time(sort_strategy)