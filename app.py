from flask import Flask, request, render_template_string

app = Flask(__name__)

danger=''' ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
    '''
header_ascii = '''
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \\
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \\__|_|  \\___|\\__,_|___/\\__,_|_|  \\___|
'''

treasure_ascii = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /  
*******************************************************************************
'''


def render_page(content):
    return render_template_string(f'''
    <html>
        <head>
            <style>
                body {{
                    background-color: black;
                    color: #39ff14; 
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 0;
                    padding: 20px;
                }}
                pre {{
                    font-family: monospace;
                    font-size: 16px;
                    white-space: pre-wrap;
                }}
                .header {{
                    margin-bottom: 30px;
                }}
                .content {{
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Welcome to Treasure Island</h1>
                <pre>{header_ascii}</pre>
                <p>Your mission is to find the treasure.</p>
            </div>
            <div class="content">
                {content}
            </div>
        </body>
    </html>
    ''')


@app.route('/')
def index():
    content = '''
        <form action="/step1">
            <label for="choice">Type (left or right)<br>
               Left Path:- Leads to a dense forest.<br>
               Right Path:-Leads to rocky cliffs, where the waves crash violently below. :<br></label><br>
            <input type="text" name="choice" id="choice" required>
            <br><br>
            <button type="submit">Submit</button>
        </form>
    '''
    return render_page(content)

@app.route('/step1')
def step1():
    choice = request.args.get('choice', '').lower()
    if choice == 'right':
        content = f"<h2><pre>{danger}</pre>Game Over! You fell into a pit.</h2>"
    elif choice == 'left':
        content = '''
            <h2>You suddenly notice there’s a small island in the distance 
            <br> So now to reach the island u have 2 choices 
            <br>Swim: You could dive in and try your luck, hoping to make it to the island. You’d have to battle the current, but maybe you’re a strong swimmer.
            <br>Build a Raft: On the shore, you notice some logs, vines, and branches, you can make a raft.
            <br>Do u want to Swim across or Build a raft?<br>
                Type(swim/build)</h2>
            <form action="/step2">
                <input type="text" name="choice" required>
                <br><br>
                <button type="submit">Submit</button>
            </form>
        '''
    else:
        content = f"<h2><pre>{danger}</pre>Invalid choice. Game Over!</h2>"
    return render_page(content)

@app.route('/step2')
def step2():
    choice = request.args.get('choice', '').lower()
    if choice == 'swim':
        content = f"<h2><pre>{danger}</pre>Game Over! You were eaten by crocodiles.</h2>"
    elif choice == 'build':
        content = '''
            <h2>Now u have reached the island but then
                <br>You stumble upon an abandoned village. Inside a hut, you find three objects:<br>
                1.A sword (good for combat).<br>
                2.A torch (useful for exploring caves).<br>
                3.A key (mystical, but purpose unknown).<br>
                Type(sword/torch/key)</h2>
            <form action="/step3">
                <input type="text" name="choice" required>
                <br><br>
                <button type="submit">Submit</button>
            </form>
        '''
    else:
        content = f"<h2><pre>{danger}</pre>Invalid choice. Game Over!</h2>"
    return render_page(content)
@app.route('/step3')
def step3():
    choice = request.args.get('choice', '').lower()
    if choice == 'sword':
        content = f"<h2>'<pre>{danger}</pre>You grab the sword with great excitement, but as soon as you swing it, it gets stuck in a tree. Now you’re just standing there, holding a tree in the air awkwardly. <br>Well done, hero!! but Game Over! .</h2>"
    elif choice == 'torch':
        content = f"<h2>'<pre>{danger}</pre>You take the torch and light it, only to realize you're standing in broad daylight. Now you're just holding a burning stick. Not very helpful, huh? Game Over! '"
    elif choice == 'key':
        content = '''
             <h2>'You stand before three doors, each one painted a different color. A dusty, old sign above them reads:<br>
                  Pick a door, any door... but choose wisely, adventurer! Not all doors lead to glory!<br>
                  Take a deep breath, and choose carefully! Will you go for the fiery red, the mysterious blue, or the suspiciously shiny yellow?
                  <br> Type(red/blue/yellow)'
                  </h2>
            <form action="/step4">
                <input type="text" name="choice" required>
                <br><br>
                <button type="submit">Submit</button>
            </form>
        '''
    else:
        content = f"<h2><pre>{danger}</pre>Invalid choice. Game Over!</h2>"
    return render_page(content)


@app.route('/step4')
def step4():
    choice = request.args.get('choice', '').lower()
    if choice == 'red':
        content = (f"<h2><pre>{danger}</pre>You open the red door and walk right into a super hot kitchen! There’s a giant oven that seems mad at you. Everything is way too spicy, and the heat is making you sweat. "
                   "<br>You try to leave, but the door won’t open! Looks like you’re stuck as the chef’s new helper...Game Over!!</h2>")
    elif choice == 'blue':
        content = f"<h2><pre>{danger}</pre>You step through the blue door and find yourself face-to-face with a giant inflatable whale. It looks cute, but before you know it, it starts pushing you out like you’re just another beach ball! You try explaining you're here for treasure, but the whale doesn’t care. It’s too busy playing with its giant ball. Not the treasure hunt you expected. Game Over!!</h2>"
    elif choice == 'yellow':
        content ='''
             <h2>'You open the yellow door and step into a room u find a chest <br>
                    As you reach for the glittering chest, a sudden chill fills the air. From the shadows, a glowing figure steps forward. It’s the Guardian of the Treasure, and It seems both serious and surprisingly funny at the same time.
                    <br>"You've come far, but before you claim your prize, I have a little riddle for you," the Guardian says with a grin.
                    <br>"I am not alive, but I grow;
                    <br>I don’t have lungs, but I need air;
                    <br>I don’t have a mouth, but water kills me.
                    <br>What am I?"
                    <br> The Guardian gives you a sly wink. "Answer correctly, and the treasure is yours."(hint:- The word starts with f)'</h2>
            <form action="/step5">
                <input type="text" name="choice" required>
                <br><br>
                <button type="submit">Submit</button>
            </form>
        '''
    else:
        content = "<h2>Invalid choice. Game Over!</h2>"
    return render_page(content)
@app.route('/step5')
def step5():
    choice = request.args.get('choice', '').lower()
    if choice == 'fire':
        content =f"<h2>Congratulations! You found the treasure!<pre >{treasure_ascii}</pre></h2>"
    else:
        content =f'''
                    "<h2>'<pre>{danger}</pre>"Nice try, but that's not quite right." The treasure chest remains firmly locked,
                    "You've got the wrong answer, adventurer. But don’t worry, every great treasure hunter has to fail a few times first!" The Guardian winks'</h2>"
                '''
    return render_page(content)
if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')