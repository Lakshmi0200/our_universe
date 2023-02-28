import streamlit as st
import requests
from matplotlib import image
import os
st.title("space and time")
day = st.slider('select date of your DOB.', 1, 31, 17)

month = st.selectbox(
    'Select month of DOB',
    ('jan', 'feb', 'mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))

if month == 'dec':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'jan':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'feb':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'mar':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'apr':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'jun':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'jul':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'aug':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'sep':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'oct':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'nov':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
st.write("Your Astrological sign is :",astro_sign)
