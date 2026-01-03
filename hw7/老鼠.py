def print_matrix(m):
    for row in m:
        print("".join(row))
    print("=" * 25)

def find_path(m, x, y):
    rows = len(m)
    cols = len(m[0])
    
    print(f"Current: x={x}, y={y}")
    # print_matrix(m) # 若想看每一步驟可取消註解

    # 1. 邊界檢查
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    
    # 2. 障礙物檢查 (*=牆, +=死路, .=已走過)
    if m[x][y] in ['*', '+', '.']:
        return False

    # 3. 標記路徑
    m[x][y] = '.'

    # 4. 終點檢查 (到達邊界算成功)
    if x == rows - 1 or y == cols - 1:
        return True

    # 5. 遞迴搜尋 (右 -> 下 -> 左 -> 上)
    if find_path(m, x, y + 1): return True
    if find_path(m, x + 1, y): return True
    if find_path(m, x, y - 1): return True
    if find_path(m, x - 1, y): return True

    # 6. 回溯：此路不通，標記為 +
    m[x][y] = '+'
    return False

# 初始化迷宮 (使用 List of Lists 以便修改)
maze_str = [
    "********",
    "** * ***",
    "     ***",
    "* ******",
    "* **",
    "***** **"
]
# 轉換為二維陣列 (List of Lists)
maze = [list(row) for row in maze_str]

# 執行
if find_path(maze, 2, 0):
    print("成功走出迷宮！最終狀態：")
    print_matrix(maze)
else:
    print("無路可走")
