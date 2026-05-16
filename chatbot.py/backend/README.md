# 🍳 SmartChef AI

SmartChef AI is an AI-powered recipe chatbot that provides cooking recipes using a synthetic dataset and a retrieval-based search system.

---

# 🚀 Project Overview

SmartChef AI is a full-stack AI chatbot project developed using:

- HTML
- CSS
- JavaScript
- Python
- Flask

The chatbot allows users to search for recipes and receive cooking instructions instantly through a smart dataset retrieval system.

The frontend was designed using HTML, CSS, and JavaScript, while the backend was developed using Python Flask.

This project demonstrates how synthetic data can be used to build an intelligent chatbot without depending completely on external AI APIs.

---

# 🤖 What is Synthetic Data?

Synthetic data is artificially created data that is manually generated or programmatically created instead of collected from real-world users.

In this project, synthetic data is used to create a recipe database for the chatbot.

The synthetic dataset contains:
- Recipe titles
- Keywords
- Ingredients
- Preparation time
- Cooking time
- Cooking instructions

The chatbot searches this dataset and returns the most relevant recipe based on the user's query.

---

# 📂 Synthetic Dataset Structure

The synthetic dataset is stored in:


# ⚡ How SmartChef AI Works

1. User opens the SmartChef AI website.

2. User enters a recipe name in the chatbot search box.

3. Frontend sends the request to the Flask backend.

4. Backend loads the synthetic recipe dataset from `recipes.json`.

5. The chatbot searches for similar recipe names and keywords.

6. Fuzzy matching is used to identify the closest recipe match.

7. The best matching recipe is selected.

8. Backend sends recipe data back to frontend.

9. Frontend displays:
   - Recipe title
   - Description
   - Ingredients
   - Preparation time
   - Cooking instructions

10. Users can continue asking for different recipes in real time.

---

# 🔍 How Recipe Searching Works

The backend uses:
- keyword matching
- title matching
- fuzzy similarity search using `difflib`

This helps the chatbot understand:
- spelling mistakes
- similar recipe names
- related cooking keywords

Example:

```text id="ms3j8v"
User Input: biriyani
Matched Recipe: Chicken Biryani
```bash
backend/recipes.json

