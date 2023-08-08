class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freqs=dict()
        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1
        maxtask = max(freqs.values())
        interval = maxtask-1
        size = interval * (n+1)
        for count in freqs.values():
            if count == maxtask:
                size += 1
        
        return max(size, len(tasks))