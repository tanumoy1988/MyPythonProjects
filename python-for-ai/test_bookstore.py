"""
Example script to test the bookstore API
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

def test_bookstore_api():
    """Test all bookstore API endpoints"""
    
    print("=" * 60)
    print("BOOKSTORE API TEST")
    print("=" * 60)
    
    # Test 1: Add books
    print("\n1. ADDING BOOKS...")
    books_to_add = [
        {
            "name": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "book_type": "Fiction",
            "rating": 4.8
        },
        {
            "name": "1984",
            "author": "George Orwell",
            "book_type": "Fiction",
            "rating": 4.7
        },
        {
            "name": "Sapiens",
            "author": "Yuval Noah Harari",
            "book_type": "Non Fiction",
            "rating": 4.5
        },
        {
            "name": "Atomic Habits",
            "author": "James Clear",
            "book_type": "Non Fiction",
            "rating": 4.6
        },
        {
            "name": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "book_type": "Fiction",
            "rating": 4.2
        }
    ]
    
    created_books = []
    for book_data in books_to_add:
        response = requests.post(f"{BASE_URL}/books/", json=book_data)
        if response.status_code == 201:
            book = response.json()
            created_books.append(book)
            print(f"✓ Added: {book['name']} by {book['author']} (ID: {book['id']})")
        else:
            print(f"✗ Failed to add book: {book_data['name']}")
    
    # Test 2: List all books
    print("\n2. LISTING ALL BOOKS...")
    response = requests.get(f"{BASE_URL}/books/")
    if response.status_code == 200:
        books = response.json()
        print(f"✓ Total books: {len(books)}")
        for book in books:
            print(f"  - [{book['id']}] {book['name']} by {book['author']} ({book['book_type']}) - Rating: {book['rating']}/5")
    
    # Test 3: Get a specific book
    if created_books:
        book_id = created_books[0]['id']
        print(f"\n3. GETTING BOOK WITH ID {book_id}...")
        response = requests.get(f"{BASE_URL}/books/{book_id}")
        if response.status_code == 200:
            book = response.json()
            print(f"✓ Retrieved: {book['name']} by {book['author']}")
    
    # Test 4: Update a book
    if len(created_books) > 0:
        book_id = created_books[0]['id']
        print(f"\n4. UPDATING BOOK WITH ID {book_id}...")
        update_data = {
            "rating": 5.0,
            "author": "Harper Lee (Updated)"
        }
        response = requests.put(f"{BASE_URL}/books/{book_id}", json=update_data)
        if response.status_code == 200:
            updated_book = response.json()
            print(f"✓ Updated: {updated_book['name']}")
            print(f"  New rating: {updated_book['rating']}/5")
            print(f"  New author: {updated_book['author']}")
    
    # Test 5: Search by author
    print("\n5. SEARCHING BY AUTHOR 'George Orwell'...")
    response = requests.get(f"{BASE_URL}/books/search/by-author/George")
    if response.status_code == 200:
        books = response.json()
        print(f"✓ Found {len(books)} book(s):")
        for book in books:
            print(f"  - {book['name']} by {book['author']}")
    
    # Test 6: Search by type
    print("\n6. SEARCHING BY BOOK TYPE 'Non Fiction'...")
    response = requests.get(f"{BASE_URL}/books/search/by-type/Non%20Fiction")
    if response.status_code == 200:
        books = response.json()
        print(f"✓ Found {len(books)} Non Fiction book(s):")
        for book in books:
            print(f"  - {book['name']} by {book['author']}")
    
    # Test 7: Filter by rating
    print("\n7. FILTERING BOOKS WITH RATING >= 4.5...")
    response = requests.get(f"{BASE_URL}/books/filter/by-rating/4.5")
    if response.status_code == 200:
        books = response.json()
        print(f"✓ Found {len(books)} book(s) with rating >= 4.5:")
        for book in books:
            print(f"  - {book['name']} - Rating: {book['rating']}/5")
    
    # Test 8: Delete a book
    if len(created_books) > 1:
        book_id = created_books[1]['id']
        book_name = created_books[1]['name']
        print(f"\n8. DELETING BOOK WITH ID {book_id}...")
        response = requests.delete(f"{BASE_URL}/books/{book_id}")
        if response.status_code == 204:
            print(f"✓ Deleted: {book_name}")
    
    # Test 9: List books after deletion
    print("\n9. LISTING ALL BOOKS AFTER DELETION...")
    response = requests.get(f"{BASE_URL}/books/")
    if response.status_code == 200:
        books = response.json()
        print(f"✓ Remaining books: {len(books)}")
        for book in books:
            print(f"  - [{book['id']}] {book['name']} by {book['author']}")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    test_bookstore_api()
