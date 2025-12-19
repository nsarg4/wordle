import arcade
import random

import arcade.csscolor
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Wordle"

class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.guess=""
        self.count = 1
        self.guess_list = ["","","","","",""]
        self.winner = False
        arcade.set_background_color(arcade.color.WHITE)



    def setup(self):
        self.words = [
    "apple", "bread", "chair", "dance", "eagle", "flame", "grape", "house", "islet", "joker",
    "knife", "light", "march", "night", "ocean", "party", "quilt", "river", "sight", "table",
    "uncle", "vivid", "whale", "xenon", "yacht", "zebra", "adobe", "bison", "crown", "dwarf",
    "emote", "field", "globe", "happy", "input", "jolly", "karma", "lemon", "mirth", "noble",
    "olive", "plant", "queen", "realm", "smile", "tiger", "unity", "voter", "witty", "xerox",
    "yield", "zesty", "acorn", "blaze", "clerk", "dream", "elite", "fancy", "grill", "hound",
    "index", "joker", "kneel", "lunar", "magic", "nurse", "optic", "piano", "quote", "rouge",
    "siren", "trust", "urban", "vogue", "woven", "xylos", "yearn", "zephyr", "amber", "brick",
    "cabin", "delta", "eject", "flood", "grove", "hound", "ivory", "jewel", "kings", "latch",
    "mango", "niche", "orbit", "penny", "quirk", "raven", "savvy", "toast", "ultra", "vigor"
]
        self.current_word = random.choice(self.words)
        

    def on_draw(self):
        arcade.start_render()

        first_y = 100

        for i in range(6):
            first_x =150
            for j in range(5):
                arcade.draw_rectangle_outline(first_x, first_y, 100, 100, arcade.color.BLACK, 5)
                first_x += 100
            first_y += 100


        
        letter_y = 600
        for i in range(6):
            letter_x = 150

            if i < self.count - 1 or (self.winner and i == self.count - 1):
                for j in range(5):
                    color = arcade.csscolor.GRAY
                    if self.guess_list[i][j] in self.current_word:
                        if self.guess_list[i][j] == self.current_word[j]:
                            color = arcade.csscolor.SPRING_GREEN
                        else:
                            color = arcade.csscolor.YELLOW
                    arcade.draw_text(self.guess_list[i][j].upper(), letter_x, letter_y, color, 20) 
                    letter_x+=100
                letter_y -= 100
                if self.count > 6 and not self.winner:
                    arcade.draw_text(f'You have used all your tries. The correct word: {self.current_word}', 10, 10, arcade.csscolor.BLUE, 18) 

                
            else:

                for j in self.guess_list[i]:
                    arcade.draw_text(j.upper(), letter_x, letter_y, arcade.csscolor.BLACK, 20) 
                    letter_x+=100
                letter_y -= 100
        
        if self.winner:
            arcade.draw_text("YOU GUESSED THE WORD!!!", 180, 10, arcade.csscolor.RED, 18)



    def on_key_press(self, key, modifiers):
        if self.winner:
            return

        if key == arcade.key.BACKSPACE:
            if len(self.guess) > 0:
                self.guess = self.guess[:-1]
                self.guess_list[self.count-1] = self.guess

        elif key == arcade.key.ENTER:
            if len(self.guess) == 5:
                if self.guess == self.current_word:
                    self.winner = True
                
                elif self.count < 6:
                    self.count += 1
                    self.guess = ""
                else:
                    self.count += 1 

        elif len(self.guess) < 5:
            try:
                letter = chr(key).lower()
                if letter.isalpha():
                    self.guess += letter
                    self.guess_list[self.count-1] = self.guess
            except:
                pass

    
   
    def update(self, delta_time):
       pass
               


        
def main():
    window = MyGame()
    window.setup()
    arcade.run()

main()