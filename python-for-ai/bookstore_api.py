from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

# Initialize FastAPI app
app = FastAPI(
    title="Bookstore API",
    description="A simple bookstore API for managing books",
    version="1.0.0"
)

# Enum for book types
class BookType(str, Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non Fiction"

# Pydantic models
class BookBase(BaseModel):
    name: str = Field(..., min_length=1, description="Book name")
    author: str = Field(..., min_length=1, description="Author name")
    book_type: BookType = Field(..., description="Type of book: Fiction or Non Fiction")
    rating: float = Field(..., ge=1, le=5, description="Rating from 1 to 5")

class Book(BookBase):
    id: int = Field(..., description="Unique book identifier")

class BookUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, description="Book name")
    author: Optional[str] = Field(None, min_length=1, description="Author name")
    book_type: Optional[BookType] = Field(None, description="Type of book: Fiction or Non Fiction")
    rating: Optional[float] = Field(None, ge=1, le=5, description="Rating from 1 to 5")

# In-memory database
books_db: dict = {}
next_book_id: int = 1

# ==================== CREATE ====================
@app.post("/books/", response_model=Book, status_code=201)
def create_book(book: BookBase):
    """Add a new book to the bookstore"""
    global next_book_id
    
    new_book = Book(
        id=next_book_id,
        name=book.name,
        author=book.author,
        book_type=book.book_type,
        rating=book.rating
    )
    
    books_db[next_book_id] = new_book
    next_book_id += 1
    
    return new_book

# ==================== READ ====================
@app.get("/books/", response_model=List[Book])
def list_all_books():
    """List all books in the bookstore"""
    if not books_db:
        return []
    return list(books_db.values())

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Get a specific book by ID"""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    
    return books_db[book_id]

# ==================== UPDATE ====================
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    """Update book details"""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    
    existing_book = books_db[book_id]
    update_data = book_update.dict(exclude_unset=True)
    
    updated_book = existing_book.copy(update={**update_data})
    books_db[book_id] = updated_book
    
    return updated_book

# ==================== DELETE ====================
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """Delete a book from the bookstore"""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    
    del books_db[book_id]
    return None

# ==================== UTILITY ENDPOINTS ====================
@app.get("/books/search/by-author/{author}", response_model=List[Book])
def search_by_author(author: str):
    """Search books by author name"""
    results = [book for book in books_db.values() if author.lower() in book.author.lower()]
    return results

@app.get("/books/search/by-type/{book_type}", response_model=List[Book])
def search_by_type(book_type: BookType):
    """Search books by type (Fiction or Non Fiction)"""
    results = [book for book in books_db.values() if book.book_type == book_type]
    return results

@app.get("/books/filter/by-rating/{min_rating}", response_model=List[Book])
def filter_by_rating(min_rating: float = Path(..., ge=1, le=5)):
    """Get books with minimum rating"""
    results = [book for book in books_db.values() if book.rating >= min_rating]
    return sorted(results, key=lambda x: x.rating, reverse=True)

# ==================== ROOT ENDPOINT ====================
@app.get("/")
def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Bookstore API",
        "endpoints": {
            "create_book": "POST /books/",
            "list_all_books": "GET /books/",
            "get_book": "GET /books/{book_id}",
            "update_book": "PUT /books/{book_id}",
            "delete_book": "DELETE /books/{book_id}",
            "search_by_author": "GET /books/search/by-author/{author}",
            "search_by_type": "GET /books/search/by-type/{book_type}",
            "filter_by_rating": "GET /books/filter/by-rating/{min_rating}",
            "api_docs": "/docs"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
