from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import difflib

# Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Load synthetic recipes database
RECIPES_DB = []
try:
    with open(os.path.join(os.path.dirname(__file__), "recipes.json"), "r") as f:
        RECIPES_DB = json.load(f)
except Exception as e:
    print("Warning: Could not load recipes.json", e)

# Recipe API Route
@app.route("/recipe", methods=["POST"])
def recipe():
    try:
        # Get frontend data
        data = request.get_json()
        query = data.get("recipe", "").lower()

        if not query:
            raise ValueError("Empty recipe query")

        # Create a dictionary mapping titles to their full recipe objects
        # We also create a searchable list of titles and keywords combined
        search_terms = {}
        for r in RECIPES_DB:
            title = r.get("title", "").lower()
            keywords = [kw.lower() for kw in r.get("keywords", [])]
            
            # Allow searching by exact title
            search_terms[title] = r
            
            # Allow searching by combined keywords (e.g. "spicy chicken")
            kw_string = " ".join(keywords)
            search_terms[kw_string] = r

        # Perform fuzzy search using difflib
        # First, try to match against titles and keyword strings
        all_terms = list(search_terms.keys())
        matches = difflib.get_close_matches(query, all_terms, n=1, cutoff=0.4)

        if matches:
            best_match_key = matches[0]
            recipe_data = search_terms[best_match_key]
            
            # Format to match frontend expectations
            response_json = {
                "name": recipe_data.get("title", "Unknown Recipe"),
                "description": recipe_data.get("description", ""),
                "prep": recipe_data.get("prep", "10 mins"),
                "cook": recipe_data.get("cook", "20 mins"),
                "ingredients": recipe_data.get("ingredients", []),
                "steps": recipe_data.get("steps", [])
            }
            return jsonify(response_json)
        
        else:
            # Fallback if no similar recipe is found in the local database
            return jsonify({
                "name": query.title(),
                "description": "Recipe not found in local database. Try asking for Pizza, Biryani, Pasta, or something like 'Spicy Chicken Curry'.",
                "prep": "0 mins",
                "cook": "0 mins",
                "ingredients": ["Not found"],
                "steps": ["Try another search term."]
            })

    except Exception as e:
        print("ERROR:", e)
        # Fallback error response
        return jsonify({
            "name": "System Error",
            "description": f"Internal Error: {str(e)}",
            "prep": "0 mins",
            "cook": "0 mins",
            "ingredients": ["Error Occurred"],
            "steps": ["Please check your server logs."]
        })

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True, port=5001)