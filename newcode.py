import streamlit as st
import itertools
import random

# Set the title of the app
st.title("Permutations of Four Numbers")

# Create a text input for the user to enter numbers
user_input = st.text_input("Enter four numbers (comma-separated):")

if user_input:
    try:
        # Split the input into a list and convert to integers
        numbers = [int(num.strip()) for num in user_input.split(",")]
        
        if len(numbers) != 4:
            st.error("Please enter exactly four numbers.")
        else:
            # Calculate all permutations
            permutations = list(itertools.permutations(numbers))
            
            # Shuffle the permutations for mixed order
            random.shuffle(permutations)
            
            # Display the results
            st.write("All possible permutations (in random order):")
            for perm in permutations:
                st.write(perm)
    except ValueError:
        st.error("Please enter valid integers.")
