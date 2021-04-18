import heapq
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        task_with_idx = [(tasks[i][0], tasks[i][1], i)for i in range(len(tasks))]
        task_with_idx.sort()
        print(task_with_idx)
        h, result = [], []
        i, ts = 0, None
        while i < len(task_with_idx):
            enqueue_time, process_time, idx = task_with_idx[i]
            if ts is None or (ts < enqueue_time and len(h) == 0):
                heapq.heappush(h, (process_time, idx))
                i += 1
                ts = enqueue_time
            else:
                while i < len(task_with_idx) and enqueue_time <= ts:
                    heapq.heappush(h, (process_time, idx))
                    i += 1
                    if i == len(task_with_idx):
                        break
                    enqueue_time, process_time, idx = task_with_idx[i]
            # process one element from heap
            process_time, idx = heapq.heappop(h)
            ts += process_time
            result.append(idx)
            print(ts, idx)
        
        while len(h) > 0:
            result.append(heapq.heappop(h)[1])

        return result
        