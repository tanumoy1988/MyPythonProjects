# 📚 Bookstore API

A simple yet powerful FastAPI-based bookstore application for managing books with full CRUD (Create, Read, Update, Delete) functionality.

## Features

- ✅ **Add Books** - Create new book entries with author, title, type, and rating
- ✅ **List Books** - View all books in the bookstore
- ✅ **Get Book** - Retrieve details of a specific book by ID
- ✅ **Update Books** - Modify book information (author, name, type, rating)
- ✅ **Delete Books** - Remove books from the bookstore
- 🔍 **Search by Author** - Find books by author name
- 🏷️ **Search by Type** - Filter books by type (Fiction/Non Fiction)
- ⭐ **Filter by Rating** - Get books with minimum rating threshold
- 📖 **Interactive API Docs** - Auto-generated Swagger UI documentation
- 🚀 **CI/CD Pipeline** - Automated testing, linting, and deployment
- 🐳 **Docker Support** - Containerized deployment

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Docker (optional, for containerized deployment)
- Make (optional, for using Makefile commands)

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd python-for-ai
```

### 2. Create virtual environment

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install fastapi uvicorn pydantic
```

## Quick Start

### 1. Start the Server

```bash
python bookstore_api.py
# Or using Makefile:
make server
```

The server will start at `http://127.0.0.1:8000`

### 2. Access Interactive Documentation

Open your browser and go to:
- **Swagger UI** (recommended): http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### 3. Run Tests

```bash
python test_bookstore.py
# Or using Makefile:
make test
```

## API Endpoints

### Create a Book
```bash
POST /books/
Content-Type: application/json

{
  "name": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "book_type": "Fiction",
  "rating": 4.8
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "name": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "book_type": "Fiction",
  "rating": 4.8
}
```

### List All Books
```bash
GET /books/
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "book_type": "Fiction",
    "rating": 4.8
  },
  ...
]
```

### Get a Specific Book
```bash
GET /books/{book_id}
```

Example: `GET /books/1`

### Update a Book
```bash
PUT /books/{book_id}
Content-Type: application/json

{
  "rating": 5.0,
  "author": "Harper Lee (Updated)"
}
```

**Note:** All fields are optional. Only provide fields you want to update.

### Delete a Book
```bash
DELETE /books/{book_id}
```

Example: `DELETE /books/1`

### Search by Author
```bash
GET /books/search/by-author/{author}
```

Example: `GET /books/search/by-author/George`

### Search by Type
```bash
GET /books/search/by-type/{book_type}
```

Example: `GET /books/search/by-type/Fiction`

Available types:
- `Fiction`
- `Non Fiction`

### Filter by Rating
```bash
GET /books/filter/by-rating/{min_rating}
```

Example: `GET /books/filter/by-rating/4.5`

Returns books with rating >= specified minimum rating, sorted by rating (highest first).

## Development

### Code Quality

```bash
# Run all linting tools
make lint

# Format code
make format

# Run security checks
make security

# Clean cache files
make clean
```

### Docker

```bash
# Build Docker image
make docker-build

# Run Docker container
make docker-run
```

## CI/CD Pipeline

This project includes a comprehensive GitHub Actions CI/CD pipeline that runs on every push and pull request.

### Pipeline Features

- **Multi-Python Testing**: Tests against Python 3.8, 3.9, 3.10, 3.11, and 3.12
- **Code Quality**: Flake8 linting, Black formatting, isort import sorting, mypy type checking
- **Security**: Bandit security linting, Safety dependency vulnerability checks
- **Docker**: Automated Docker image building and testing
- **Deployment**: Ready for production deployment (configure deployment steps as needed)

### Pipeline Jobs

1. **Test**: Runs tests across multiple Python versions
2. **Lint**: Code quality checks (flake8, black, isort, mypy)
3. **Security**: Security vulnerability scanning
4. **Docker**: Build and test Docker image
5. **Deploy**: Production deployment (only on main branch pushes)
6. **Notify**: Pipeline status notifications

### Triggering the Pipeline

The pipeline automatically runs on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches
- Manual trigger via GitHub Actions UI

### Local Pipeline Simulation

You can run the same checks locally:

```bash
# Install all development dependencies
pip install -r requirements.txt

# Run tests
make test

# Run linting
make lint

# Run security checks
make security

# Build Docker image
make docker-build
```

## Testing

### Using Python Test Script

```bash
python test_bookstore.py
```

This will test all endpoints with sample data.

### Using cURL

```bash
# Add a book
curl -X POST http://127.0.0.1:8000/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "1984",
    "author": "George Orwell",
    "book_type": "Fiction",
    "rating": 4.7
  }'

# List all books
curl http://127.0.0.1:8000/books/

# Get a specific book
curl http://127.0.0.1:8000/books/1

# Update a book
curl -X PUT http://127.0.0.1:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"rating": 5.0}'

# Delete a book
curl -X DELETE http://127.0.0.1:8000/books/1

# Search by author
curl http://127.0.0.1:8000/books/search/by-author/George

# Search by type
curl "http://127.0.0.1:8000/books/search/by-type/Fiction"

# Filter by rating
curl http://127.0.0.1:8000/books/filter/by-rating/4.5
```

### Using Python Requests

```bash
pip install requests
python test_bookstore.py
```

## Book Model

### Fields

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `id` | integer | Yes (auto) | - | Unique book identifier |
| `name` | string | Yes | Min length: 1 | Book title |
| `author` | string | Yes | Min length: 1 | Author name |
| `book_type` | enum | Yes | "Fiction" or "Non Fiction" | Type of book |
| `rating` | float | Yes | 1.0 - 5.0 | Book rating |

### Example Book Object

```json
{
  "id": 1,
  "name": "Sapiens",
  "author": "Yuval Noah Harari",
  "book_type": "Non Fiction",
  "rating": 4.5
}
```

## Error Handling

### 404 Not Found
```json
{
  "detail": "Book with ID 999 not found"
}
```

### 422 Unprocessable Entity
Returned when validation fails (e.g., rating > 5, empty name, etc.)

```json
{
  "detail": [
    {
      "loc": ["body", "rating"],
      "msg": "ensure this value is less than or equal to 5",
      "type": "value_error.number.not_le"
    }
  ]
}
```

## Project Structure

```
python-for-ai/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline
├── bookstore_api.py           # Main FastAPI application
├── test_bookstore.py          # Test script with examples
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker container configuration
├── .dockerignore             # Docker ignore file
├── setup.cfg                 # Configuration for tools (flake8, mypy, etc.)
├── Makefile                  # Development commands
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## Data Storage

Currently, the API uses **in-memory storage** (dictionary). This means:
- Data is lost when the server restarts
- Perfect for testing and development
- No database setup required

### To Add Database Support

You can easily extend this with:
- SQLite (simple)
- PostgreSQL (production-ready)
- MongoDB (NoSQL)

## Future Enhancements

- [ ] Add database support (SQLite/PostgreSQL)
- [ ] User authentication and authorization
- [ ] Book inventory management
- [ ] Price tracking
- [ ] Reviews and comments
- [ ] Advanced filtering and sorting
- [ ] Pagination support
- [ ] API rate limiting
- [ ] Caching layer
- [ ] Monitoring and logging

## API Response Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 204 | No Content - Resource deleted successfully |
| 400 | Bad Request - Invalid input |
| 404 | Not Found - Resource not found |
| 422 | Unprocessable Entity - Validation error |
| 500 | Internal Server Error |

## Troubleshooting

### Port Already in Use
```bash
# Change the port in bookstore_api.py
# Change: uvicorn.run(app, host="0.0.0.0", port=8000)
# To: uvicorn.run(app, host="0.0.0.0", port=8001)
```

### Module Not Found
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt
```

### Connection Refused
- Make sure the server is running
- Check the host and port configuration

### Pipeline Issues
- Check GitHub Actions logs for detailed error messages
- Ensure all required secrets are configured for deployment
- Verify Docker build works locally first

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

The CI/CD pipeline will automatically run tests and quality checks on your PR.

## Deployment

### Docker Deployment

```bash
# Build and run with Docker
docker build -t bookstore-api .
docker run -p 8000:8000 bookstore-api
```

### Cloud Deployment

The pipeline includes deployment steps that can be configured for:
- **Heroku**: Container deployment
- **AWS ECR**: Amazon Elastic Container Registry
- **Google Cloud Run**: Serverless container deployment
- **Azure Container Instances**: Azure container deployment

Configure the deployment commands in `.github/workflows/ci-cd.yml` under the `deploy` job.

## License

Open source - feel free to use and modify.

---

**Happy Reading! 📚**

