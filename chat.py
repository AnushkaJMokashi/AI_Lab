import streamlit as st
import random
from difflib import SequenceMatcher

# Define patterns and responses for the cake ordering chatbot
patterns_responses = {
    "hi": ["Hello! Welcome to our bakery. How can I assist you with your cake order today?"],
    "what cakes do you offer": ["We offer a variety of cakes including chocolate, vanilla, strawberry, red velvet, and custom flavors. What flavor are you interested in?"],
    "what sizes are available": ["Our cakes are available in sizes ranging from 6 inches to 12 inches in diameter. What size would you like?"],
    "do you offer delivery": ["Yes, we offer delivery within the city limits. Please provide your address so we can calculate the delivery fee."],
    "how much does a cake cost": ["The cost of our cakes depends on the size and flavor. What size and flavor are you interested in?"],
    "how can I place an order": ["You can place an order by calling our hotline at XXX-XXXX-XXXX, by visiting our website and using our online order form, or by visiting our bakery in person."],
    "do you offer gluten-free options": ["Yes, we offer gluten-free options for some of our cakes. Please let us know your dietary restrictions and we can provide more information."],
    "can I customize my cake": ["Yes, we offer custom cake designs. Please provide details about your desired design and we'll be happy to assist you further."],
    "what are your payment options": ["We accept cash, credit/debit cards, and mobile payment apps. Payment is required upon placing your order."],
    "how long in advance should I order": ["We recommend placing your order at least 24-48 hours in advance, especially for custom cakes. However, we may be able to accommodate rush orders depending on our current schedule."],
    "bye": ["Thank you for considering our bakery for your cake purchase! Have a wonderful day!"]
}

# Fallback response for unmatched input
fallback_responses = [
    "I'm sorry, I didn't understand that. How can I assist you with your cake order?",
    "I'm not sure I understand. Can you please rephrase that?"
]

# Sample images for demonstration
veg_images = {
    "Salad": "https://www.example.com/salad_image.jpg",
    "Soup": "https://www.example.com/soup_image.jpg",
    "Vegetable Curry": "https://www.example.com/veg_curry_image.jpg",
}

nonveg_images = {
    "Chicken Wings": "https://www.example.com/chicken_wings_image.jpg",
    "Steak": "https://www.example.com/steak_image.jpg",
    "Fish Tacos": "https://www.example.com/fish_tacos_image.jpg",
}

all_images = {
    "Burger": "https://www.example.com/burger_image.jpg",
    "Pizza": "https://www.example.com/pizza_image.jpg",
    "Sushi": "https://www.example.com/sushi_image.jpg",
}

# Function to calculate similarity between two strings using SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Function to generate response for the chatbot
def respond(input_text):
    input_text = input_text.lower()
    max_similarity = 0
    best_match_response = None
    
    # Threshold for similarity to consider a match
    threshold = 0.5
    
    for pattern, responses in patterns_responses.items():
        similarity = similar(input_text, pattern)
        if similarity > max_similarity and similarity >= threshold:
            max_similarity = similarity
            best_match_response = random.choice(responses)
            
    if best_match_response is None:
        best_match_response = random.choice(fallback_responses)
        
    return best_match_response

# Streamlit app
def main():
    st.title("Food Ordering and Cake Ordering Chatbot")

    st.markdown("""
    ### Food Ordering and Cake Ordering Chatbot
    
    Welcome to our shop's chatbot! You can order food or inquire about cake options.
    """)

    st.subheader("To chat with bot click Below!!")

    # Sample images for demonstration

    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    def streamdata(i):
        st.session_state.stage = i

    def veg_menu():
        for item, img_url in veg_images.items():
            st.image(img_url, caption=item)

    def nonveg_menu():
        for item, img_url in nonveg_images.items():
            st.image(img_url, caption=item)

    def all_menu():
        for item, img_url in all_images.items():
            st.image(img_url, caption=item)

    if st.session_state.stage == 0:
        st.button('Mega-Bot', on_click=streamdata, args=[1])

    if st.session_state.stage >= 1:
        name = st.text_input('Name', key='name_input', value=st.session_state.get('name', ''), on_change=streamdata, args=[2])
        st.session_state.name = name

    pref = None
    if st.session_state.stage >= 2:
        st.write(f'Hello {st.session_state.name}!')
        pref = st.selectbox(
            'Pick your Preference',
            [None, 'Veg','Non Veg','All'],
            on_change=streamdata, args=[3]
        )
        if pref is None:
            streamdata(2)

    if st.session_state.stage >= 3:
        st.write(f'Your preference is : {pref}')
        st.button('Start Over', on_click=streamdata, args=[0])
        st.button('Next', on_click=streamdata,args=[4])

    if st.session_state.stage >= 4:
        if pref.lower() == "veg":
            st.write(f"Would you prefer enjoying crunchy snacks or want to enjoy a {pref} Meal ?")
            veg_menu()
        elif pref.lower() == "nonveg" or pref.lower() == "non veg":
            st.write(f"Would you prefer enjoying crunchy snacks or want to enjoy a {pref} Meal ?")
            nonveg_menu()
        elif pref.lower() == "all":
            st.write(f"Would you prefer enjoying crunchy snacks or want to enjoy a Meal ?")
            all_menu()
            st.text("Let me know if you have a personal preference:")

            if prompt := st.text_input("You:"):

                if st.button("Send"):
                    if prompt == "Burger":
                        st.write("Burgers")
                    if prompt == "I want to ask you something different ":
                        st.text_area("Chatbot:", value="Sure, go ahead!", height=100, max_chars=None, key=None)
                    if prompt == "show options":
                        st.session_state.stage = 3
                    else:
                        response = respond(prompt)
                        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=None)

# Run the Streamlit app
if __name__ == "__main__":
    main()
