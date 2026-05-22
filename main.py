from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from datetime import datetime, timedelta

# Ініціалізація нашого B2B API
app = FastAPI(title="GYMini Core OS API", version="1.0")

# --- 1. СХЕМИ ДАНИХ ---
class ClientProfile(BaseModel):
    client_id: str
    goal: str  # Наприклад: "posture_correction", "weight_loss", "muscle_gain"
    level: str
    days_per_week: int

# --- 2. БАЗА ДАНИХ (Симуляція логів турнікета) ---
# У реальному проєкті тут буде підключення до SQL/NoSQL бази клубу
gym_logs = pd.DataFrame({
    "client_id": ["CLI-001", "CLI-042", "CLI-105", "CLI-201"],
    "name": ["Олександр М.", "Ірина К.", "Вадим С.", "Максим М."],
    # Симуляція останнього візиту
    "last_visit_date": [
        datetime.now() - timedelta(days=14), # Давно не був
        datetime.now() - timedelta(days=21), # Дуже давно не була
        datetime.now() - timedelta(days=5),  # Нормально
        datetime.now() - timedelta(days=2)   # Активний
    ]
})

# --- 3. МОДУЛЬ 1: Експертна система генерації тренувань ---
@app.post("/api/v1/generate_workout")
def generate_workout(profile: ClientProfile):
    """
    Цей ендпоінт приймає запит з фронтенду/додатка спортзалу
    і повертає готову програму.
    """
    # Ядро експертної системи
    if profile.goal == "posture_correction":
        # Програма базується на теоретичних засадах формування правильної постави
        # Головний акцент - теорія фізичної культури: зміцнення м'язового корсета без вертикального осьового навантаження
        workout_plan = {
            "theory_basis": "Теоретичні основи формування постави (зміцнення глибоких м'язів спини).",
            "exercises": [
                {"name": "Екстензія спини (гіперекстензія) на підлозі", "sets": 3, "reps": 15},
                {"name": "Тяга горизонтального блоку до пояса (зведення лопаток)", "sets": 3, "reps": 12},
                {"name": "Вправа 'Човник' у статиці", "sets": 3, "duration": "30 сек"},
                {"name": "Планка класична з суворим контролем попереку", "sets": 3, "duration": "45 сек"}
            ],
            "warning": "Уникати присідань зі штангою та станової тяги до зміцнення корсета."
        }
    elif profile.goal == "muscle_gain":
        workout_plan = {
            "theory_basis": "Гіпертрофія м'язових волокон через прогресуюче навантаження.",
            "exercises": [
                {"name": "Жим штанги/гантелей лежачи", "sets": 4, "reps": 10},
                {"name": "Жим ногами в тренажері", "sets": 4, "reps": 12}
            ]
        }
    else:
        workout_plan = {"error": "Невідома ціль. Будь ласка, зверніться до чергового тренера."}

    return {
        "status": "success",
        "client_id": profile.client_id,
        "generated_plan": workout_plan
    }

# --- 4. МОДУЛЬ 2: CRM Відтоку (Аналітика даних) ---
@app.get("/api/v1/churn_prediction")
def get_churn_risks():
    """
    Цей ендпоінт викликається адміністративною панеллю власника клубу.
    Він аналізує логі і повертає список клієнтів, яких треба рятувати.
    """
    today = datetime.now()
    
    # Використовуємо Pandas для швидкого розрахунку різниці в днях для всього масиву даних
    gym_logs['days_absent'] = (today - gym_logs['last_visit_date']).dt.days
    
    churn_report = []
    
    for index, row in gym_logs.iterrows():
        status = "Active"
        action = "None"
        
        # Логіка визначення ризику
        if row['days_absent'] >= 14:
            status = "High Churn Risk"
            action = "Call via CRM & Offer Bonus"
        elif row['days_absent'] >= 7:
            status = "Medium Risk"
            action = "Send Push Notification"
            
        churn_report.append({
            "client_id": row['client_id'],
            "name": row['name'],
            "days_absent": int(row['days_absent']),
            "status": status,
            "recommended_action": action
        })
        
    # Сортуємо масив, щоб найпроблемніші клієнти були зверху
    churn_report.sort(key=lambda x: x['days_absent'], reverse=True)
    
    return {
        "total_clients_analyzed": len(gym_logs),
        "risky_clients_found": len([c for c in churn_report if c['status'] != "Active"]),
        "report": churn_report
    }