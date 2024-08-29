import re
import random

class RuleBot():
    # Negative Responses
    negative_responses = ("No.", "I don’t want to.", "I’m not interested in that.", "I refuse.", "I’m not going to do that.", 
                          "Nah", "no")
    # Exit Responses
    exit_responses = ("Goodbye", "Bye","See you later", "I’m done", "End chat", "Quit", "Exit", "I'm leaving",
                      "Talk to you later", "I have to go", "Logging off", "Close conversation","That's all",
                        "Stop", "Cancel", "No more", "Finish")
    
    # Starter Questions
    alien_questions = (
        "What is this place called Earth?\n",
        "Why are you here?\n",
        "Are there many humans like you?\n",
        "Does Earth have a leader?\n",
        "What technology do you have in this planet?\n"
    )



    def __init__(self):
        self.alien = {'describe_planet': r'.*\s*your planet.*',
                      'introduce_yourself': r'what is\s.* | \s.*you\s.*'
                      }
        
    def great(self):
        self.name = input("What's your name? ")
        will_help = input(f"Hello {self.name}! I'm a robot landed here. Could I ask you somethings about you planet?\n")
        if will_help in self.negative_responses:
            print("Okay, have a nice day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_responses:
            if command == reply:
                print("Okay, Thank you for your time. GoodBye!")
                return True
    
    def match_reply(self, reply):
        for key, value in self.alien.items():
            intent = key
            regex = value
            found_match = re.match(regex, reply)
            if found_match:
                if intent == 'describe_planet':
                    return self.describe_planet()
                elif intent == 'introduce_yourself':
                    return self.introduce_robot()
                
            else:
                return self.no_match_intent()
            
    def describe_planet(self):
        describe_planet_responses = (
        "My planet is a vast, barren world with towering mountains and deep, shadowy valleys. The sky is a swirling mix of purple and green, and the air is thin but sweet.\n",
        "Our home is covered in endless oceans of liquid methane, with massive floating cities that drift across the surface. We rarely see the ground, but when we do, it's a rugged, icy landscape.\n",
        "The surface of my planet is dotted with enormous crystalline structures that sparkle in the light of our twin suns. We have no trees or plants like Earth, but our world is rich with strange and colorful life forms.\n"
        )
        return random.choice(describe_planet_responses)
    
    def introduce_robot(self):
        describe_robot_responses = (
        "I am an advanced exploration unit designed to study and interact with new civilizations. My core is powered by a fusion reactor, and my sensors can detect a wide range of environmental data.\n",
        "I am a robotic envoy from my planet, equipped with artificial intelligence and designed to learn about your species.\n",
        "As a robotic emissary, I am programmed to observe, communicate, and share knowledge. My systems include language processing, environmental analysis, and a database of information collected from across the galaxy.\n"
        )
        return random.choice(describe_robot_responses)
    
    def no_match_intent(self):
        responses = ("Please tell me more!\n", "very nice! what else?\n",
                     "I see. can you ellaborate?\n", "why?\n",
                     "How do you think I feel when you say that?\n")
        return random.choice(responses)

    def chat(self):
        reply = input(random.choice(self.alien_questions))
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    
AlienBot = RuleBot()
AlienBot.great()