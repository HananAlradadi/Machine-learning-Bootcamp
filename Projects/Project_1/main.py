import streamlit as st
import pandas as pd
import pickle
import os
st.title('car price predicted')
st.write('# car price predicted')  
st.markdown('''
Welcome, come to discover the exact prices of cars.  No more being scammed when buying or selling a car.  Thanks to the magic of machine learning'''
)

final_model = pickle.load(open(os.path.abspath('Projects/Project_1/final_model.sav'), 'rb'))



data = pd.read_csv((os.path.abspath('Projects/Project_1/'cleaneData.csv'))
with st.form("my_form"):
   make_model = st.selectbox('Select the model of your car',data['make_model'].unique() )
   power_kW = st.number_input('Enter the horsepower of your car')
   engine_size = st.number_input('Enter engine size of your car')
   mileage = st.number_input('Enter mileage size of your car')
   age = st.number_input('Enter age size of your car')
   type = st.selectbox('Select the type of your car', data['type'].unique())
   submitted = st.form_submit_button('Submit')

if submitted :
    df = pd.DataFrame.from_dict([{
        "type": type,
        "power_kW": power_kW,
        "make_model": make_model,
        "engine_size": engine_size,
        "mileage": mileage,
        "age": age
    }])
    re = final_model.predict(df)[0].__round__(2)
    if re <= 0 :
        st.error('Please enter realistic values.')

    else :
        st.text('the predicted of car price is: ')
        st.success(re)



