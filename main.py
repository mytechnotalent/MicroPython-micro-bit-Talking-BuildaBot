import gc
import time

from microbit import display, Image
from speech import say

# Our Python dictionary which is a database
# and here is where we can type in new key/value
# pairs or in our case trigger word or words and
# then a response as our little friend will learn
# from us and will add what it learns into the 
# database or db and when it loses power
# it will forget however this is our chance
# to build a bot of our own and teach our 
# friend like it is a new born baby everything 
# we want it to understand so all you have to do
# is uncomment line 24 and give a trigger word
# or words and a response separated by a "-" 
# dash and save and then flash and our little
# friend will remember this forever
db = {
        'hi': 'Hi to you!',
        'hello': 'Hello to you!',
        # 'test': 'Test response!'.
     }

# Customize bot speaking speed
SPEED = 95

# Our little friend wants to show how happy it is to 
# talk to us so it smiles wide when it wakes up
display.show(Image.HAPPY)

# Our little friend is going to enter in a big
# loop to talk to us
while True:
    try:
        # This is an advanced topic as well however this little function
        # cleans out the unnecessary global objects or variables on what
        # we call the heap area in memory
        gc.collect()
        
        # We want to clear the response so our little friend can get a 
        # new response from you
        response_ = ''
        
        # Here is where you interact with our little friend
        response = input('YOU: ')
        
        # We want to make sure that our dictionary database can 
        # find all values even if you use a capital letter
        # so we convert everything to lowercase 
        response = response.lower()
        
        # If you type something other than pressing enter that means 
        # response has a value so the rest of the code will continue
        # on
        if response:
            # This is a bit complicated do not worry about this for now
            # all this is doing is looking through our dictionary database
            # and seeing if our input value has the word or words which
            # match an entry in the dictionary database and if it does
            # put the value in the _response object
            response_ = [val for key, val in db.items() if key in response]
            gc.collect()
            
            # If our little friend got a response from us then make sure
            # we trigger the speaking or suprised image so our little friend
            # can open its mouth to talk and then have our little friend
            # talk to us in our REPL and by hearing it speak as well
            if response_:
                display.show(Image.SURPRISED)
                print('BOT: {0}'.format(response_[0]))
                say(str(response_[0]), speed=SPEED)
                display.show(Image.HAPPY)
                
            # If you type the word "teach" pass to the next if statement for
            # processing
            if response == 'teach':
                pass
                
            # If this is not a response in our dictionary database and it is
            # not the word teach, our little friend is confused and wants to 
            # learn from us so this is where you get to teach our little friend
            # so it is going to print out a response in the REPL and speak to 
            # us as well
            if not response_ and response != 'teach':
                display.show(Image.SURPRISED)
                print('BOT: I do not understand.  Please type the word "teach" to teach me.')
                say('I do not understand.  Please type the word teach to teach me.', speed=SPEED)
                display.show(Image.HAPPY)
        
        # If we type the word "teach" then our little friend is excited to learn from us
        # so we type a trigger word or words like "name - My name is George." as we see
        # that we use the "-" to separate the trigger word or words from how we want our 
        # little friend to respond to us
        if response == 'teach':
            display.show(Image.SURPRISED)
            say('Type the trigger word or words. then type a dash, then type a response.', speed=SPEED)
            response = input('BOT: Type Trigger Word/Words - Response: ')
            display.show(Image.HAPPY)
            if response:
                while True:
                    if response:
                        response = response.split(' - ')
                        key = response[0]
                        try:
                            value = response[1]
                            db[key] = value
                        except IndexError:
                            break
                        break
    
    # If we type in blank data our dictionary database wont know what to do
    # so it will pass and redo the loop
    except IndexError:
        gc.collect()
 
    # If we want to end the program and get back to a REPL by pressing 
    # CTRL + C
    except KeyboardInterrupt:
        break
