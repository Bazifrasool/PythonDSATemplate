
def isValidState(state,n):
    if len(state) == n:
        return True
    else:
        False

def getCandidates(state,n):
    if len(state) == 0:
        return range(n)
    candidates = range(n)
    selected_candidates = [x for x in candidates if x not in state ]
    return selected_candidates

def search(state,soln,n):
    if isValidState(state,n):
        soln.append(state.copy())
    for each in getCandidates(state,n):
        state.append(each)
        search(state,soln,n)
        state.pop()

if __name__ == "__main__":
    string_main = "IAMBAZIF"
    array = [0,1,2,3,4,5,6,7]
    soln = []
    state = []
    search(state,soln,len(array))
    for each in soln:
        for i,every in enumerate(each):
            each[i] = string_main[every]
    for i,each in enumerate(soln):
        print(i+1,"".join(each))