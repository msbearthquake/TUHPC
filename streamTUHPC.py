import   streamlit  as st; from PIL import Image; import numpy  as np
import pandas  as pd; import pickle

import os

filename1 = 'https://raw.githubusercontent.com/msbearthquake/TUHPC/main/Capture1.PNG'
filename2 = 'https://raw.githubusercontent.com/msbearthquake/TUHPC/main/Capture2.PNG'

st.title('Tensile behavior of UHPC  ')
with st.container():
    st.image(filename1)
    st.image(filename2)

## 
x1  = st.number_input('Fiber Type (1 for Steel fibers, 0 for Hybrid):',0.0)
x2p = st.number_input('Fiber Volume (%):',0.0)
x2 = x2p/100
x3 = st.number_input('Length of Fiber (in):',0.0)
x4 = st.number_input('Diameter of Fiber (in):',0.0)
x5 = st.number_input('RI index:',0.0)
x6 = st.number_input('Compressive Strength (ksi):',0.0)

##
x1_tval = (2*(x1 - 0) / ( 1 ))-1
x2_tval = (2*(x2 - 0) / ( 0.05 - 0 ))-1
x3_tval = (2*(x3 - 0.5) / ( 2.44 - 0.5 ))-1
x4_tval = (2*(x4 - 0.0011) / ( 0.031 - 0.0011 ))-1
x5_tval = (2*(x5 - 0) / ( 9.09 - 0 ))-1
x6_tval = (2*(x6 - 8.127) / ( 45.396 - 8.127 ))-1

inputvec = np.array([x1_tval, x2_tval, x3_tval, x4_tval, x5_tval, x6_tval])


filename3 = 'FCS.pkl'
filename4 = 'SFC.pkl'
filename5 = 'PCS.pkl'
filename6 = 'SPC.pkl'



### save the model to disk
# pickle.dump(model, open(filename, 'wb'))
 
### some time later...
### load the model from disk


with st.container():

    if st.button('Run'):
        if x2!=0 and x5!=0:
            loaded_model1 = pickle.load(open(filename3, 'rb'))
            loaded_model2 = pickle.load(open(filename4, 'rb'))
            loaded_model3 = pickle.load(open(filename5, 'rb'))
            loaded_model4 = pickle.load(open(filename6, 'rb'))

            yhat1 = loaded_model1.predict(inputvec.reshape(1, -1))
            FCS_real = (yhat1+1) * (2320.603 - 304.580 ) * (1/2) + 304.580

            yhat2 = loaded_model2.predict(inputvec.reshape(1, -1))
            SFC_real = (yhat2+1) * (5800.0- 0.0 ) * (1/2) + 0.0

            yhat3 = loaded_model3.predict(inputvec.reshape(1, -1))
            PCS_real = (yhat3+1) * (3495.00- 304.58 ) * (1/2) + 304.58

            yhat4 = loaded_model4.predict(inputvec.reshape(1, -1))
            SPC_real = (yhat4+1) * (48000.00- 0.0 ) * (1/2) + 0.0

            


            st.write("First cracking Strees (psi): " , np.round(FCS_real, decimals=4))
            st.write("Strain at the first cracking (µ ε): " , np.round(SFC_real, decimals=4))
            st.write("Post-cracking stress (psi): " , np.round(PCS_real, decimals=4))
            st.write("Strain at post-cracking (µ ε): " , np.round(SPC_real, decimals=4))



        else:
            st.write("Fiber Volume, RI index and Compressive Strength should not be zero.")

# st.write(trainx)

filename7 = 'https://raw.githubusercontent.com/msbearthquake/TUHPC/main/Capture3.PNG'
filename8 = 'https://raw.githubusercontent.com/msbearthquake/TUHPC/main/Capture4.PNG'


with st.container():
    st.header("Developer:")

    st.image(filename8)
 


with st.container():
    st.header("Supervisor:")

    st.image(filename7)