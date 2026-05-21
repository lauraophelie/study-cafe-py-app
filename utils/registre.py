import json
import os
import uuid
import datetime

def create_new_session(username, duration):
    print("here")
    try:
        new_session = {
            "session_id": str(uuid.uuid4()),
            "username": username,
            "duration": duration,
            "date_time_creation": datetime.datetime.now().isoformat()
        }
        register_path = 'register/register.json'

        if not os.path.exists(register_path):
            with open(register_path, 'w') as f:
                json.dump([], f)

        with open(register_path, 'r') as f:
            data = json.load(f)
        data.append(new_session)

        with open(register_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        return True
    except Exception as e:
        print(str(e))
        return False