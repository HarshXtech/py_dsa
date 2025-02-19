def countNegatives(grid):
    
    def count_neg_in_rows(row):
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2

            if row[mid] < 0:
                right = mid
            else:
                left = mid + 1
        return len(row) - left
    
    total_negatives = 0

    for row in grid:
        total_negatives += count_neg_in_rows(row)                      

    
    return total_negatives


print(countNegatives([[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] ))
