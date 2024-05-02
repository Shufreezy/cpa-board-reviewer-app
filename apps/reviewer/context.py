import uuid

context = {
  "title": "My Quiz",
  "questions": [
    {
    "id": str(uuid.uuid4()),
    "question": "What is the capital of France?",
    "correct": "Paris",
    "answers": ["Paris", "London", "Rome", "Berlin"]
  },
  {
    "id": str(uuid.uuid4()),
    "question": "What is the largest planet in our solar system?",
    "correct": "Jupiter",
    "answers": ["Jupiter", "Earth", "Saturn", "Uranus"]
  },
  {
    "id": str(uuid.uuid4()),
    "question": "What is the smallest planet in our solar system?",
    "correct": "Mercury",
    "answers": ["Mercury", "Mars", "Venus", "Neptune"]
  }
  ]
}