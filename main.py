import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyBFRKJTYlJhGg7zjudiXAQSwoHqMkxmFQE")

model = genai.GenerativeModel('gemini-1.5-flash',
                              generation_config=genai.GenerationConfig(
                                  temperature=0.1
                              ))

def generate_recipe(ingredients):
    response = model.generate_content(f'I have the following ingredients: {ingredients}. Please generate a recipe for me.')
    return response.text

st.title("AI Recipe Generator 🍳🥗🍛")
st.write("This is a simple AI recipe generator. You can generate a recipe for a given set of ingredients.")

ingredients = st.text_input("Enter your ingredients would you have in your fridge")

if st.button("Generate Recipe 🍽️"):
    if ingredients:
        with st.spinner("Generating recipe... 🍽️"):
            recipe = generate_recipe(ingredients)
            st.markdown(recipe)
    else:
        st.warning("Please enter some ingredients before generating a recipe.")