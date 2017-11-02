import gspread
from oauth2client.service_account import ServiceAccountCredentials

class DataGetter():
    def __init__(self, credsFile='client_secret.json'):
        self.scope  = ['https://spreadsheets.google.com/feeds']
        self.creds  = ServiceAccountCredentials.from_json_keyfile_name(credsFile, self.scope)
        self.client = gspread.authorize(self.creds)

    def basicMovementData(self):
        return self.client.open("MovementTrainingData").sheet1.get_all_records()
