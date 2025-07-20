# Schema-Builder-Backend
# HROne Backend Intern Hiring Task

✅ FastAPI-based backend for an eCommerce app with MongoDB (Atlas).

## 🔧 Tech Stack
- Python 3.10+
- FastAPI
- MongoDB Atlas
- Pymongo

## 📦 API Endpoints

### Create Product
**POST /products**
```json
{
  "name": "Shirt",
  "description": "Cotton half-sleeve",
  "price": 499.99,
  "sizes": ["small", "medium", "large"]
}
