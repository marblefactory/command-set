import gspread
from oauth2client.service_account import ServiceAccountCredentials

class DataGetter():
    """
    An object that has cridentials to read Drive documents.
    """
    def __init__(self, credsFile='client_secret.json'):
        self.scope  = ['https://spreadsheets.google.com/feeds']
        self.creds  = ServiceAccountCredentials.from_json_keyfile_name(credsFile, self.scope)
        self.client = gspread.authorize(self.creds)

    def basicMovementData(self):
        """
        Gets the training data from the first basic movement form and processes
        it into a list of spoken commands and their corresponding labels.
        """
        rows      = self.client.open("MovementTrainingData").sheet1.get_all_records()

        responces = []
        labels    = []

        for row in rows:
            for i, response in enumerate(list(row.values())[1:]):
                labels.append(i)
                responces.append(response.lower())

        return (responces, labels)
