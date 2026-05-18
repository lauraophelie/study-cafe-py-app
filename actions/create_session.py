from cryptography.fernet import Fernet

def start_study_session(username, duration=60):
    pass

def open_study_session():
    group_key = Fernet.generate_key()
    group_cipher = Fernet(group_key)

    return group_key, group_cipher