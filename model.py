import torch
import torch.nn as nn
import torch.nn.functional as F

# Let's now define our Neural Network.

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)  # Apply 2D dropout after convolutions
        self.dropout2 = nn.Dropout(0.5)     # Apply regular dropout after fully connected layers
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)               # 2D dropout applied after max pooling
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)               # Regular dropout applied after fully connected layer
        output = self.fc2(x)
        return output
