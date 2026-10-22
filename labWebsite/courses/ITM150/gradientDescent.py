import torch
import matplotlib.pyplot as plt
losses = []

# 定義訓練資料
sizes = torch.tensor([1500, 2000, 1200], dtype=torch.float32)
bedrooms = torch.tensor([3, 4, 2], dtype=torch.float32)
prices = torch.tensor([300000, 400000, 250000], dtype=torch.float32)

# 初始化權重
w1 = torch.randn(1, requires_grad=True)
w2 = torch.randn(1, requires_grad=True)

# 定義訓練迴圈
learning_rate = 0.0000001
epochs = 10000

for epoch in range(epochs):
    # 預測房價
    predictions = w1 * sizes + w2 * bedrooms
    
    # 計算損失
    loss = torch.mean((predictions - prices) ** 2)
    
    # 使用反向傳播計算梯度
    loss.backward()
    losses.append(loss.item())

    # 更新權重
    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad
        
        # 將梯度歸零
        w1.grad.zero_()
        w2.grad.zero_()
    
    if epoch % 1000 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')

plt.plot(losses)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# Weighting
print(f'weighting：w1 = {w1.item()}, w2 = {w2.item()}')
