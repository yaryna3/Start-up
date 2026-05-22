# Start-up
# GYMini Core OS API

This project is the backend part of a fitness club management system, built with FastAPI[cite: 1]. It helps automate workout planning and analyzes client activity[cite: 1].

## Project Description and Features

The program has two main modules:

1. **Expert System for Workout Generation (`/api/v1/generate_workout`)**[cite: 1]
   * This part takes client profile data (ID, goal, fitness level, days per week) and returns a ready workout plan[cite: 1].
   * The main focus is the "posture_correction" goal[cite: 1]. The program uses the theory of correct posture formation: it generates exercises to strengthen the back muscles (like hyperextension, plank, "boat" pose) without vertical load on the spine[cite: 1].
   * It also has basic logic for the "muscle_gain" goal[cite: 1].

2. **CRM Churn Prediction System (`/api/v1/churn_prediction`)**[cite: 1]
   * This endpoint is for the admin panel[cite: 1]. It uses the Pandas library to quickly analyze the database[cite: 1].
   * The system checks simulated client visit logs (the test database includes clients Oleksandr M., Iryna K., Vadym S., and Maksym M.)[cite: 1].
   * The program automatically counts how many days each client has missed and gives them a risk status[cite: 1].
   * Based on the status (for example, "High Churn Risk" for 14+ days or "Medium Risk" for 7+ days), the system suggests a specific action for the admin: call the client with a bonus or send a push notification[cite: 1].

## How to Run the Code

1. Make sure you have all the needed libraries installed. Type this in your terminal:
```bash
   pip install fastapi pydantic pandas uvicorn

