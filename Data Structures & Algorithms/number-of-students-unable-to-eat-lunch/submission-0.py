class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        prefs = {
            0: 0,
            1: 0
        }
        for s in students:
            if s == 0:
                prefs[0] += 1
            else:
                prefs[1] += 1
        
        for s in sandwiches:
            if prefs[s] > 0:
                prefs[s] -= 1
                res -= 1
            else:
                break
                                       

        return res