import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

st.title('Rental Estimation in Valencia, Spain')

House_type=st.selectbox('#### Type of house',['Piso', 'Ático', 'Dúplex', 'Estudio', 'Casa', 'Chalet'],placeholder='Piso')
Location=st.selectbox('#### District',['Aiora', 'Albors', 'Arrancapins', 'Benicalap', 'Benimaclet',
       'Campanar', 'Ciutat Jardí', 'Ciutat de les Arts i de les Ciències',
       'El Botànic', 'El Cabanyal-El Canyamelar', 'El Carme', 'El Grau',
       'El Mercat', 'El Perellonet', 'El Pilar', 'El Pla del Remei',
       'El Saler', 'Gran Via', "L'Amistat", 'La Bega Baixa',
       'La Carrasca', 'La Malva-rosa', 'La Petxina', 'La Punta',
       'La Raiosa', 'La Roqueta', 'La Seu', 'La Xerea', 'Les Tendetes',
       'Malilla', 'Mestalla', 'Montolivet', 'Morvedre', 'Nou Moles',
       'Orriols', 'Patraix', 'Penya-roja', 'Russafa', 'Sant Antoni',
       'Sant Francesc', 'Sant Pau','Other'])
Rooms=st.slider('#### Rooms',1,5,2,1)
Bathrooms=st.slider('#### Bathrooms',1,4,2,1)
Surface=st.slider('#### Surface',15,200,75,1)
st.write('#### Extras')
Furnished=st.toggle('Furnished')
Elevator=st.toggle('Elevator')
Terrace=st.toggle('Terrace')
Balcony=st.toggle('Balcony')
Storage=st.toggle('Storage')
Premium=st.toggle('Premium')

def load_preprocessor():
    return joblib.load('Rental_project_preprocessor.save')

preprocessor=load_preprocessor()

model=joblib.load('Rental_project_model.pkl')

if st.button('# Estimate rental'):

    binary_var=[Furnished,Elevator,Terrace,Balcony,Storage,Premium]   

    observation={'House_type':House_type, 'Location':Location, 'Furnished':int(Furnished), 'Elevator':int(Elevator), 'Terrace':int(Terrace), 'Balcony':int(Balcony),
       'Storage':int(Storage), 'Rooms':Rooms, 'Bathrooms':Bathrooms, 'Surface':Surface, 'Agent_cat':int(Premium)}
    
    observation={k:[v] for k,v in observation.items()}
    observation2=pd.DataFrame(observation)
    x=preprocessor.transform(observation2)
    prediction=model.predict(x)
    st.write(f'# Prediction: {round(prediction[0])} €')

    fig=plt.figure(figsize=(8,4))

    round_prediction=int(round(prediction[0],-2))

    plt.errorbar(0,round_prediction,300,fmt='s',linewidth=5,capsize=0,markersize=24,ecolor='grey',capthick=5,color='teal')

    x=[-0.3,0.9]
    range1=[round_prediction-300,round_prediction-300]
    range2=[260,260]
    range3=[80,80]
    range4=[260,260]
    y=np.vstack([range1, range2, range3, range4])
    plt.stackplot(x,y,colors=['w','lightgrey','teal','lightgrey'],alpha=0.5)

    plt.axhline(round_prediction+300,color='grey',linewidth=2,linestyle='--')
    plt.axhline(round_prediction-300,color='grey',linewidth=2,linestyle='--')

    plt.annotate(f'Max value: {round_prediction+300} €',xy=(0.22,0.85),xycoords='axes fraction',fontsize=15)
    plt.annotate(f'{round_prediction} €',xy=(0.25,0.46),xycoords='axes fraction',fontsize=25,fontweight='bold')
    plt.annotate(f'Min value: {round_prediction-300} €',xy=(0.22,0.11),xycoords='axes fraction',fontsize=15)

    plt.title('Estimated range',fontsize=20,fontweight='bold')
    plt.xticks([])
    plt.xlim(-0.2,0.8)
    plt.ylim(round_prediction-340,round_prediction+340)
    plt.ylabel('Price (€)')

    st.pyplot(fig)
    

