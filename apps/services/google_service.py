import json
import gspread

import google.generativeai as genai

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

GEMINI_API_KEY = ''

with open("gemini.json") as jsonFile:
    GEMINI_API_KEY = json.load(jsonFile)['key']
    genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("How old was Don Bosco when he died, what is the latest news of the Salesian brotherhood?")

print(response.text)

def get_question_sets():
    question_sets = []
    for item in listOfLists:
        question_sets.append({'question': item[REFRESHER_QUESTION_1_INDEX], 'correct_answer': item[REFRESHER_ANSWER_1_INDEX]})
        question_sets.append({'question': item[REFRESHER_QUESTION_2_INDEX], 'correct_answer': item[REFRESHER_ANSWER_2_INDEX]})
        question_sets.append({'question': item[REFRESHER_QUESTION_3_INDEX], 'correct_answer': item[REFRESHER_ANSWER_3_INDEX]})
    return question_sets

def get_learnings():
    return_value = []
    for item in listOfLists:
        return_value.append(item[SUMMARY_INDEX])
    return return_value
    
