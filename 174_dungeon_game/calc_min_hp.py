class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):

        hp_right = calculateMinimumHP()
        hp_down = calculateMinimumHP()
        
        ans = 1
        if (dungeon[0][0] < 0)
            ans = -dungeon[0][0] + 1
        
        if hp_right < hp_down < 0:
            return ans + (-hp_down) + 1
        if hp_down < hp_right < 0:
            return ans + (-hp_right) + 1

        if hp_right >= 0 or hp_down > = 0
            return ans + 1
        
