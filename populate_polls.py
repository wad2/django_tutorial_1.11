import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()

from polls.models import Question, Choice
from datetime import datetime

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    question1_choices = [
        {"choice_text": "The sky", "votes": 5},
        {"choice_text": "Just hacking", "votes": 8},
        {"choice_text": "Not much", "votes": 2},]

    question2_choices = [
        {"choice_text": "Paris", "votes": 5},
        {"choice_text": "Berlin", "votes": 1},
        {"choice_text": "Brussels", "votes": 3},]


    question3_choices = [
        {"choice_text": "The Spice Girls", "votes": 2},
        {"choice_text": "Atomic Kitten", "votes": 5},
        {"choice_text": "The Proclaimers", "votes": 12},]

    question4_choices = [
        {"choice_text": "1513", "votes": 5},
        {"choice_text": "1314", "votes": 1},
        {"choice_text": "1746", "votes": 3},]

    question5_choices = [
        {"choice_text": "William Shakespeare", "votes": 2},
        {"choice_text": "Charles Dickens", "votes": 5},
        {"choice_text": "Walter Scott", "votes": 9},]

    questions = {"What's up?": {"choices": question1_choices, "pub_date": datetime(2016, 10, 17, 15, 30)},
                 "What is the capital of France?": {"choices": question2_choices, "pub_date": datetime(2016, 8, 27, 10, 46)},
                 "Who would walk 500 miles?": {"choices": question3_choices, "pub_date": datetime(2016, 9, 16, 13, 14)},
                 "When was the Battle of Flodden?": {"choices": question4_choices, "pub_date": datetime(2016, 2, 13, 20, 52)},
                 "Who wrote \"Waverley\"?": {"choices": question5_choices, "pub_date": datetime(2016, 10, 15, 8, 9)}}

    for question, question_data in questions.items():
        q = add_question(question, question_data["pub_date"])
        for c in question_data["choices"]:
            add_choice(q, c["choice_text"], c["votes"])

    # Print out the categories we have added.
    for q in Question.objects.all():
        for c in Choice.objects.filter(question=q):
            print("- {0} - {1}".format(str(q), str(c)))

def add_choice(question, choice_text, votes):
    choice = Choice.objects.get_or_create(question=question, choice_text=choice_text)[0]
    choice.votes = votes
    choice.save()
    return choice

def add_question(question_text, pub_date):
    question = Question.objects.get_or_create(question_text=question_text, pub_date=pub_date)[0]
    question.save()
    return question

# Start execution here!
if __name__ == '__main__':
    print("Starting Polls population script...")
    populate()