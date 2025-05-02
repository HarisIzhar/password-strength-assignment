import streamlit as st
import re

def check_password_strength(password):
    score = 0
    messages = []

    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        messages.append("✅ Strong Password!")
    elif score == 3:
        messages.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        messages.append("❌ Weak Password - Improve it using the suggestions above.")

    return messages

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    results = check_password_strength(password)
    for msg in results:
        st.write(msg)
