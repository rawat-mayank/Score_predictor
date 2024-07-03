import streamlit as st
import pickle



model = pickle.load(open("model.pkl", "rb"))

teams=[
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka',
    'Netherlands']


st.title('Cricket Score Predictor')
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))



col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five_runs = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 300 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs
    if batting_team == 'Australia':
        batting_team = 1
    if batting_team == 'India':
        batting_team = 4
    if batting_team == 'Bangladesh':
        batting_team = 2
    if batting_team == 'New Zealand':
        batting_team = 6
    if batting_team == 'South Africa':
        batting_team = 8
    if batting_team == 'England':
        batting_team = 3
    if batting_team == 'Afghanistan':
        batting_team = 0
    if batting_team == 'Pakistan':
        batting_team = 7
    if batting_team == 'Sri Lanka':
        batting_team = 9
    if batting_team == 'Netherlands':
        batting_team = 5
    if bowling_team == 'Australia':
        bowling_team = 1
    if bowling_team == 'India':
        bowling_team = 4
    if bowling_team == 'Bangladesh':
        bowling_team = 2
    if bowling_team == 'New Zealand':
        bowling_team = 6
    if bowling_team == 'South Africa':
        bowling_team = 8
    if bowling_team == 'England':
        bowling_team = 3
    if bowling_team == 'Afghanistan':
        bowling_team = 0
    if bowling_team == 'Pakistan':
        bowling_team = 7
    if bowling_team == 'Sri Lanka':
        bowling_team = 9
    if bowling_team == 'Netherlands':
        bowling_team = 5


    features = [[batting_team, bowling_team, overs, current_score, balls_left, wickets, crr,
                 last_five_runs]]

    # Make a prediction
    prediction = model.predict(features)

    # Display the prediction result
    st.write(f"Predicted Total Score: {int(prediction[0])}")

