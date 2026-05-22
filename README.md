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

# GYMini Core OS API

Цей проєкт — це бекенд-частина для системи управління фітнес-клубом, створена за допомогою FastAPI[cite: 1]. Програма автоматизує підбір тренувань та допомагає аналізувати активність клієнтів[cite: 1].

## Опис проєкту та функціонал

У програмі реалізовано два основних модулі:

1. **Експертна система генерації тренувань (`/api/v1/generate_workout`)**[cite: 1]
   * Ця частина приймає дані профілю клієнта (ідентифікатор, ціль, рівень підготовки, кількість занять) і повертає готову програму тренувань[cite: 1].
   * Основний акцент зроблено на цілі "posture_correction" (корекція постави)[cite: 1]. Програма базується на теоретичних засадах формування правильної постави: для цієї цілі генеруються вправи на зміцнення м'язового корсета спини (наприклад, гіперекстензія, планка, "човник") без вертикального осьового навантаження[cite: 1].
   * Також прописана базова логіка для генерації тренувань з метою набору м'язової маси ("muscle_gain")[cite: 1].

2. **CRM система аналітики відтоку клієнтів (`/api/v1/churn_prediction`)**[cite: 1]
   * Цей ендпоінт призначений для адміністративної панелі та використовує бібліотеку Pandas для швидкого аналізу бази даних[cite: 1].
   * Система аналізує змодельовані логи відвідувань клієнтів (до тестової бази включені клієнти Олександр М., Ірина К., Вадим С. та Максим М.)[cite: 1].
   * Програма автоматично розраховує, скільки днів кожен клієнт не був у залі, і присвоює йому статус ризику[cite: 1].
   * Залежно від статусу (наприклад, "High Churn Risk" при відсутності понад 14 днів або "Medium Risk" від 7 днів), система пропонує адміністратору конкретну дію: зателефонувати клієнту з бонусом або надіслати push-сповіщення[cite: 1].

## Як запустити код

1. Переконайтеся, що у вас встановлені всі необхідні бібліотеки. Введіть у терміналі:
```bash
   pip install fastapi pydantic pandas uvicorn
