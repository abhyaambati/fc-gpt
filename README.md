# 🧐 fc-gpt: AI Fact Verifier

## 📌 Overview
**fc-gpt** is an AI-powered fact verification system that checks the truthfulness of a claim by retrieving evidence and analyzing it using **GPT-3.5 Turbo** and **RoBERTa-based Natural Language Inference (NLI)**.  

The system is designed to be **accurate, strict, and reliable**, reducing false positives while correctly verifying factual claims.


## 🏗️ Project Structure
```
fc-gpt/
│-- backend/            # FastAPI backend
│   ├-- main.py         # API server handling requests
│   ├-- retrieval.py    # Retrieves evidence from the web
│   ├-- explanation.py  # Fact-checking using GPT & NLI
│   ├-- config.py       # Stores API keys
│   ├-- requirements.txt # Backend dependencies
│-- frontend/           # Streamlit-based UI
│   ├-- app.py         # Main frontend file
│   ├-- requirements.txt # Frontend dependencies
│-- README.md           # Documentation
```


## 🎨 Running the Frontend (Streamlit UI)
### **1️⃣ Set Up the Frontend**
```sh
cd frontend
pip install -r requirements.txt
```

### **2️⃣ Run the UI**
```sh
streamlit run app.py
```
- **Frontend runs at**: `http://localhost:8501`
- Enter a claim in the text box and click **"Verify Claim"** to see results.

---

## How It Works

### **1️⃣ Evidence Retrieval**
- Uses **SerpAPI (Google Search API)** to find **relevant sources**.
- Extracts the most relevant snippet of **factual information**.

### **2️⃣ Fact-Checking with AI**
- **First Step:** **GPT-3.5 Turbo** analyzes whether the claim is **fully supported**, **contradicted**, or **inconclusive**.
- **Second Step (if needed):** **RoBERTa (NLI)** checks if the evidence **entails, contradicts, or is neutral** to the claim.
- If both models are unsure, it **returns "Unknown".**

### **3️⃣ Response Format**
The system provides:
- **Claim:** What the user entered.
- **Evidence:** The most relevant factual snippet.
- **Result:** ✅ **True**, ❌ **False**, ⚠️ **Unknown**

---

## 📜 API Reference

### **1️⃣ Fact-Check Endpoint**
#### **`POST /fact-check`**
Verifies a claim's accuracy based on evidence.

📌 **Example Request:**
```json
{
  "claim": "The Eiffel Tower is in Paris."
}
```

📌 **Example Response:**
```json
{
  "claim": "The Eiffel Tower is in Paris.",
  "evidence": "The Eiffel Tower is a famous landmark located in Paris, France.",
  "is_true": true
}
```


## 📌 Future Improvements
✅ **Improve Accuracy** – Tune GPT and NLI models for better fact-checking.  
✅ **Customizable Model Selection** – Allow users to choose different AI models.  
✅ **More Data Sources** – Expand retrieval to Wikipedia, News APIs, and more.  
✅ **Mobile Support** – Improve UI for usability on mobile devices.  



