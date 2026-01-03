import json

def editDistance(b, a):
    """
    計算字串 b 到字串 a 的最小編輯距離 (Levenshtein Distance)
    b: source string
    a: target string
    回傳: 字典 {'d': 距離數值, 'm': DP矩陣}
    """
    alen, blen = len(a), len(b)
    
    # 邊界情況處理：若其中一個字串為空
    if alen == 0: return {'d': blen, 'm': []}
    if blen == 0: return {'d': alen, 'm': []}

    # 初始化矩陣 (blen+1) x (alen+1)
    # m[i][j] 代表 b的前i個字元 轉換到 a的前j個字元 的距離
    m = [[0] * (alen + 1) for _ in range(blen + 1)]

    # 初始化第一欄 (b 轉換為空字串需刪除 i 次)
    for i in range(blen + 1):
        m[i][0] = i
    
    # 初始化第一列 (空字串轉換為 a 需插入 j 次)
    for j in range(alen + 1):
        m[0][j] = j

    # 動態規劃填表
    for i in range(1, blen + 1):
        for j in range(1, alen + 1):
            if b[i-1] == a[j-1]:
                # 字元相同，距離不變
                m[i][j] = m[i-1][j-1]
            else:
                # 取三者最小值：取代、插入、刪除
                m[i][j] = min(
                    m[i-1][j-1] + 1, # Substitution (取代)
                    m[i][j-1] + 1,   # Insertion (插入 a[j] / Gap in b)
                    m[i-1][j] + 1    # Deletion (刪除 b[i] / Gap in a)
                )
                
    return {'d': m[blen][alen], 'm': m}

def align(b, a, m):
    """
    根據 DP 矩陣回溯路徑並印出對齊結果
    """
    i, j = len(b), len(a)
    ax, bx = '', ''
    
    # 開始回溯 (Backtracking)
    while (i > 0 and j > 0):
        # 這裡的判斷順序決定了當有多條路徑成本相同時的優先選擇
        # 優先檢查是否是「刪除 (Gap in a)」(來自上方)
        if m[i][j] == m[i-1][j] + 1:
            i -= 1
            bx = b[i] + bx
            ax = '-' + ax  # 使用 '-' 代表空隙，比空白更清楚
        
        # 檢查是否是「插入 (Gap in b)」(來自左方)
        elif m[i][j] == m[i][j-1] + 1:
            j -= 1
            ax = a[j] + ax
            bx = '-' + bx
            
        # 檢查是否是「取代」或「相同」(來自左上方)
        else: 
            i -= 1
            j -= 1
            bx = b[i] + bx
            ax = a[j] + ax

    # 處理邊界剩餘的字元
    while (i > 0):
        i -= 1
        bx = b[i] + bx
        ax = '-' + ax
    
    while (j > 0):
        j -= 1
        ax = a[j] + ax
        bx = '-' + bx
    
    print('Alignment Result:')
    print(f'b (Source): {bx}')
    print(f'a (Target): {ax}')

def dump(m):
    print("Matrix Dump:")
    for row in m:
        print(json.dumps(row))

# === 主程式執行驗證 ===
if __name__ == "__main__":
    # 測試資料
    # 注意：這裡的 b 字串中間包含兩個空白
    b_str = "ATG  ATCCG"
    a_str = "ATGCAATCCC"
    
    print(f"Comparing:\nString b: '{b_str}'\nString a: '{a_str}'\n")

    result = editDistance(b_str, a_str)
    
    print(f"Min Edit Distance: {result['d']}\n")
    
    # 若想看矩陣詳細內容可取消下面註解
    # dump(result['m'])
    
    align(b_str, a_str, result['m'])
