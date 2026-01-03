import numpy as np
import time

# ==========================================
# 方法 1: 遞迴黎曼積分 (Recursive Riemann Sum)
# ==========================================
def riemann_integrate_nd(func, bounds, subdivisions=10):
    """
    使用遞迴方式計算 n 維黎曼和 (中點法則)。
    
    參數:
    - func: 目標函數，接受一個 list 或 numpy array 作為輸入。
    - bounds: 積分範圍，格式為List of tuples: [(min1, max1), (min2, max2), ...]
    - subdivisions: 每個維度切分的段數 (注意：複雜度為 subdivisions^n)
    """
    bounds = np.array(bounds)
    ndim = len(bounds)
    
    # 計算每個維度的步長 (delta)
    deltas = (bounds[:, 1] - bounds[:, 0]) / subdivisions
    
    # 計算微小體積單元 dV (所有維度步長的乘積)
    dV = np.prod(deltas)
    
    # 用來暫存當前座標點的陣列
    current_point = np.zeros(ndim)

    def recursive_solver(dim_index):
        # 基底情況 (Base Case): 
        # 已經填滿所有維度的座標，計算函數值
        if dim_index == ndim:
            return func(current_point)
        
        local_sum = 0.0
        start, end = bounds[dim_index]
        step = deltas[dim_index]
        
        # 迴圈遍歷當前維度 (使用中點法: start + 0.5*step)
        # 這裡手動跑迴圈，從第 0 格跑到第 subdivisions-1 格
        for i in range(subdivisions):
            # 計算中點座標
            mid_point = start + (i + 0.5) * step
            current_point[dim_index] = mid_point
            
            # 遞迴呼叫下一層
            local_sum += recursive_solver(dim_index + 1)
            
        return local_sum

    # 開始遞迴，從第 0 維度開始
    total_sum_f = recursive_solver(0)
    
    return total_sum_f * dV

# ==========================================
# 方法 2: 蒙地卡羅積分 (Monte Carlo Integration)
# ==========================================
def monte_carlo_integrate_nd(func, bounds, num_samples=100000):
    """
    使用蒙地卡羅方法計算 n 維積分。
    適合高維度，不受 subdivisions^n 的複雜度爆炸影響。
    """
    bounds = np.array(bounds)
    ndim = len(bounds)
    
    # 1. 計算總體積 V = (max1-min1) * (max2-min2) ...
    volume = np.prod(bounds[:, 1] - bounds[:, 0])
    
    # 2. 生成隨機樣本點
    # np.random.uniform 可以在範圍內產生均勻分佈
    # lower_bounds 和 upper_bounds 用於向量化生成
    lower_bounds = bounds[:, 0]
    upper_bounds = bounds[:, 1]
    
    # 產生形狀為 (num_samples, ndim) 的矩陣
    random_points = np.random.uniform(low=lower_bounds, high=upper_bounds, size=(num_samples, ndim))
    
    # 3. 計算所有點的函數值總和
    # 這裡假設 func 可以接受單一點，我們使用列表推導式或 apply_along_axis
    # 如果 func 支援向量化輸入 (matrix input)，可以直接 sum(func(random_points))，速度會快非常多
    
    # 通用寫法 (假設 func 一次只吃一個點):
    total_value = sum(func(point) for point in random_points)
    
    # 4. 套用公式: 積分值 = 體積 * 平均函數值
    average_value = total_value / num_samples
    return volume * average_value

# ==========================================
# 測試範例
# ==========================================

# 定義一個 n 維函數，例如： f(x) = sum(x_i^2) (所有座標的平方和)
# 理論值:
# 如果是 3維，範圍 [0,1]^3，積分 x^2+y^2+z^2 
# Int(x^2) = 1/3. 總積分 = 1*1*(1/3) + 1*1*(1/3) + ... = 1 (因為體積是1，且各項獨立)
def target_function(point):
    return np.sum(np.array(point) ** 2)

if __name__ == "__main__":
    # 設定參數
    NDIM = 3
    BOUNDS = [(0, 1)] * NDIM  # 每個維度都是 0 到 1
    
    print(f"=== 正在計算 {NDIM} 維超球體的平方和積分 ===")
    print(f"積分範圍: {BOUNDS}")
    
    # --- 測試黎曼積分 ---
    # 注意：如果維度很高 (如 n>5)，subdivisions 必須設很小，否則計算量是 subdivisions^n
    N_SUB = 50 
    print(f"\n[黎曼積分] 切分段數: {N_SUB} (總運算次數: {N_SUB}^{NDIM} = {N_SUB**NDIM})")
    
    start_time = time.time()
    res_riemann = riemann_integrate_nd(target_function, BOUNDS, subdivisions=N_SUB)
    end_time = time.time()
    
    print(f"結果: {res_riemann:.6f}")
    print(f"耗時: {end_time - start_time:.4f} 秒")

    # --- 測試蒙地卡羅 ---
    N_SAMPLES = 500000
    print(f"\n[蒙地卡羅] 採樣點數: {N_SAMPLES}")
    
    start_time = time.time()
    res_mc = monte_carlo_integrate_nd(target_function, BOUNDS, num_samples=N_SAMPLES)
    end_time = time.time()
    
    print(f"結果: {res_mc:.6f}")
    print(f"耗時: {end_time - start_time:.4f} 秒")
    
    print(f"\n理論值 (對於 [0,1]^{NDIM} 的 sum(x^2)): {NDIM * (1/3):.6f}")
