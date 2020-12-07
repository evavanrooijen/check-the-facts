import streamlit as st
import pandas as pd
import numpy as np

st.title(""" Check the Facts: Analyses""" )


st.write('Analyse van het aantal ingeschreven studenten voor WO opleidingen tussen 2010 en 2019.')
st.write('Een onderzoeksvraag is: "Wat is het effect van de invoering van het leenstelsel in 2015 op het aantal inschrijvingen in verschillende sectoren?"')

# Collect data, aggregate number of students
data = pd.read_csv('data/wo_inges_ho.csv', delimiter=';')

# Sidebar Options for further details
st.sidebar.title('Analyse Opties')
type_data = st.sidebar.radio('Analyseer de/het ... van ingeschrevenen', ('Groei', 'Aantal'))
#st.sidebar.text('We analyseren de groei')
#st.sidebar.text(' van het aantal studenten')

onderzoeksvraag = st.sidebar.radio('Onderzoeksvraag/Filter', ('INTRO', 'GESLACHT', 'PROVINCIE', 'OPLEIDINGSVORM'))
totals = st.sidebar.checkbox('Laat ook totale aantallen zien')
#time_horizon = st.sidebar.slider('Startjaar', 2010, 2019, 2010)

CROHO_select = st.sidebar.selectbox(
    "Selecteer CROHO onderdeel:",
    ("economie", "recht", "onderwijs", "natuur", "techniek")
)

if onderzoeksvraag == 'PROVINCIE':
    provincie = st.sidebar.selectbox(
        "Selecteer een provincie:",
        (data['PROVINCIE'].unique())
    )
    st.title('Is het aantal studenten in {} toegenomen?'.format(provincie))
    # plot sum studenten over 2015-2019
    #st.table(data['PROVINCIE'== provincie])

    st.table(data.groupby('PROVINCIE')['2018', '2019'].sum())

    opleiding = st.sidebar.selectbox(
        "Selecteer opleiding:",
        data.loc[data['CROHO ONDERDEEL'] == CROHO_select]['OPLEIDINGSNAAM ACTUEEL'].unique()
    )

    st.title('Waar wordt deze studie aangeboden?')
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)


if onderzoeksvraag == 'OPLEIDINGSVORM':
    vorm = st.sidebar.selectbox(
        "Selecteer type opleiding:",
        ("bachelor", "master", 'ongedeelde opleiding', 'postmaster')
    )

    opleiding = st.sidebar.selectbox(
    "Selecteer opleiding:",
    data.loc[data['CROHO ONDERDEEL'] == CROHO_select].loc[data['TYPE HOGER ONDERWIJS'] == vorm]['OPLEIDINGSNAAM ACTUEEL'].unique())



if totals:
    st.title('Totale aantal ingeschreven WO-studenten')
    time_series = data.iloc[:,-10:].sum()
    st.line_chart(time_series)

    student_growth = np.diff(time_series.values)
    st.line_chart(student_growth)

## MAke this dependent on the choice for onderdeel
#st.title('Analyse voor CROHO onderdeel: {}'.format(CROHO_select))
#st.text('Gemiddelde aantal studenten was .. voor leenstelsel en is ... erna.')
#st.text('Gemiddelde studentengroei per jaar was ..., na 2015 (invoering leenstelsel) werd dat ... .')

# Growth per CROHO
students_per_croho = data.drop(['GEMEENTENUMMER', 'OPLEIDINGSCODE ACTUEEL'], axis=1).groupby('CROHO ONDERDEEL').sum()

if totals == True:
    st.title('Totaal aantal studenten: {}'.format(CROHO_select))
    st.line_chart(students_per_croho.loc[CROHO_select])


if onderzoeksvraag == 'GESLACHT':
    opleiding = st.sidebar.selectbox(
        "Selecteer opleiding:",
        data.loc[data['CROHO ONDERDEEL'] == CROHO_select]['OPLEIDINGSNAAM ACTUEEL'].unique()
    )
    sector_geslacht = data.drop(['GEMEENTENUMMER', 'OPLEIDINGSCODE ACTUEEL'], axis=1).groupby(['CROHO ONDERDEEL', onderzoeksvraag]).sum()
    st.title('Groei mannen vs vrouwen: {}'.format(CROHO_select))
    st.line_chart(pd.concat([sector_geslacht.diff(axis=1).loc[CROHO_select].loc['man'], sector_geslacht.diff(axis=1).loc[CROHO_select].loc['vrouw']], axis=1))

# Perform RDD
## Growth Factor (from regression beta) for period prior == Growth Factor after period 

# Interpret results, write conclusion
