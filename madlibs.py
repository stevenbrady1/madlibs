from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_word(word_type):
    """Function to get a random word based on the type"""
    words = {
        'noun': ['dog','car','banana','moutain', 'cookie'],
        'verb': ['run', 'jump', 'eat', 'sleep', 'drive'],
        'adjective': ['big', 'yellow', 'quick', 'lazy', 'fun'],
        'adverb' : ['quickly', 'lazily', 'happliy', 'sadly'],
        'place' : ['park','restaurant', 'school', 'zoo', 'museum'],
        'exclamation' : ['Wow', 'Oh no', 'Hooray', 'Yikes', 'Ooops'],
    }
    return random.choice(words[word_type])

def create_story():
    """Function to get a random story based on a template"""
    story_template = (
        "{exclamation}! Today I went to the {place} and saw a very {adjective} {noun}."
        "It was {adverb} {verb}ing around! I couldn't believe my eayes, so I decided to"
        "{verb} along with it, What a day!" 
    )

    #Replace placeholders with randoom vars
    story = story_template.format(
        exclamation=get_word('exclamation'),
        place=get_word('place'),
        adjective=get_word('adjective'),
        noun=get_word('noun'),
        adverb=get_word('adverb'),
        verb=get_word('verb')
    )

    return story

@app.route('/')
def home():
    return create_story()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)