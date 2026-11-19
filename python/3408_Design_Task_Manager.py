class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (userId, priority)
            self.heap.append((-priority, -taskId))

        heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.tasks[taskId]
        self.tasks[taskId] = (userId, newPriority)
        heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            negative_priority, negative_task_id = heappop(self.heap)

            priority = -negative_priority
            taskId = -negative_task_id

            if taskId not in self.tasks:
                continue
            
            userId, current_priority = self.tasks[taskId]

            if priority != current_priority:
                continue
            
            del self.tasks[taskId]

            return userId
        
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
