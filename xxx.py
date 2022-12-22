
import streamlit as st
import pandas as pd


heading=st.container()

dataset=st.container()


with heading:
    st.title('Welcome to our dashboard')
    st.markdown('We will help you filter data and understand insights')

with dataset:
    st.header('Please choose the options below to get your desired result')
    data=pd.read_csv('samplepython.csv',skipfooter=2,engine='python')
    a=st.slider('What is the minimum clicks value you need',min_value=4000,max_value=90000,value=30000,step=5000)
    b=st.text_input('What do you want to evaluate','Clicks')
    c=st.selectbox('Choose the number of rows you want', options=[5,6,7],index=0)
    datanew=data[data['Clicks']>=a]
    datanew1=datanew.groupby('Category')[b].sum()
    datanew1=datanew1.to_frame(name=b)

    st.write(datanew1.head(n=c))
    st.bar_chart(datanew1.head())


    @st.cache
    def convert_df_to_csv(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')


    st.download_button(
        label="Download data as CSV",
        data=convert_df_to_csv(data),
        file_name='rawdata.csv',
        mime='text/csv',
    )
