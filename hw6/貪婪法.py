import numpy as np

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 10 + 3 * X + np.random.randn(100, 1)

def greedy_search(X, y, iterations=1000):
    w = 0.0
    b = 0.0
    step_size = 0.1

    best_loss = np.mean(((X * w + b) - y)**2)
    
    for i in range(iterations):
        candidates = [
            (w + step_size, b),
            (w - step_size, b),
            (w, b + step_size),
            (w, b - step_size)
        ]
        
        move_made = False

        for w_can, b_can in candidates:
            loss_can = np.mean(((X * w_can + b_can) - y)**2)

            if loss_can < best_loss:
                w, b = w_can, b_can
                best_loss = loss_can
                move_made = True
                break 

        if not move_made:
            step_size *= 0.5

        if step_size < 1e-5:
            break
            
    return w, b, best_loss

w_final, b_final, final_loss = greedy_search(X, y)

print("=== 結果 ===")
print(f"預測參數: w = {w_final:.4f}, b = {b_final:.4f}")
print(f"最終誤差 (MSE): {final_loss:.4f}")
