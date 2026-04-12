import torch
import torch.nn as nn

class DQN(nn.Module):
    #input dim , output dim , hidden dim

    def __init__(self, num_states, num_actions):
        super(DQN,self).__init__()

        self.model = nn.Sequential(
            nn.Linear(num_states , 128),
            nn.ReLU(),
            nn.Linear(128,num_actions)
        )

    def forward(self,x):
        return self.model(x)    
    