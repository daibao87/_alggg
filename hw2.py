# 方法 1：直接運算
def power2n_1(n):
    return 2**n

# 方法 2a：用遞迴 (加法型)
def power2n_2a(n):
    if n == 0: return 1
    return power2n_2a(n-1) + power2n_2a(n-1)

# 方法 2b：用遞迴 (乘法型)
def power2n_2b(n):
    if n == 0: return 1
    return 2 * power2n_2b(n-1)

# 方法 3：用遞迴 + 查表 (Memoization)
memo = {0: 1}
def power2n_3(n):
    if n in memo:
        return memo[n]
    
    # 使用 power2n(n-1) + power2n(n-1)
    res = power2n_3(n-1) + power2n_3(n-1)
    memo[n] = res
    return res

# 測試
n = 10
print(f"方法 1: {power2n_1(n)}")
print(f"方法 2a: {power2n_2a(n)}")
print(f"方法 2b: {power2n_2b(n)}")
print(f"方法 3: {power2n_3(n)}")
