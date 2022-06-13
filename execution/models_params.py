def LSTM_params():
	dim_input, dim_layers, dim_hidden = 3, 1, 40
	return (dim_input, dim_hidden, dim_layers)
	
def RNN_params():
	dim_input, dim_layers, dim_hidden = 3, 1, 65
	return (dim_input, dim_hidden, dim_layers)

def GRU_params():
	dim_input, dim_layers, dim_hidden = 3, 1, 25
	return (dim_input, dim_hidden, dim_layers)

