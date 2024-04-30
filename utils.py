import base64
import os

def write_data(file_name, data):
    if type(data) == bytes:
        #bytes to base64
        data = base64.b64encode(data)
    os.makedirs(os.path.dirname(file_name), exist_ok=True)    
    with open(file_name, 'wb') as f: 
      
        f.write(data)
 
def read_data(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        
    #base64 to bytes
    return base64.b64decode(data)