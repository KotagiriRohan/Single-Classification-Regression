import re
import numpy as np
import pandas as pd
from  PIL import Image
from IPython.display import display
X = np.empty((40,401))
def data_collection():
    for i in range(1,21):
        var = 'Apple_image/apple'+str(i)+'.jfif' 
        image = Image.open(var).resize((20,20)).convert('L')
        x = np.array(image).reshape((1,400))
        X[i-1,0] = 1
        X[i-1,1:] = x[0]
    for j in range(1,21):
        var2 = 'Not_Apple/notapple'+str(i)+'.jfif' 
        image2 = Image.open(var2).resize((20,20)).convert('L')
        x2 = np.array(image2).reshape((1,400))
        X[i+19,0] = 1
        X[i+19,1:] = x2[0]
    Y = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]).reshape((40,1))
    iden = np.identity(401)
    iden[0,0] = 0
    lam = 0.001
    theta = np.linalg.inv(((X.T)@X))@((X.T)@Y)
    #print(theta)
    return theta

#data_collection()

def hypothosis():
    theta = data_collection()
    img = Image.open("cutapple.jfif").resize((20,20)).convert('L')
    k = np.array(img).reshape((1,400))
    arr = np.empty((1,401))
    arr[0,0] = 1
    arr[0,1:] = k
    z = arr@theta
    e = np.finfo(float).eps
    h_theta = 1/(1+np.power(e,-z))
    if(h_theta < 0.5):
        print("it is not an apple", float(h_theta))
    else:
        print("It is an apple" , float(h_theta))
    return h_theta

hypothosis()