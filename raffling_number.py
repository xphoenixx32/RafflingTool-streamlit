import streamlit as st
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

# Set up the number ranges
main_numbers = np.arange(1, 39)      # 1 to 38
special_numbers = np.arange(1, 9)      # 1 to 8

# Weight parameters for the weighted lottery
main_probs = np.array([
    16.14, 14.62, 17.38, 17.04, 14.17, 16.09, 16.25, 16.14, 13.05, 16.54,
    15.64, 15.47, 15.58, 16.65, 16.85, 16.31, 15.75, 15.13, 16.48, 15.41,
    15.02, 16.59, 15.80, 17.77, 16.09, 16.48, 15.80, 16.20, 15.47, 15.47,
    14.29, 15.02, 14.29, 15.47, 15.64, 15.97, 16.93, 15.50
])
special_probs = np.array([12.09, 13.78, 12.43, 12.77, 13.33, 11.47, 12.09, 12.04])

# Normalize probabilities
main_probs = main_probs / main_probs.sum()
special_probs = special_probs / special_probs.sum()

# Page configuration
st.set_page_config(page_title="Lottery Raffling Tool", layout="centered")

# Title and description
st.markdown("<h2 style='text-align: center; color: #333;'>Welcome, future billionaires!</h2>", unsafe_allow_html=True)
st.title("💰 Lottery Tool")
st.markdown("#### Choose a Sampling Method 🔽")

# Use a selection box instead of a radio button
lottery_type = st.selectbox("Select Sampling Method", 
                            ("Random Sampling", "Weighted Sampling (prob. 2005~now)"))

# Button to perform the draw
if st.button("Draw Numbers"):
    if lottery_type == "Random Sampling":
        selected_main, selected_special = fair_lottery(main_numbers, special_numbers)
        method = "Random Sampling"
    else:
        selected_main, selected_special = weighted_lottery(main_numbers, main_probs, special_numbers, special_probs)
        method = "Weighted Sampling (prob. 2005~now)"
    
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
    st.markdown("##### First Section (6 Numbers):", unsafe_allow_html=True)
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
    st.markdown("##### Second Section (1 Number):", unsafe_allow_html=True)
    st.markdown(second_section_html, unsafe_allow_html=True)
