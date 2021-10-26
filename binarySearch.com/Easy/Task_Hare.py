class Solution:
    def solve(self, tasks, people):
        if len(people)<1:
            return 0
        elif len(people)<2 and len(tasks)>1:
            return 1 if tasks[0] <= people[0] else 0
        elif len(people)<2 and len(tasks)<1:
            return 0
        sortPpl = people.sort(reverse=True)
        sortTask = tasks.sort(reverse=True)
        count=0
        taskIndex = 0
        for ii in range(0, len(people)):
            while(taskIndex < len(tasks)):
                if tasks[taskIndex] <= people[ii]:
                    count += 1
                    taskIndex += 1
                    break
                taskIndex += 1
        return count

      
# optimised solution
class Solution:
    def solve(self, tasks, people):
        # sort in ascending order
        tasks.sort()
        people.sort()
        n = len(people)
        n2 = len(tasks)
        
        if (n2 == 0):
            return 0
        i = 0
        j = 0
        while (i < n2 and j < n):
            if (tasks[i] <= people[j]):
                # increment number of tasks
                # and go to next people
                i+=1
                j+=1
            else:
                # go to next people
                j+=1
        return i
