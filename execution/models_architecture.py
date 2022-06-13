class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, layer_dim):
        super(LSTM, self).__init__()
        self.hidden_dim, self.layer_dim, self.input_dim = hidden_dim, layer_dim, input_dim
        self.lstm = nn.LSTM(input_size=input_dim, hidden_size=hidden_dim, num_layers=layer_dim, batch_first=True, dropout=dropout_val)
        self.linear = nn.Linear(hidden_dim, out_features=dim_out)
        self.act = nn.LeakyReLU()

    def forward(self, x):
        h0 = torch.zeros(self.layer_dim, CFG.batch_size, self.hidden_dim, device=x.device).requires_grad_()
        c0 = torch.zeros(self.layer_dim, CFG.batch_size, self.hidden_dim, device=x.device).requires_grad_()
        pred, _ = self.lstm(x, (h0.detach(), c0.detach()))
        return self.linear(pred)
        
        
class RNN(nn.Module): # ! GRU outperforms RNN !
    def __init__(self, input_dim, hidden_dim, layer_dim):
        super(RNN, self).__init__()
        self.hidden_dim, self.layer_dim, self.input_dim = hidden_dim, layer_dim, input_dim
        self.rnn = nn.RNN(input_dim, hidden_dim, layer_dim, batch_first=True, bidirectional=bidirectional, dropout=dropout_val)
        self.linear = nn.Linear(self.hidden_dim*num_directions, out_features=dim_out)
    
    def forward(self, x):
        pred, _ = self.rnn(x, None)
        return self.linear(pred)


class GRU(nn.Module):     # ! Best prectice : Bi-directional & multi hidden layer & nn.Tanh() as activation !
    def __init__(self, input_dim, hidden_dim, layer_dim):
        super(GRU, self).__init__()
        self.hidden_dim, self.layer_dim, self.input_dim = hidden_dim, layer_dim, input_dim
        self.gru = nn.GRU(input_dim, hidden_dim, layer_dim, batch_first=True, bidirectional=bidirectional, dropout=dropout_val)
        self.linear = nn.Linear(hidden_dim*num_directions, out_features=dim_out)
        self.act    = nn.Tanh() # Consider normalizing data to use it !!! Non-linearity effect ...
        
    def forward(self, x):
        h0 = torch.zeros(self.layer_dim*num_directions, CFG.batch_size, self.hidden_dim, device=x.device).requires_grad_()
        pred, _ = self.gru(x, h0.detach())
        return self.linear(pred) # --> self.act(2*self.linear(pred))   
