
import streamlit as st
import requests


st.set_page_config(
    page_title="Mental Health Score Predictor",
    page_icon="🧠",
    layout="centered"
)


st.title("🧠 Mental Health Score Predictor")
st.write("Enter your information to predict your mental health score.")


age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20
)


gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


country = st.text_input(
    "Country",
    placeholder="Enter your country"
)


academic_level = st.selectbox(
    "Academic Level",
    ["Undergraduate", "Graduate", "High School"]
)


most_used_platform = st.selectbox(
    "Most Used Platform",
    [
        "Facebook",
        "LinkedIn",
        "Instagram",
        "Snapchat",
        "Twitter",
        "YouTube",
        "TikTok",
        "LINE",
        "KakaoTalk",
        "VKontakte",
        "WhatsApp",
        "WeChat"
    ]
)


purpose_of_use = st.selectbox(
    "Purpose Of Use",
    [
        "Networking",
        "Education",
        "Entertainment",
        "News"
    ]
)


avg_daily_usage_hours = st.number_input(
    "Average Daily Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)


daily_unlocks = st.number_input(
    "Daily Unlocks",
    min_value=0,
    value=10
)


study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)


physical_activity_hours = st.number_input(
    "Physical Activity Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)


sleep_hours_per_night = st.number_input(
    "Sleep Hours Per Night",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)


stress_level = st.selectbox(
    "Stress Level",
    [
        "Medium",
        "Low",
        "Very High",
        "High"
    ]
)


if st.button("Predict Mental Health Score"):

    if not country.strip():

        st.warning("Please enter your country.")

    else:

        data = {
            "age": age,
            "gender": gender,
            "country": country.strip(),
            "academic_level": academic_level,
            "most_used_platform": most_used_platform,
            "purpose_of_use": purpose_of_use,
            "avg_daily_usage_hours": avg_daily_usage_hours,
            "daily_unlocks": daily_unlocks,
            "study_hours": study_hours,
            "physical_activity_hours": physical_activity_hours,
            "sleep_hours_per_night": sleep_hours_per_night,
            "stress_level": stress_level
        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=data
            )

            if response.status_code == 200:

                result = response.json()

                score = result["predicted_mental_health_score"]

                st.success("Prediction completed!")

                st.metric(
                    "Predicted Mental Health Score",
                    score
                )

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

                st.write(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                "FastAPI server is not running. "
                "Please start FastAPI first."
            )

