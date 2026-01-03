import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 10 + 3 * X + np.random.randn(100, 1) 

def gradient_descent(X, y, learning_rate=0.1, iterations=1000):
    w = 0.0 
    b = 0.0
    m = len(y) 
    
    losses = []
    
    for i in range(iterations):
        y_pred = X.dot(w) + b

        loss = np.mean((y_pred - y)**2)
        losses.append(loss)
        diff = y_pred - y
        dw = (2/m) * np.sum(diff * X) 
        db = (2/m) * np.sum(diff)     
        w = w - learning_rate * dw
        b = b - learning_rate * db
        
    return w, b, losses
w_final, b_final, loss_history = gradient_descent(X, y)

print("=== 結果 ===")
print(f"預測參數: w = {w_final:.4f}, b = {b_final:.4f}")
print(f"最終誤差 (MSE): {loss_history[-1]:.4f}")
