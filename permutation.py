import streamlit as st
import itertools
import random

# Set the title of the app
st.title("Permutations of Four Numbers", anchor=None)

# Create a text input for the user to enter numbers
user_input = st.text_input("Enter four numbers (space-separated):")

if user_input:
    try:
        # Split the input into a list and convert to integers
        numbers = [int(num.strip()) for num in user_input.split()]
        
        if len(numbers) != 4:
            st.error("Please enter exactly four numbers.")
        else:
            # Calculate all permutations
            permutations = list(itertools.permutations(numbers))
            
            # Remove the input permutation from the list
            input_permutation = tuple(numbers)
            permutations.remove(input_permutation)
            
            # Shuffle the remaining permutations for mixed order
            random.shuffle(permutations)
            
            # Display the results in four columns
            st.write("### All possible permutations (in random order):")
            cols = st.columns(4)  # Create four columns

            # Loop through the permutations and display in columns
            for i, perm in enumerate(permutations):
                # Join the numbers into a string without parentheses
                formatted_perm = ' '.join(map(str, perm))
                # Use a larger font size and bold text for readability
                cols[i % 4].markdown(f"<span style='font-size: 20px; font-weight: bold;'>{formatted_perm}</span>", unsafe_allow_html=True)

    except ValueError:
        st.error("Please enter valid integers.")
