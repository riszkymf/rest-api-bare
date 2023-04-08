import json
from random import randint
from libs import lorem

def gen_text(word_count):
    text = []
    while len(text) < word_count:
        paragraph = lorem.paragraph().split(" ")
        text.extend(paragraph)
    return " ".join(text)


def generate_toaster_payload():
    question = gen_text(randint(270,320))
    response = gen_text(randint(270,320))
    r_count = randint(4,10)
    r_data = {}
    for i in range(0,r_count):
        r_data["R{}".format(str(i))] = randint(1,10)/10

    result = {
        "Query": {
            "question": question,
            "response": response
        }
    }
    result.update(r_data)
    return result


def generate_payload():
    list_query = []
    for i in range(0,randint(1,5)):
        list_query.append(generate_toaster_payload())
    

    data_struct = {
    "Assessment": {
        "Origin": "ERX233",
        "Designator": "AP101",
        "Toaster": list_query
        }
    }
    return data_struct