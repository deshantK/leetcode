class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        cnt = 0
        right = len(people)-1
        left = 0
        while left <= right:
            if people[right]+people[left] <= limit:
                left +=1
            right -=1
            cnt +=1


        return cnt
        