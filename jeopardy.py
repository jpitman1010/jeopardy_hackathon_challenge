from flask import Flask, render_template, request, flash, session, redirect, url_for
import os
import sys
from jinja2 import StrictUndefined

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def game_stage():
    return render_template("stage.html")

@app.route('/round_one', methods = ['POST'])
def round_one():
    return render_template("round_one.html")

@app.route('/round_two', methods = ['POST'])
def round_two():
    return render_template("round_two.html")

@app.route('/final_round', methods = ['POST'])
def final_round():
    return render_template("final_round.html")

@app.route('/play_again', methods = ["POST"])
def play_again():
    return render_template("round_one.html")

# def game_play():

#     question_answer_dict = {'Tools of the Writer’s Trade': {
#     200: {"Nabokov’s novels all began on 3×5 these, which he kept under his pillow in case of inspiration": 'What is an index card?'},
#     400 : {'In 2009 this, on which Cormac McCarthy produced 5 million words, sold for over $250,000 at auction':'What is a typewriter?'},
#     600: {"At London’s Charles Dickens museum, visitors can handle Dickens’ own pen of this type": 'What is a fountain pen?'},
#     800: {"Raymond Chandler composed screenplays by talking into this machine, a brand name copyrighted in 1907": 'What is a dictaphone?'},
#     1000: {"Steinbeck was obsessed with these; the Mongol 2 3/8 model came closest to the perfect point": 'What is a pencil?'}
#     },
#     'Quarterback U.': {
#     200: {"Peyton Manning": "What is University of Tennessee?"},
#     400: {"Vince Young": "What is University of Texas?"},
#     600: {"Steve Young": "What is BYU (Brigham Young)?"},
#     800: {"Drew Brees": "What is Purdue?"},
#     1000: {"Jim Kelly & Gino Torretta": "What is University of Miami?"}
#     },
#     'The “N” Crowd':{
#     200: {"He was a great rugby & lacrosse player but he’s better known as “The Father of Basketball”": 'Who is Naismith?'},
#     400: {"Once in the news himself, today this marine colonel hosts “War Stories” on the Fox News Channel": "Who is (Ollie) North?"},
#     600: {"After a breakdown around 1919, this Russian-born ballet dancer spent the rest of his life in & out of asylums": "Who is Najinksy?"},
#     800: {"(Daily Double) – He not only won the 1971 Nobel Prize for Literature, he also served in the Chilean senate": "Who is (Pablo) Neruda?"},
#     1000: {"Egypt’s president from 1956 to 1970, he dreamed of leading the whole Arab world": "Who is Nasser?"}
#     },
#     'Rivers': {
#     200: {"As the central river artery, this is one of the world’s busiest waterways": "What is the Mississippi?"},
#     400: {"Although its ultimate source is still debated, this river flows into the Atlantic": "What is the Amazon?"},
#     600: {"From two small sources, this river flows to the North Sea": "What is the Rhine?"},
#     800: {"The head of this river is dry for much of the year and flows to an estuary on the North Sea": "What is the Thames?"},
#     1000: {"Flowing westward, this river has a drainage basin that covers seven states": "What is the Colorado?"}
#     },
#     'Flaming Foods': {
#     200: {"“Joy of Cooking” instructions for making this cherry dessert: “Standing back, ignite with a long lighted match": "What is cherries jubilee?"},
#     400: {"Henri Charpentier is said to have created this dessert crepes dish by accident; the dish was a flaming success": "What is Crepe Suzette?"},
#     600: {"You can make a flaming version of this tex-mex dish whose name means “little sashes”": "What are fajitas?"},
#     800: {"This dessert, cake & ice cream browned in the oven, can be flambeed for a dramatic presentation": "What is Baked Alaskan?"},
#     1000: {"Brennan’s in New Orleans says that this flaming fruity dessert is the most requested item on its menu": "What is Bananas Foster?"}
#     },
#     'Animals in Italian': {
#     200: {"Avoid the sting as you tell us that un’ape is this insect": "What is the bee?"},
#     400: {"If you’re called un asino, you’re either a fool, or this animal": "What is a donkey?"},
#     600: {"That’s the scariest ragno, one of these, I’ve ever seen! Don’t tell Signorina Muffet": "What is a spider?"},
#     800: {"Un cane is this; ready for walkies?": "What is a dog"},
#     1000: {"It really gets me that una capra is one of these farm animals": "What is a goat?"}
#     },
#     'The Old West': {
#     400: {"The first of his cowboy hats was called the boss of the plains; Carlsbad, the most popular model, followed": "What is Stetson?"},
#     800: {"The act of herding cattle; death was sometimes called “the last” one": "What is the roundup?"},
#     1200: {"In 1859 this Nevada town sprung up virtually overnight with the discovery of the Comstock Lode": "What is Virginia City?"},
#     1600: {"In 1867 Joseph McCoy set up a shipping yard in Abilene, Kansas to hold Texas cattle arriving on this trail": "What is Chisolm Trail"},
#     2000: {"As the result of an injury suffered in his first gunfight in 1876, he began using a cane & often used it as a weapon": "Who is Bat Masterson"}
#     },
#     'Books & Movies': {
#     400: {"The Power and the ___ Daze": "What is Glory?"},
#     800: {"The Confessions of Nat ___ and Hooch": "Who is Turner?"},
#     1200: {"The Painted ___ on a Wire": "What is Bird?"},
#     1600: {"Vanity ___ Game.":"What is Fair?"},
#     2000: {"The Red and the ___ Knight": "What is Black?"}
#     },
#     'Julius Caesar Salad': {
#     400: {"In 2008 a marble one of these was found in a French river, apparently thrown there right after Caesar’s fall.": "What is a bust?"},
#     800: {"It’s named for Julius Caesar & is sometimes written in a date as “7”": "What is July?"},
#     1200: {"In Spanish the name becomes this, as on former boxing champion Chavez" : "Who is Julio Caesar Chavez?"},
#     1600: {"(Daily Double) – This 5-word line spoken by the soothsayer is a quote from Shakespeare’s “Julius Caesar”": "What is Beware the Ides of March?"},
#     2000: {"In 45 B.C. Caesar was given permission to wear this, which he appreciated as it covered his baldness": "What is a laurel wreath?"}
#     },
#     'Boning Up': {
#     400: {"The name of this condition that affects mostly women literally means “porous bone”": "What is osteoporosis?"},
#     800: {"This fatty substance inside the bones is a major site of blood cell production": "What is the marrow?"},
#     1200: {"Your false ribs are so called because unlike your true ribs, they aren’t attached to this breastbone": "What is the sternum?"},
#     1600: {"(Daily Double) – This bone with a ball-&-socket joint at one end is about 1/4 of your height": "What is the femur?"},
#     2000: {"Most broken bones in children are this type of fracture with a colorful name, in which the break cuts only partway through the bone": "What is a greenstick?"}
#     },
#     '“Big” Stuff': {
#     400: {"Jazz musicians & jockeys helped give New York City this nickname": "What is the Big Apple?"},
#     800: {"If you’re under this, you’re at the circus": "What is the big top?"},
#     1200: {"Digit also known as the hallux": "What is the big toe?"},
#     1600: {"In France this feature of the night sky is known as “le casserole”": "What is the Big Dipper?"},
#     2000: {"Rhyming nickname of Boston’s Interstate 93 construction project": "What is the Big Dig?"}
#     },
#     'The Sanders of Time': {
#     400: {"A Louisville museum is devoted to the success story of this man who was famous for his breasts, thighs & legs": "Who is Col. Sander?"},
#     800: {"In an episode of this Garry Shandling series, the title star thinks David Duchovny is hitting on him": "What is The Larry Sanders Show?"},
#     1200: {"This Heisman trophy winner played his college ball at Oklahoma State": "Who is Barry Sanders?"},
#     1600: {"Olympic gold medal swimmer and TV personality seen here": "Who is Summer Sanders?"},
#     2000: {"On Dec. 10, 2010 he conducted a one-man, 9-hour filibuster on the Senate floor to protest a tax bill": "Who is Bernie Sanders?"}
#     }}





if __name__ == '__main__':
    #https://www.chipcage.com/jeopardy/questions/
    # game_stage()
    app.run(host='0.0.0.0', debug=True, use_reloader=True)