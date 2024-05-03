import secrets
import gspread

from flask import url_for

from gspread.utils import GridRangeType

gc = gspread.service_account('key.json')

wks = gc.open("Myra's Study End Form (Responses)").sheet1
listOfLists = wks.get(return_type=GridRangeType.ListOfLists)
# first row is ignored
listOfLists.pop(0)

# indexes
SUMMARY_INDEX = 1
REFRESHER_QUESTION_1_INDEX = 2
REFRESHER_ANSWER_1_INDEX = 3
REFRESHER_QUESTION_2_INDEX = 4
REFRESHER_ANSWER_2_INDEX = 5
REFRESHER_QUESTION_3_INDEX = 6
REFRESHER_ANSWER_3_INDEX = 7


def get_context():
    return None

def get_learnings():
    return_value = []
    for item in listOfLists:
        return_value.append(item[SUMMARY_INDEX])
    return return_value