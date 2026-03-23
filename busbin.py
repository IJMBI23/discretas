def busbin(a:list[int], x:int) -> int:
    def searching(left, right):
        if left > right:
            return -1
        m = (left + right) // 2
        if x == a[m]:
            return m
        if x < a[m]:
            return searching(left, m - 1)
        return searching(m + 1, right)
    return searching(0, len(a) - 1)
