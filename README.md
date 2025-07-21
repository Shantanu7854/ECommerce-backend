# E-Commerce Backend
Deployed Link: [https://ecommerce-backend-1-300f.onrender.com](https://ecommerce-backend-1-300f.onrender.com) 

This is a basic FastAPI backend project for an e-commerce app that supports:

1. Adding and retrieving products
2. Placing orders
3. Connecting to MongoDB Atlas

## Project Structure

```
.
├── app/
│   ├── main.py         # Entry point for the FastAPI app
│   ├── models.py       # Pydantic models defining structure for Products and Orders
│   ├── database.py     # Handles MongoDB connection setup using PyMongo
│   ├── routes.py       # API route definitions for CRUD operations on products and orders
│   └── schemas.py      # MongoDB schema definitions using dictionary-based structures
├── requirements.txt     # Python dependencies required to run the project
├── render.yaml          # Configuration for deploying to Render.com
├── .env.example         # Example environment variable file
└── README.md            # Documentation for project overview and instructions
```

### Code Breakdown

* `main.py`: Initializes the FastAPI app and includes the API routes
* `models.py`: Defines `Product` and `Order` using Pydantic for request validation
* `database.py`: Connects to MongoDB using credentials stored in environment variables
* `routes.py`: Contains all the API endpoints for interacting with products and orders
* `schemas.py`: Defines how documents are structured in the MongoDB collections

Each file in the `app/` folder plays a modular role in separating concerns like data modeling, route handling, and database communication.

---

## API Endpoints 

### Create Product

* **Endpoint:** `/products`
* **Method:** `POST`
* **Description:** Add a new product by passing product details in the request body.

### List Products

* **Endpoint:** `/products`
* **Method:** `GET`
* **Query Parameters:**
  * `limit`: Number of products to return
  * `offset`: Number of products to skip (used for pagination, sorted by `_id`)

### Create Order

* **Endpoint:** `/orders`
* **Method:** `POST`
* **Description:** Create a new order by providing `user_id` and a list of product IDs.

### List Orders for a User

* **Endpoint:** `/orders/{user_id}`
* **Method:** `GET`

---

## How to Run Locally

1. **Clone the repository:**

   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv venv
   On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add environment variables:**

   * Create a `.env` file using the provided `.env.example`

5. **Start the server:**

   ```bash
   uvicorn app.main:app --reload
   ```

---

## Dependencies

* `fastapi`
* `uvicorn`
* `pymongo`
* `python-dotenv`

---

## Sample .env file 

```env
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/ecommerce
MONGO_DB_NAME=ecommerce
```

---


