import gspread
from oauth2client.service_account import ServiceAccountCredentials
from typing import List


class DataGetter():
    """
    An object that has cridentials to read Drive documents.
    """
    def __init__(self, credsFile='client_secret.json'):
        self.scope  = ['https://spreadsheets.google.com/feeds']
        self.creds  = ServiceAccountCredentials.from_json_keyfile_name(credsFile, self.scope)
        self.client = gspread.authorize(self.creds)

    def location_data(self) -> List[List[str]]:
        """
        :return: a list of answers for each question about locations.
        """
        # All the answers a single user provided.
        rows = self.client.open("MovementTrainingData").sheet1.get_all_records()
        # The rows after removing the first column, which is a timestamp.
        all_user_answers = [list(row.values())[1:] for row in rows]
        # All the answers for a question.
        question_answers = [[] for _ in range(19)]

        for user_answers in all_user_answers:
            for question_index, answer in enumerate(user_answers):
                if answer != '':
                    question_answers[question_index].append(answer.lower())

        return question_answers


    def location_ideal_answers(self) -> List[str]:
        """
        :return: a list of ideal answers for each question about locations. These can be used to obtain the correct
                 vector to represent each question, and hence check the performance of the classifier on locations.
                 The questions can be found here:
                    https://docs.google.com/forms/d/1aneFYVkj3aK3hPpsC0egHf0fFnNNhcNsxML5NM6GDMk/edit
        """
        return [
            # Scenario 1
            'go through the door in front of you',
            # Scenario 2
            'take the first door on your right',
            # Scenario 3
            'take the first door on your right',
            # Scenario 4
            'go through the door on your right',
            # Scenario 5
            'go behind the desk',
            # Scenario 6
            'go through the door in front of you then turn left',
            # Scenario 7
            'go around the corridor',
            # Scenario 8
            'take the first door on your left',
            # Scenario 9
            'go to room 2 behind you',
            # Scenario 10
            'go to room 2',
            # Scenario 11
            'take the double doors on your left',
            # Scenario 12
            'go upstairs',
            # Scenario 13
            'go out of the room and then go through the next room on the right',
            # Scenario 14
            'go into the garden',
            # Scenario 15
            'go into the garden behind you',
            # Scenario 16
            'go behind the desk',
            # Scenario 17
            'go behind the sofas',
            # Scenario 18
            'walk forwards a little bit',
            # Scenario 19
            'go into the boardroom'
        ]
