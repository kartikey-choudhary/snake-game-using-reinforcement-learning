import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
device = torch.device("cpu")
class Linear_QNet(nn.Module):
    def __init__(self,input_size,hidden_size,output_size):
        super().__init__()
        self.linear1=nn.Linear(input_size,hidden_size)
        self.linear2=nn.Linear(hidden_size,output_size)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.relu(x)
        x = self.linear2(x)
        return x
    
    def save(self,file_name='model.pth'):
        model_folder_path='./model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name=os.path.join(model_folder_path,file_name)
        torch.save(self.state_dict(),file_name)

class QTrainer:
    def __init__(self,model,lr,gamma):
        self.lr=lr
        self.gamma=gamma
        self.model=model
        self.optimizer=optim.Adam(model.parameters(),lr=self.lr)
        self.criterion=nn.MSELoss()

    def train_step(self,state,action,reward,next_state,done):
        state=torch.tensor(state,dtype=torch.float).to(device) 
        next_state=torch.tensor(next_state,dtype=torch.float).to(device) 
        action=torch.tensor(action,dtype=torch.long).to(device) 
        reward=torch.tensor(reward,dtype=torch.float).to(device)   

        if len(state.shape)==1:
            state=torch.unsqueeze(state,0)
            next_state=torch.unsqueeze(next_state,0)
            action=torch.unsqueeze(action,0)
            reward=torch.unsqueeze(reward,0)
            done=(done, ) 

        pred=self.model(state)

        target=pred.clone()
        for idx in range(len(done)):
            Q_new=reward[idx]
            if not done[idx]:
                Q_new=reward[idx]+self.gamma*torch.max(self.model(next_state[idx]))
            target[idx][torch.argmax(action).item()]=Q_new
        
        self.optimizer.zero_grad()
        loss=self.criterion(target,pred)
        loss.backward()
        self.optimizer.step()