from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retrieval import retrieve_evidence
from explanation import check_claim_truthfulness

app = FastAPI()

class ClaimRequest(BaseModel):
    claim: str

@app.post("/fact-check")
def fact_check_api(request: ClaimRequest):
    try:
        # Retrieve evidence from search
        evidence = retrieve_evidence(request.claim)

        # Validate that evidence exists
        if not evidence or evidence == "No relevant evidence found.":
            return {
                "claim": request.claim,
                "evidence": "No relevant evidence found.",
                "is_true": "Unknown"
            }

        # Determine if the claim is true or false based on evidence
        is_true = check_claim_truthfulness(request.claim, evidence)

        return {
            "claim": request.claim,
            "evidence": evidence,
            "is_true": is_true
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# Run FastAPI server if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
