
import uuid
import datetime

hotel_database = {}

def register_hotel(hotel_name, manager_email, plan):
    api_key = f"tn_{str(uuid.uuid4()).replace('-', '')[:20]}"
    hotel_database[api_key] = {
        "hotel_name": hotel_name,
        "manager_email": manager_email,
        "plan": plan,
        "registered_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "active": True
    }
    return api_key

def receive_hotel_data(api_key, staff_name, role, 
                        records_accessed, failed_logins, 
                        download_mb, hour):
    if api_key not in hotel_database:
        return {"error": "Invalid API key"}
    
    hotel = hotel_database[api_key]
    return {
        "hotel": hotel["hotel_name"],
        "staff": staff_name,
        "status": "Data received and analysed"
    }
