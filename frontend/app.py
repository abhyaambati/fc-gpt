import streamlit as st
import requests

# Set page title and layout
st.set_page_config(page_title="fc-gpt: AI Fact Verifier", layout="wide")

# Page title
st.title("🧐 fc-gpt: AI Fact Verifier")
st.write("Enter a claim below and let AI verify its accuracy.")

# Input field for the claim
claim = st.text_input("Enter a claim:")

if st.button("Verify Claim"):
    if claim:
        try:
            st.write("🔄 Sending request to backend...")  # Debug log
            response = requests.post("http://127.0.0.1:8000/fact-check", json={"claim": claim})
            st.write(f"📡 Response Status: {response.status_code}")  # Debug log

            if response.status_code == 200:
                result = response.json()
                st.subheader("🔍 Fact-Check Results:")
                st.write(f"**Claim:** {result['claim']}")
                st.write(f"**Evidence:** {result['evidence']}")

                # Show result based on "is_true" field
                if result["is_true"] == True:
                    st.success("✅ **Claim is TRUE.**")
                elif result["is_true"] == False:
                    st.error("❌ **Claim is FALSE.**")
                else:
                    st.warning("⚠️ **Not enough evidence to determine truthfulness.**")

            else:
                st.error("❌ Error: Could not get a response from the backend. Is the API running?")
        except Exception as e:
            st.error(f"⚠️ Exception: {str(e)}")
    else:
        st.warning("⚠️ Please enter a claim first.")
