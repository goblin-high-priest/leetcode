class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for course, pre in prerequisites:
            preMap[course].append(pre)

        def has_cycle(course):

            if course in visited:
                return True
            
            if not preMap[course]:
                return False
            
            visited.add(course)

            for pre in preMap[course]:

                if has_cycle(pre):
                    return True

            visited.remove(course)
            preMap[course] = []
            return False
        
        for course in range(numCourses):
            
            if has_cycle(course):
                return False
        
        return True
