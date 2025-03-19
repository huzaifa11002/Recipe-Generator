# AI Recipe Generator

## Overview
AI Recipe Generator is a simple Streamlit-based application that generates a recipe based on the given ingredients using AI. It utilizes the Google Gemini AI model to create accurate and creative recipes.

## Features
- Generates a recipe based on user-provided ingredients.
- Uses Google Gemini AI for content generation.
- Utilizes Streamlit for an interactive UI.
- Simple and user-friendly interface.

## Tech Stack
- **Python**
- **Streamlit** (For frontend UI)
- **Google Gemini AI** (For recipe generation)
- **Unified Virtualenv (UV)** (For project environment)

## Installation
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-recipe-generator
   ```

2. **Set up the environment (using UV)**
   ```bash
   uv venv env
   source env/bin/activate  # (For Windows: env\Scripts\activate)
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter the available ingredients in the input field.
2. Click the "Generate Recipe" button.
3. The AI will generate a recipe based on the given ingredients.
4. The recipe will be displayed in markdown format.

## Live Demo
To try the AI Recipe Generator without installation, visit:
[Live App](https://recipe-generator-huzaifa.streamlit.app/)

## Configuration
This project uses Google Gemini AI, so you need to configure an API key. It is recommended to store the `api_key` in a `.env` file.

## Contribution
If you would like to contribute or suggest improvements, feel free to raise a pull request or an issue.

## License
This project is open-source and distributed under the [MIT License](LICENSE).

---
Made with ❤️ using Streamlit & Google Gemini AI

---

# SecurePass - Password Generator & Strength Checker

## Overview
SecurePass is a simple and secure password generator and strength checker that helps users create strong passwords and evaluate their security.

## Features
- **Password Generator:** Customizable password generation (length, digits, symbols)
- **Strength Checker:** Analyze the security of passwords
- **Interactive UI:** Simple and intuitive design using Streamlit
- **Real-time Security Check:** Instantly analyze generated passwords

## Tech Stack
- **Python**
- **Streamlit** (For frontend UI)
- **Modules (Custom Python functions)**
- **Unified Virtualenv (UV)** (For project environment)

## Installation
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd securepass-password-generator
   ```

2. **Set up the environment (using UV)**
   ```bash
   uv venv env
   source env/bin/activate  # (For Windows: env\Scripts\activate)
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## Usage
1. **Password Generator:**
   - Select the "Password Generator" tab.
   - Choose password length, digits, and symbols.
   - Click the "Generate Password" button.
   - The generated password will be displayed on the screen.
   
2. **Password Strength Checker:**
   - Select the "Check Strength" tab.
   - Enter your password and click the "Check" button.
   - The system will analyze your password and provide a security score.

## Live Demo
To try SecurePass without installation, visit:
[Live App](https://password-generator-huzaifa.streamlit.app/)

## Contribution
If you would like to contribute or suggest improvements, feel free to raise a pull request or an issue.

## Lice
