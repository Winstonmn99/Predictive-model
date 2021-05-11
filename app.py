import pickle
import streamlit as st

pickle_in = open('real_model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs
def prediction(Engine_rpm,Shaft_power,Wind_speed,Current_speed):

     prediction = classifier.predict( [[Engine_rpm,Shaft_power,Wind_speed,Current_speed]])
     print(prediction)
     return prediction


def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Predictive Modelling of Ship Fuel Consumption using Machine Learning</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    Engine_rpm = st.number_input('Engine rpm')
    Shaft_power = st.number_input('Shaft power')
    Wind_speed = st.number_input("Wind speed")
    Current_speed = st.number_input("Current speed")
    result =""


    if st.button("Predict"):
        result = prediction(Engine_rpm,Shaft_power,Wind_speed,Current_speed)
        st.success('The required fuel rate is {}'.format(result))
        print(result)
    if st.button("About"):
        st.success("Developed by: Winston maben, Prajwal Kumar, M B Akash, Arsala Jamsheed.")

if __name__=='__main__':
    main()
