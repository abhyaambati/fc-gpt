from serpapi import GoogleSearch
from config import SERPAPI_KEY

def retrieve_evidence(query):
    """ Fetch relevant search results using SerpAPI. """
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        if "organic_results" in results and len(results["organic_results"]) > 0:
            snippets = [result['snippet'] for result in results["organic_results"]]
            return snippets[0]  # Return the most relevant snippet
        else:
            return "No relevant evidence found."

    except Exception as e:
        return f"Error fetching evidence: {str(e)}"

# Test retrieval
if __name__ == "__main__":
    print(retrieve_evidence("NASA landed on the Moon in 1969"))
