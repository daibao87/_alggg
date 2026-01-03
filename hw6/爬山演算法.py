import numpy as np

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 10 + 3 * X + np.random.randn(100, 1)

def hill_climbing(X, y, iterations=2000):
    w = np.random.randn()
    b = np.random.randn()

    current_pred = X * w + b
    current_loss = np.mean((current_pred - y)**2)
    
    step_size = 0.05 
    
    for i in range(iterations):

        w_try = w + (np.random.rand() - 0.5) * step_size * 2
        b_try = b + (np.random.rand() - 0.5) * step_size * 2
        
        try_pred = X * w_try + b_try
        try_loss = np.mean((try_pred - y)**2)

        if try_loss < current_loss:
            w = w_try
            b = b_try
            current_loss = try_loss
            
    return w, b, current_loss
w_final, b_final, final_loss = hill_climbing(X, y)

print("=== 結果 ===")
print(f"預測參數: w = {w_final:.4f}, b = {b_final:.4f}")
print(f"最終誤差 (MSE): {final_loss:.4f}")
