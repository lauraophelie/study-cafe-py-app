import datetime
from cryptography.fernet import Fernet
import json

class StudyInviteLink:
    def __init__(self, socket, student_name, session_id):
        self.socket = socket
        self.student_name = student_name
        self.session_id = session_id

    def generate_invite_link(self, group_key):
        link_data = self.process_invite_link_data()
        study_link_data = self.process_invite_link(link_data)
        study_link = group_key.encrypt(study_link_data)

        return study_link
    
    def process_invite_link(self, link_data):
        link_data_json = json.dumps(link_data)
        link_data_encode = link_data_json.encode('utf-8')

        return link_data_encode
    
    def process_invite_link_data(self):
        hostname = self.socket.gethostname()
        addr_ip = self.socket.gethostbyname(hostname)
        current_datetime = datetime.datetime.now()

        link_data = {
            "user_id": self.student_name,
            "session_id": self.session_id,
            "server_host": hostname,
            "server_ip": addr_ip,
            "date_time_creation": current_datetime
        }
        return link_data


    def save_study_session(self):
        pass