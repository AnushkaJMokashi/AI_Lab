import streamlit as st
import pandas as pd

# Sample data for demonstration
sample_books_data = {
    "Title": ["Book 1", "Book 2", "Book 3"],
    "Author": ["Author 1", "Author 2", "Author 3"],
    "Genre": ["Fiction", "Non-fiction", "Science Fiction"],
    "Available Copies": [5, 3, 7]
}
df = pd.DataFrame(sample_books_data)

df.to_csv("books.csv",index=False)
books_df = pd.read_csv("books.csv")
def main():
    st.title("Library Management System")

    # Display available books
    st.subheader("Available Books")
    st.table(books_df)

    # Option to borrow a book
    selected_book = st.selectbox("Select a book to borrow:", books_df["Title"])
    borrow_button = st.button("Borrow")

    if borrow_button:
        borrow_book(selected_book)

def borrow_book(book_title):
    book_index = books_df.index[books_df["Title"] == book_title].tolist()[0]
    if books_df.loc[book_index, "Available Copies"] > 0:
        books_df.loc[book_index, "Available Copies"] -= 1
        # Save changes to DataFrame
        books_df.to_csv("books.csv", index=False)
        st.success(f"You have successfully borrowed '{book_title}'. Enjoy your reading!")
    else:
        st.warning("Sorry, this book is currently unavailable.")

if __name__ == "__main__":
    main()
