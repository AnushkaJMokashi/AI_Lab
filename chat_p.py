
import random
from difflib import SequenceMatcher
pattern_responses={
    "hi":["Hello"],
    "What cakes do you offer?":["Chocolate,Vanilla"],
    "What are cost ranges? ":["200-300 rs"]
}

fallback_response=[
    "Sorry, I don't understand your query",
    "I am not aware about this"
]

def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()

def respond(input_text):
    input_text = input_text.lower()
    max_similarity = 0
    best_match_response = None
    
    threshold = 0.2
    
    for pattern,responses in pattern_responses.items():
        similarity = similar(input_text,pattern)
        #print("Similarity", similarity)
        if similarity > max_similarity and similarity >= threshold:
            max_similarity = similarity
            best_match_response = random.choice(responses)
    
    if best_match_response is None:
        best_match_response = random.choice(fallback_response)
        
            
    return best_match_response

def chat():
   
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bye")
            break
        response = respond(user_input)
        print("Bot: ",response)
        

if __name__ == "__main__":
    chat()
