class Solution: # Time Limit Exceeded
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        """
        core: the minimun hp to go to next point
        """
        if len(dungeon) == 1 and len(dungeon[0]) == 1:  # one point
            return 1 if dungeon[0][0] >=0 else -dungeon[0][0] + 1
        elif len(dungeon) > 1 and len(dungeon[0]) == 1: # one column
            hp_down = self.calculateMinimumHP(dungeon[1:])
            min_hp = hp_down - dungeon[0][0]
            return 1 if min_hp <= 0 else min_hp
        elif len(dungeon) == 1 and len(dungeon[0]) > 1: # one row
            hp_right = self.calculateMinimumHP([line[1:] for line in dungeon])
            min_hp = hp_right - dungeon[0][0]
            return 1 if min_hp <= 0 else min_hp
        elif len(dungeon) > 1 and len(dungeon[0]) > 1:
            hp_down = self.calculateMinimumHP(dungeon[1:])
            hp_right = self.calculateMinimumHP([line[1:] for line in dungeon])
            min_hp = min(hp_down, hp_right) - dungeon[0][0]
            return 1 if min_hp <= 0 else min_hp
        
        
def main():
    m = [[-2, -3, 3],
         [-5, -10, 2],
         [10, 30, -5]]
    s = Solution()
    print s.calculateMinimumHP(m)
    print s.calculateMinimumHP([[5, -5]])

if __name__ == '__main__':
    main()
