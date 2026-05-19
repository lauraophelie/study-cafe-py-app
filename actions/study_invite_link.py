import datetime
from cryptography.fernet import Fernet
import json
import base64

class StudyInviteLink:
    def __init__(self, socket, port_number, student_name, session_id=''):
        self.socket = socket
        self.port_number = port_number
        self.student_name = student_name
        self.session_id = session_id

    def generate_invite_link(self, max_user=5):
        link_data = self.process_invite_link_data(max_user=)
        return self.process_invite_link(link_data)
    
    def process_invite_link(self, link_data):
        link_data_json = json.dumps(link_data)

        link_data_encode = base64.urlsafe_b64encode(
            link_data_json.encode('utf-8')
        )

        return link_data_encode
    
    def process_invite_link_data(self, max_user=5):
        hostname = self.socket.gethostname()
        addr_ip = self.socket.gethostbyname(hostname)
        current_datetime = datetime.datetime.now()

        link_data = {
            "user_id": self.student_name,
            "session_id": self.session_id,
            "server_port_number": self.port_number,
            "server_host": hostname,
            "server_ip": addr_ip,
            "date_time_creation": current_datetime,
            "max_user": max_user
        }
        return link_data


    def save_study_session(self):
        pass