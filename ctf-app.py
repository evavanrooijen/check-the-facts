import streamlit as st
import pandas as pd
import numpy as np

st.title(""" Hello World!""" )
st.write( """
Let's check some facts!
""" )

st.write('Analyse van het aantal ingeschreven studenten voor WO opleidingen tussen 2010 en 2019. Een onderzoeksvraag is: "Wat is het effect van de invoering van het leenstelsel in 2015 op het aantal inschrijvingen in verschillende sectoren?"')

# Collect data, aggregate number of students
data = pd.read_csv('wo_inges_ho.csv', delimiter=';')

# Sidebar Options for further details
st.sidebar.title('Analyse Opties')
st.sidebar.text('We analyseren de groei')
st.sidebar.text(' van het aantal studenten')

onderzoeksvraag = st.sidebar.radio('Onderzoeksvraag/Filter', ('GESLACHT', 'PROVINCIE'))
totals = st.sidebar.checkbox('Laat ook totale aantallen zien')
time_horizon = st.sidebar.slider('Startjaar', 2010, 2019, 2010)

CROHO_select = st.sidebar.selectbox(
    "Selecteer CROHO onderdeel:",
    ("economie", "recht", "onderwijs", "natuur", "techniek")
)

if totals:
    st.title('Totale aantal ingeschreven WO-studenten')
    time_series = data.iloc[:,-10:].sum()
    st.line_chart(time_series)

    student_growth = np.diff(time_series.values)
    st.line_chart(student_growth)


st.title('Analyse voor CROHO onderdeel: {}'.format(CROHO_select))
st.text('Gemiddelde aantal studenten was .. voor leenstelsel en is ... erna.')
st.text('Gemiddelde studentengroei per jaar was ..., na 2015 (invoering leenstelsel) werd dat ... .')

# Growth per CROHO
students_per_croho = data.drop(['GEMEENTENUMMER', 'OPLEIDINGSCODE ACTUEEL'], axis=1).groupby('CROHO ONDERDEEL').sum()

if totals == True:
    st.title('Totaal Aantal Studenten')
    st.line_chart(students_per_croho.loc[CROHO_select])


if onderzoeksvraag == 'GESLACHT':
    sector_geslacht = data.drop(['GEMEENTENUMMER', 'OPLEIDINGSCODE ACTUEEL'], axis=1).groupby(['CROHO ONDERDEEL', onderzoeksvraag]).sum()
    st.title('Groei mannen vs vrouwen: {}'.format(CROHO_select))
    st.line_chart(pd.concat([sector_geslacht.diff(axis=1).loc[CROHO_select].loc['man'], sector_geslacht.diff(axis=1).loc[CROHO_select].loc['vrouw']], axis=1))

# Perform RDD
## Growth Factor (from regression beta) for period prior == Growth Factor after period 

# Interpret results, write conclusion
