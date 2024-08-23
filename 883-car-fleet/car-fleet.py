class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # What the problem wants from us:
        # return number of fleets
        # fleets are groups of cars tarvelling together (speed is lowest speed of the car in that group)
        # the order of the cars in the position arry doesn't matter
        # position !> target
        # one laned road

        spos = []
        for i in range(len(position)):
            spos.append((position[i], speed[i]))        
        spos.sort()

        stackk = []
        for i in range(len(spos)-1, -1, -1):
            distance = target - spos[i][0]
            time = distance / spos[i][1]

            stackk.append(time)
            if len(stackk) > 1:
                if stackk[len(stackk)-2] >= time:
                    stackk.pop()
        
        # print(spos)
        # print(stackk)
        return len(stackk)








