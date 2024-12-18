import streamlit as st

def calculate_stroke_risk(age, glucose, bmi):
    risk_score = 0
    max_score = 12

    # Age 점수
    if age >= 65:
        risk_score += 4
    elif age >= 40:
        risk_score += 3
    elif age >= 19:
        risk_score += 2
    elif age >= 12:
        risk_score += 1

    # Glucose 점수
    if glucose > 100:
        risk_score += 4
    elif glucose < 70:
        risk_score += 2

    # BMI 점수
    if bmi >= 30:
        risk_score += 4
    elif bmi >= 25:
        risk_score += 3
    elif bmi < 18.5:
        risk_score += 1

    risk_percentage = (risk_score / max_score) * 100
    return risk_percentage

st.title("Stroke Risk Calculator")
age = st.number_input("Enter your Age:", min_value=1, max_value=120, value=30)
glucose = st.number_input("Enter your Glucose Level (mg/dL):", min_value=50.0, max_value=300.0, value=90.0)
bmi = st.number_input("Enter your BMI:", min_value=10.0, max_value=50.0, value=22.0)

if st.button("Calculate Risk"):
    risk = calculate_stroke_risk(age, glucose, bmi)
    st.write(f"Your estimated stroke risk is {risk:.1f}%")
