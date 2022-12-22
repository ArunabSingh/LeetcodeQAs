def spiralTraverse(array):
    # Write your code here
    spiral_order = []

    start_col = 0
    start_row = 0

    end_col = len(array[0]) - 1
    end_row = len(array) - 1

    while start_col <= end_col and start_row <= end_row:
        for col in range(start_col, end_col + 1):
            spiral_order.append(array[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            spiral_order.append(array[row][end_col])

        for col in range(end_col - 1, start_col - 1, -1):
            if start_row == end_row:
                break
            spiral_order.append(array[end_row][col])

        for row in range(end_row - 1, start_row, -1):
            if start_col == end_col:
                break
            spiral_order.append(array[row][start_col])

        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1

    return spiral_order
