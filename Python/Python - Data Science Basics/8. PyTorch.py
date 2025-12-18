import torch

# give me a sample program for pytorch basics
import torch.nn as nn
import torch.optim as optim

# Create tensors
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

# Basic operations
z = x + y
print("Addition:", z)

# Simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(3, 1)
    
    def forward(self, x):
        return self.fc(x)

model = SimpleNet()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy training data
inputs = torch.randn(10, 3)
targets = torch.randn(10, 1)

# Training loop (simplified)
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

print("Training complete. Final loss:", loss.item())