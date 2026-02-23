import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker",page_icon="🔒")

st.title("🔒 Password Strength Checker")

st.markdown("""
## welcome to the ultimate password strength checker
 use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
 we will give you helpful tips to create a strong password""")

password = st.text_input("Enter your password", type="password")


feedback = []

score = 0

# Length Check
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")

    if feedback:
        st.markdown("## Improvment Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("please enter your password to get started.")
