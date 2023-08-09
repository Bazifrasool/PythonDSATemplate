class Solution(object):
    def search(self,soln,state,n):
        if self.is_valid_state(state,n):
            print("here",soln,state)
            soln.append(state.copy())
        for each in self.get_candidate(state,n):
            state.append(each)
            self.search(soln,state,n)
            state.remove(each)

    def get_candidate(self,state,n):
        if len(state) ==0:
            return range(n)
        candidates = set(range(n))
        atk_col = set()
        atk_posDiag = set()
        atk_negDiag = set()
        for row,col in enumerate(state):
            atk_col.add(col)
            atk_posDiag.add(row+col)
            atk_negDiag.add(row-col)
        to_prune = set()
        for each in candidates:
            if each +  len(state) in atk_posDiag or len(state) -each in atk_negDiag or each in atk_col:
                to_prune.add(each)
        return candidates.difference(to_prune)



    def is_valid_state(self,state,n):
        if len(state) == n:
            return True
        else:
            return False

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        soln = []
        state = []
        self.search(soln,state,n)
        matrix = [["." for y in range(n)] for i in range(n)]
        res = []
        for each in soln:
            matrix =[["." for y in range(n)] for i in range(n)]
            for row,col in enumerate(each):
                matrix[row][col] = "Q"
            res.append(matrix.copy())
        for each in res:
            for row,every in enumerate(each):
                each[row] = "".join(every)
        return res