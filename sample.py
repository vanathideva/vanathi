# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:02:58 2022

@author: Tharaneesh
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import plotly.graph_objects as go
import time
from PIL import Image
from classify import predict

st.title("DUNGEONS & DRAGONS CURRENCY CALCULATOR")
image = Image.open("images/imagee.jpg")
st.image(image,use_column_width=True)
st.subheader('please input the number of coins you have for each coin type')
cu=1/100
sil=1/10
ele=1/2
gold=1
plaat=10
c=st.empty()
s=st.empty()
e=st.empty()
g=st.empty()
p=st.empty()

noofcopper = c.number_input('enter no of copper')

noofsilver = s.number_input('enter no of silver')
noofele = e.number_input('enter no of ele')
noofgold = g.number_input('enter no of gold')
noofplatinum = p.number_input('enter no of platinum')

totalgold = (noofcopper * cu) + (noofsilver * sil) + (noofele * ele) + (noofgold * gold) + (noofplatinum * plaat)
totalgold = round(totalgold)
st.subheader(f'you have {totalgold} currency pieces.')

s = [
    {"values": gold, "count": noofgold},
    {"values": cu, "count": noofcopper},
    {"values": sil, "count": noofsilver},
    {"values": ele, "count": noofele},
    {"values": plaat, "count": noofplatinum}]

 
a=pd.DataFrame(s)
st.dataframe(data=a)

st.bar_chart(data=a)
st.line_chart(a)
st.area_chart(a)


