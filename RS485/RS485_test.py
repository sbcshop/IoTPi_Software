from IoTPi import RS485

# Uncomment below block of code(remove '''  ''') to make IoTPi receiver

'''
############## Data receive ###
data = RS485()
data.RS485_Receive()
print(data.RS485_Receive())
###############################
'''



# Uncomment below block of code to make IoTPi sender
'''
############ Data send ########
tx = "hello"
data = RS485()
data.RS485_Send(tx)
###############################
'''