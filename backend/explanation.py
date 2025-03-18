import openai
from config import OPENAI_API_KEY
from transformers import pipeline

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Load the Natural Language Inference (NLI) model
nli_model = pipeline("text-classification", model="roberta-large-mnli")

def check_claim_truthfulness_gpt(claim, evidence):
    """
    Uses GPT-3.5 Turbo to determine if a claim is true or false based on the evidence.
    Returns:
        - True if the claim is fully supported by strong evidence.
        - False if the claim is contradicted by the evidence.
        - 'Unknown' if the evidence is weak or neutral.
    """
    prompt = f"""
    You are an expert fact-checking AI with strict verification standards. Your job is to determine whether a claim is TRUE or FALSE based on provided evidence.

    Question: "{claim}"
    Answer: "{evidence}"

    Carefully evaluate this:
    - If the evidence **directly and strongly supports the claim**, respond ONLY with 'True'.
    - If the evidence **clearly contradicts or disproves the claim**, respond ONLY with 'False'.
    - If the evidence is **weak, indirect, missing key details, or unclear**, respond with 'Unknown'.

    STRICT RULES:
    - You MUST respond with exactly 'True', 'False', or 'Unknown'.
    - Do NOT assume truth if the evidence is indirect or incomplete.
    - If the claim is only partially supported or lacks confirmation, respond with 'Unknown'.
    - Do NOT provide explanations or additional text.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "system", "content": prompt}]
        )
        result = response["choices"][0]["message"]["content"].strip().lower()

        print(f"DEBUG: GPT-3.5 Response -> {result}")  # Debugging Output

        if result == "true":
            return True
        elif result == "false":
            return False
        else:
            return "Unknown"

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return "Unknown"

def nli_fact_check(claim, evidence):
    """
    Uses Natural Language Inference (NLI) to verify if the claim is supported by the evidence.
    Returns:
        - True if the evidence strongly supports the claim.
        - False if the evidence contradicts the claim.
        - 'Unknown' if the evidence is neutral or unclear.
    """
    input_text = f"Claim: {claim} Evidence: {evidence}"
    result = nli_model(input_text)

    label = result[0]['label'].lower()
    print(f"DEBUG: NLI Response -> {label}")  # Debugging Output

    if label == "entailment":  # Evidence strongly supports claim
        return True
    elif label == "contradiction":  # Evidence contradicts claim
        return False
    elif label == "neutral":  # Neutral = Not strong enough evidence
        return "Unknown"
    else:
        return "Unknown"

def check_claim_truthfulness(claim, evidence):
    """
    Uses GPT-3.5 Turbo to determine if a claim is true or false. If unclear, falls back to NLI.
    """
    gpt_result = check_claim_truthfulness_gpt(claim, evidence)

    if gpt_result != "Unknown":
        return gpt_result  # If GPT is confident, return its answer

    # If GPT is unsure, use NLI
    return nli_fact_check(claim, evidence)
