import numpy as np
import math

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 10 + 3 * X + np.random.randn(100, 1)

def simulated_annealing(X, y, iterations=5000):
    w = 0.0
    b = 0.0
    current_loss = np.mean(((X * w + b) - y)**2)
    temperature = 100.0
    cooling_rate = 0.995 
    min_temperature = 0.001
    
    step_size = 0.1
    
    for i in range(iterations):
        if temperature < min_temperature:
            break
        w_new = w + (np.random.rand() - 0.5) * step_size
        b_new = b + (np.random.rand() - 0.5) * step_size
        new_loss = np.mean(((X * w_new + b_new) - y)**2)
        if new_loss < current_loss:
            w, b = w_new, b_new
            current_loss = new_loss
        else:
            prob = math.exp((current_loss - new_loss) / temperature)
            if np.random.rand() < prob:
                w, b = w_new, b_new
                current_loss = new_loss

        temperature *= cooling_rate
            
    return w, b, current_loss
w_final, b_final, final_loss = simulated_annealing(X, y)

print("=== 結果 ===")
print(f"預測參數: w = {w_final:.4f}, b = {b_final:.4f}")
print(f"最終誤差 (MSE): {final_loss:.4f}")
