import streamlit as st
import pandas as pd
import numpy as np

def weighted_lottery(main_numbers, main_probs, special_numbers, special_probs):
    """
    Draw 6 numbers from main_numbers based on main_probs,
    and 1 number from special_numbers based on special_probs.
    """
    selected_main = np.random.choice(main_numbers, size=6, replace=False, p=main_probs)
    selected_special = np.random.choice(special_numbers, size=1, replace=False, p=special_probs)
    return list(selected_main), int(selected_special[0])

def fair_lottery(main_numbers, special_numbers):
    """
    Draw 6 numbers from main_numbers fairly,
    and 1 number from special_numbers fairly.
    """
    selected_main = np.random.choice(main_numbers, size=6, replace=False)
    selected_special = np.random.choice(special_numbers, size=1, replace=False)
    return list(selected_main), int(selected_special[0])

first_zone = pd.read_csv("assets/first_zone.csv")
second_zone = pd.read_csv("assets/second_zone.csv")

main_numbers = first_zone['Number'].values
main_probs = first_zone['Probability'].values.astype(float)
main_probs = main_probs / main_probs.sum() # Normalize probabilities

special_numbers = second_zone['Number'].values
special_probs = second_zone['Probability'].values.astype(float)
special_probs = special_probs / special_probs.sum() # Normalize probabilities

# Page configuration
st.set_page_config(page_title="Lottery Raffling Tool", layout="centered")

# Title and description
st.markdown("<h4 style='text-align: center; color: #333;'>🙌 Welcome, future billionaires!</h2>", unsafe_allow_html=True)
st.markdown("###### 💰 *Lottery Tool*")
st.markdown("##### Choose a Sampling Method 🔽")

# Use a selection box instead of a radio button
lottery_type = st.selectbox("Select Sampling Method", 
                            ("Random Sampling", "Weighted Sampling (prob. 2008~now)"))

# Button to perform the draw
if st.button("Draw Numbers"):
    if lottery_type == "Random Sampling":
        selected_main, selected_special = fair_lottery(main_numbers, special_numbers)
        method = "Random Sampling"
    else:
        selected_main, selected_special = weighted_lottery(main_numbers, main_probs, special_numbers, special_probs)
        method = "Weighted Sampling (prob. 2008~now)"

    st.balloons()
    # HTML for first section (6 numbers) with white background
    first_section_html = f"""
    <div style="
         background-color: white;
         color: black;
         padding: 10px;
         border-radius: 5px;
         font-size: 24px;
         font-weight: bold;
         text-align: center;
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
         {', '.join(map(str, sorted(selected_main)))}
    </div>
    """
    st.markdown("###### *First Section (6 Numbers)*", unsafe_allow_html=True)
    st.markdown(first_section_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # HTML for second section (1 number) with red background
    second_section_html = f"""
    <div style="
         background-color: #FFCCCC;
         color: red;
         padding: 10px;
         border-radius: 5px;
         font-size: 24px;
         font-weight: bold;
         text-align: center;
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
         {selected_special}
    </div>
    """
    st.markdown("###### *Second Section (1 Number)*", unsafe_allow_html=True)
    st.markdown(second_section_html, unsafe_allow_html=True)
