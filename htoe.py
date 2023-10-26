from google.transliteration import transliterate_text
from googletrans import Translator
import math

from googletrans import Translator
import openpyxl
import xlwt
from xlwt import Workbook
from elt import translit
import gender_guesser.detector as gender
from guess_indian_gender import IndianGenderPredictor
from genderize import Genderize

# result = transliterate_text('आपके', lang_code='hi')
# print(result)
fathersample="फादर रमेश फादर राम फादर सीता सुनीता"

translator = Translator()
transliterated_father = translator.translate(fathersample, dest='hi').pronunciation
# transliterated_father = [sub.replace('phaadar', 'father') for sub in transliterated_father]
print(transliterated_father)

# print(type(sample))
# hinditext = "कमल,सुरज,आग,शांतिबाई,सुनीता,पार्वती,"
# hinditextar = ["नमस्ते आप कहा से है ","कमल","सुरज"]
# english = ["aap", "kamal", "Hello"]
# kamal = "कमल"
# suraj = "सुरज"
# aag = "आग"
# santi = "शांतिबाई"

# # translated_txt = translator.translate(my_input, dest='hi').text
# # print(translated_txt),
# transliterated_txt4 = translator.translate(sample, dest='hi').pronunciation
# transliterated_txt4 = translator.translate(hinditextar, dest='hi').pronunciation
# # transliterated_txt = translator.translate(kamal, dest='hi').pronunciation
# # transliterated_txt1 = translator.translate(santi, dest='hi').pronunciation
# transliterated_txt2 = translator.translate(suraj, dest='hi').pronunciation
# print(transliterated_txt4)
# to_hindi = translit('english')
# print(to_hindi.convert(english))


def addgender(name):
    print("Gender Adding...")
    d = gender.Detector()

    guessed_gender = d.get_gender(name[0])
    i = IndianGenderPredictor()
    half = []
    for j in range(100):
        half.append(name[j])

    print(i.predict(name=name[0]))

    g = Genderize()
    # arr = g.get(half)
    print(guessed_gender)
    print("Add gender done")

    # return arr

    # The get_gender method returns 'mostly_male' or 'mostly_female'
    # if the gender is not clear, we consider these cases as 'unknown'
    # if guessed_gender == 'mostly_female':
    #     return 'female'
    # if guessed_gender in ['mostly_male', 'andy','unknown']:
    #     return 'male'
    # else:
    #     return guessed_gender