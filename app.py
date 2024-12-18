# Data mining final project group 5
import streamlit as st

def calculate_stroke_risk(age, glucose, bmi):
    risk_score = 0
    max_score = 12

    # Age score
    if age >= 65:
        risk_score += 4
    elif age >= 40:
        risk_score += 3
    elif age >= 19:
        risk_score += 2
    elif age >= 12:
        risk_score += 1

    # Glucose score
    if glucose > 100:
        risk_score += 4
    elif glucose < 70:
        risk_score += 2

    # BMI score
    if bmi >= 30:
        risk_score += 4
    elif bmi >= 25:
        risk_score += 3
    elif bmi < 18.5:
        risk_score += 1

    risk_percentage = (risk_score / max_score) * 100
    return risk_percentage

# Stroke Risk
def get_risk_level(risk):
    if risk < 25:
        return "Low", "green"
    elif risk < 50:
        return "Medium", "orange"
    elif risk < 75:
        return "High", "darkorange"
    else:
        return "Very High", "red"

# Age, BMI, Glucose Catogory
def get_age_category(age):
    if age <= 11: return "Children and under"
    elif age <= 18: return "Adolescent"
    elif age <= 39: return "Young adult"
    elif age <= 64: return "Middle adult"
    else: return "Older adult"

def get_bmi_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Healthy Weight"
    elif bmi < 30: return "Overweight"
    else: return "Obese"

def get_glucose_category(glucose):
    if glucose < 70: return "Low Glucose"
    elif glucose <= 100: return "Healthy Glucose"
    else: return "High Glucose"

# Streamlit UI
st.title("🩺 Stroke Risk Calculator")

# Fieald
age = st.number_input("Age", min_value=1, max_value=120, value=51)
glucose = st.number_input("Glucose Level", min_value=30.0, max_value=300.0, value=31.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)

# Category
st.write(f"**Category**: {get_age_category(age)}")
st.write(f"**Category**: {get_glucose_category(glucose)}")
st.write(f"**Category**: {get_bmi_category(bmi)}")

# Calculation Button
if st.button("Calculate Risk"):
    risk_percentage = calculate_stroke_risk(age, glucose, bmi)
    risk_level, color = get_risk_level(risk_percentage)

    # Result make
    st.markdown(f"""
    <div style="border:1px solid #ddd; padding:10px; border-radius:10px;">
        <h3 style="color: {color};">Estimated Risk: {risk_percentage:.1f}%</h3>
        <h4 style="color: {color};">Risk Level: {risk_level}</h4>
        <p>Key Risk Factors:</p>
        <ul>
            <li>Age Category: {get_age_category(age)}</li>
            <li>Glucose Level Category: {get_glucose_category(glucose)}</li>
            <li>BMI Category: {get_bmi_category(bmi)}</li>
        </ul>
        <p style="font-size:12px; color:gray;">
        * This calculator was created for the Datamining Final Project. Please consult a doctor for accurate diagnosis.
        </p>
    </div>
    """, unsafe_allow_html=True)

