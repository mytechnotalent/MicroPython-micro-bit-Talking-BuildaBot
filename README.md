![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/MicroPython-micro-bit%20Talking%20BuildaBot.png?raw=true)

# MicroPython micro:bit
# Talking BuildaBot
This is a FUN talking BuildaBot for the official BBC micro:bit V2 where you get to build your VERY OWN TALKING BOT FROM SCRATCH!

## Schematic
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/schematic.png?raw=true)

## Parts
[micro:bit](https://microbit.org/buy/?location=US&version=microbitV2)

## STEP 1: Navigate To The FREE micro:bit Python Web Editor
[micro:bit Python Web Editor](https://python.microbit.org/v/beta)<br><br>
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%201.png?raw=true)

## STEP 2: Plug micro:bit V2 Into Computer
***PLUG IN USB CABLE TO COMPUTER AND DEVICE**

## STEP 3: Click CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%203.png?raw=true)

## STEP 4: Click "BBC micro:bit CMSIS-DAP" & CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%204.png?raw=true)

## STEP 5: Highlight Sample Code - Select All
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%205.png?raw=true)

## STEP 6: Click Backspace On Keyboard To Delete Sample Code
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%206.png?raw=true)

## STEP 7: Copy Talking TODOBot Python Code Template Into Python Web Editor
# CODE
```python
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
```

## STEP 8: Rename Script Name To talking_buildabot

## STEP 9: Click Save
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%209.png?raw=true)

## STEP 10: Click Download Python Script
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%2010.png?raw=true)

## STEP 11: Click Flash
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%2011.png?raw=true)

## STEP 12: Click Open Serial
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_BuildaBot/blob/main/STEP%2012.png?raw=true)

## STEP 13: Interact With Baby BuildaBot, Teach It Everything You Want!
This is a little itty bitty baby BuildaBot that only knows how to respond to "hi"
or "hello" so this is a great chance to teach it everything you want by typing the word
"teach" and then it will prompt you for a trigger word or words and then a response and
it will LEARN FROM YOU!<br>
*** NOTE *** Make sure your trigger word or words do not use any punctuation of any kind when teaching the bot.
```
YOU: hi
BOT: Hi to you!
YOU: How are you?
BOT: I do not understand.  Please type the word "teach" to teach me.
YOU: teach
BOT: Type Trigger Word/Words - Response: how are you - I am great thank you!
YOU: How are you?
BOT: I am great thank you!
```

## STEP 14: Teach BuildaBot Permanently
Our little friend will forget what it learned when it loses power or gets 
reset however this is a GREAT opportunity to learn a little Python and type in some things
we would LOVE our little friend to learn and keep in its little brain forever!
* STEP 10A: Edit Original Code (Lines 21 - 25)
```python
...
db = {
        'hi': 'Hi to you!',
        'hello': 'Hello to you!',
        'how are you': 'I am great thank you!',
     }
...
```

* STEP 9: Click Save

* STEP 10: Click Download Python Script

* STEP 11: Click Flash

* STEP 12: Click Open Serial

* STEP 15: Interact With Baby BuildaBot After It Learned From You!<br>
*** NOTE *** Make sure your trigger word or words do not use any punctuation of any kind when teaching the bot.
```
YOU: How are you?
BOT: I am great thank you!
```

## STEP 16: Keep On Adding To The Python Dictionary Database
Great job!  You permanently taught little baby BuildaBot something awesome!  Now you can continue step 10 over ande over as many times as you like to keep building its knowledge base.  In the process you are also learning a little Python as what you just edited is called a Python dictionary where you get to add key and value pairs to teach our little friend ina very FUN WAY!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
