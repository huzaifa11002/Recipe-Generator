# AI Recipe Generator

## Overview
AI Recipe Generator ek simple Streamlit-based application hai jo AI ka use karke diye gaye ingredients ke basis par ek recipe generate karta hai. Yeh Google Gemini AI model ka istemal karta hai taake accurate aur creative recipes generate ki ja sakein.

## Features
- User ke diye gaye ingredients ke basis par ek recipe generate karta hai.
- Google Gemini AI ka use karta hai content generation ke liye.
- Streamlit ka use karta hai interactive UI ke liye.
- Simple aur user-friendly interface.

## Tech Stack
- **Python**
- **Streamlit** (Frontend UI ke liye)
- **Google Gemini AI** (Recipe generation ke liye)
- **Unified Virtualenv (UV)** (Project environment ke liye)

## Installation
1. **Repository clone karein**
   ```bash
   git clone <repository-url>
   cd ai-recipe-generator
   ```

2. **Environment setup karein (UV ka use karein)**
   ```bash
   uv venv env
   source env/bin/activate  # (Windows ke liye: env\Scripts\activate)
   ```

3. **Dependencies install karein**
   ```bash
   pip install -r requirements.txt
   ```

4. **Streamlit app run karein**
   ```bash
   streamlit run app.py
   ```

## Usage
1. Ingredients input field mein apne fridge ke available ingredients likhein.
2. "Generate Recipe" button dabayein.
3. AI aapke diye gaye ingredients ke basis par ek recipe generate karega.
4. Recipe ko markdown format mein display kiya jayega.

## Live Demo
Agar aap is AI Recipe Generator ko bina install kiye dekhna chahte hain, toh yahan visit karein:
[Live App](https://recipe-generator-huzaifa.streamlit.app/)

## Configuration
Project Google Gemini AI ka use karta hai, isliye aapko ek API key configure karni hogi. `api_key` ko `.env` file mein store karna recommended hai.

## Contribution
Agar aap is project mein kuch naya add karna chahte hain ya koi improvement suggest karna chahte hain, toh pull request ya issue raise karein.

## License
Yeh project open-source hai aur [MIT License](LICENSE) ke under distribute kiya gaya hai.

---
Made with ❤️ using Streamlit & Google Gemini AI

