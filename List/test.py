from ListAlgorithms import ListNode, Solution

if __name__ == "__main__":
    solution = Solution()
    
    ListNodes = [ListNode(num) for num in range(5)]
    for index in range(4):
        ListNodes[index].next = ListNodes[index + 1]
    ListNodes[-1].next = None
    
    print(solution.detectCycle(ListNodes[0]))
    print(solution.rotateRight(ListNodes[0], 3))