import numpy as np
import matplotlib.pyplot as plt

def softmax(z):
    exp_z = np.exp(z - np.max(z))
    return exp_z / np.sum(exp_z)

def cross_entropy_log2(p, q):
    return -np.sum(p * np.log2(q + 1e-9))

p = np.array([1/2, 1/4, 1/4])
z = np.array([0.0, 0.0, 0.0]) 

learning_rate = 0.1
iterations = 500

print(f"Target P: {p}")
print("-" * 30)

history = []

for i in range(iterations):
    q = softmax(z)
    loss = cross_entropy_log2(p, q)
    history.append(loss)

    gradient = (q - p)

    z = z - learning_rate * gradient

    if i % 100 == 0:
        print(f"Iter {i}: Loss={loss:.5f}, q={np.round(q, 4)}")

# 結果驗證
q_final = softmax(z)
print("-" * 30)
print(f"Final q : {np.round(q_final, 4)}")
print(f"Target p: {p}")
print(f"Match?  : {np.allclose(q_final, p, atol=1e-3)}")

# 計算 p  Entropy 
entropy_p = -np.sum(p * np.log2(p))
print(f"Min Loss (Entropy of p): {entropy_p:.5f}")
print(f"Final Loss             : {history[-1]:.5f}")

# 繪製下降圖
plt.plot(history)
plt.title("Cross Entropy Minimization using Gradient Descent")
plt.xlabel("Iteration")
plt.ylabel("Cross Entropy Loss")
plt.grid(True)
plt.show()
