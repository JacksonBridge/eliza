# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# eliza
# 
# Jackson Hambridge
# CMSC 416 - 1 January 2020
# This program will start a dialogue with the user.
# Please input clear, correct sentences.
# Eliza will turn inputted phrases into dialogue.
# Run this program in Python 3 in the command line
# Elize will prompt the user.  For example...
#
# >> [Eliza] What is on your mind today?
# >> I am sad.
# >> [Eliza] Why are you sad?
# >> I missed my birthday.
# >> Why did you miss your birthday?
#
# Eliza tests for key words such as 'am' 'were' 'are'
# or tenses such as -'ed' and converts them into questions.
# 
# Eliza checks for 'to be' verbs in different tenses as well
#
# 'goodbye' will end the program
# If asked a question, Eliza will redirect the user
# 
# First Eliza detects the user's name, searching for 'is' 'am' or just a single word inputted
# Then, when a line is inputted, the program will remove the end punctuation.
# If there are multiple "I" statements, Eliza will take the last one.
# Then, keywords are tested for in a certain order.
# If none of the keywords are included, Eliza will ask a generic statement.
#


import re
import random



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# splitLine
# This method splits the parameter by a the space delimeter.
def splitLine(line):
    splitLine=re.split('\s',line)
    return splitLine



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# getName
# This method will return the word after 'is' or 'am' or just
# the word if there is only one word.
def getName(line):
    splitLine = re.split('\s',line)

    name="ybnpbipkjd"

    count=0
    if re.search(r'is',line) is not None:
        for token in splitLine:
            if token == "is" or token == "am":
                nameLocation=count+1
            count=count+1  
        name=splitLine[nameLocation]
        name=re.sub(r'\.',"",name)
    else:
        if len(splitLine) == 1:
            name=splitLine[0]
            name=re.sub(r'\.',"",name)
            print("[Eliza] Not very chatty, are we?")

    if name=="ybnpbipkjd":
        print("[Eliza] Sorry, I didn't quite catch that.")
        return getName(input())

    return name



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# sub
# This method finds and replaces a string within a string
def sub(find, replace, line):
    line=re.sub(find,replace,line)
    return line




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# splitLine
# This method splits the parameter by a the space delimeter.
def search(find,line):
    if re.search(find,line) is not None:
        return 1
    else:
        return 0



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# changePosession
# Change the ownership of posessive pronouns
# ex. from 'me' to 'you'
def changePosession(line):

    split=splitLine(line)
    count=0
    newLine=""
    # This ensures that "me" in not included in a word, such as "name"
    for tokens in split:
        if search("[A-Za-z]+me",tokens) == 0 and search("[Mm]e[A-Za-z]+",tokens) == 0:
            tokens=sub("me","you",tokens)
        newLine=newLine+" "+tokens

    # Getting rid of that pesky double space
    lineListed=list(newLine)
    lineListed[0]=""
    line="".join(lineListed)

    # Change posession
    line=sub(" me "," you ",line)
    line=sub(" my "," your ",line)
    line=sub("My ","Your ",line)
    line=sub("I ","you ",line)
    line=sub("myself","yourself",line)
    line=line.lower()
    return line



def countWord(word,line):
    split=splitLine(line)
    count=0
    for tokens in split:
        if tokens==word:
            count=count+1
    return count



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# toQuestion
# This method converts a sentence to a question
def toQuestion(line,name):
    line=sub("\.","",sub("!","",line))

    # Randomize Eliza saying the name
    if random.randint(0,5)==1:
        name=", " + name
    else:
        name=""

    # Silence
    if line=="":
        return "Don't be shy. How have you been feeling lately?"

    # I - counter
    # If there are multiple I's in the sentence, take the last one.
    if countWord("I",line)>1:
        line=sub(".*I ","I ",line)

    # Question
    # If the user asks a question, Eliza redirects them
    if search("\?",line):
        if search(" I ",line):
            return "Tell me more."
        return "Let's get back to you" + name + "."

    # Personal 'to be' verbs
    # Search for "am" and "was" so that alexa may ask "why are" or "why were"
    if search(" am ",line) and search("I",line):
        keyFeeling=sub(".*am ","",line)
        keyFeeling=changePosession(keyFeeling)
        return "Why are you " + keyFeeling + name + "?"
    if search(" was ",line) and search("I",line):
        keyFeeling=sub(".*was ","",line)
        keyFeeling=changePosession(keyFeeling)
        return "Why were you " + keyFeeling + name + "?"

    # 'is' without 'I'
    # Search for "is" without "I" which implies that some other noun *is* some description
    if search(" is ",line) and not search("I ",line):
            line=changePosession(line)
            line=sub(" is "," ",line)
            return "Why is " + line + name + "?"

    # Special, common verbs
    # 'do' --> 'Why do...?'
    if search(" do ",line):
        line=sub("do ","",line)
        line=changePosession(line)
        return "Why do " + line + name + "?"
    # 'does' --> 'Why does...?'
    if search(" does ",line):
        line=sub("does ","",line)
        line=changePosession(line)
        return "Why does " + line + name + "?"
    # 'did' --> 'Why did...?'
    if search(" did ",line):
        line=sub("did ","",line)
        line=changePosession(line)
        return "Why did " + line + name + "?"
    # 'can' --> 'Why can...?'
    if search(" can ",line):
        line=sub("can ","",line)
        line=changePosession(line)
        return "How can " + line + name + "?"
    # 'will' --> 'Why will...?'
    if search(" will ",line):
        line=sub("will ","",line)
        line=changePosession(line)
        return "Why will " + line + name + "?"
    # 'went' --> 'Why did... do...?'
    if search(" went ",line):
        line=sub("went ","go ",line)
        line=changePosession(line)
        return "Why did " + line + name + "?"

    # Sentences with 'I' as the subject.
    if search("I",line):
        if search("I [A-Za-z]+ed",line):
            line=changePosession(line) 
            return "Why do you think " + line + name + "?"
        line=sub(".*I ","I ",line)
        line=changePosession(line)
        return "Why do you think " + line + name + "?"

    # Special verbs when the subject isn't 'I'
    # are --> Why are...?
    if search(" are ",line):
        keyObject=sub(" are "," ",line)
        keyObject=changePosession(keyObject)
        return "Why are " + keyObject + name + "?"
    # were --> Why were...?
    if search(" were ",line):
        keyObject=sub(" were "," ",line)
        keyObject=changePosession(keyObject)
        return "Why were " + keyObject + name + "?"
    # was --> Why was...?
    if search(" was ",line):
        keyObject=sub(" was "," ",line)
        keyObject=changePosession(keyObject)
        return "Why was " + keyObject + name + "?"
    # can --> Why can...?
    if search(" can ",line):
        keyObject=sub(" can "," ",line)
        keyObject=changePosession(keyObject)
        return "Why do you think " + keyObject + name + "?"
    # will be --> Why will... be...?
    if search(" will be ",line) == 1:
        keyFeeling = sub(".*be ","",line)
        keyFeeling = sub("\.","",keyFeeling)
        return "Why will you be " + keyFeeling + name + "?"

    # Catch-all for any regular past tense verb.
    if search(" [A-Za-z]+ed",line):
        line=changePosession(line) 
        return "Why do you think " + line + name + "?"

    # Final statement
    line=changePosession(line)
    end=random.randint(1,5)
    if end==1:
        return "What do you mean when you say " + line + name + "?"
    if end==2:
        return "What you mean by " + line + name + "."
    if end==3:
        return "Why do you think that " + line + name + "?"
    if end==4:
        return "Why do you think that is?"
    if end==5:
        return "Why do you think that " + line + name + "?"
    
# Welcoming statement
print("[Eliza] Hello! My name is Eliza. What is your name?")

# Gather input
line = input()

# Get name
name = getName(line)

# Prompt user
print("[Eliza] Welcome, " + name + "! What is on your mind today?")

present=1
while(present==1):
    line=input()
    # The keyword 'Goodbye' will exit the Eliza
    if search("[Gg]oodbye",line):
        present=0
        print("[Eliza] " + name + ", thank you for coming in today. Have a great day!")
    else:
        print("[Eliza] " + toQuestion(line,name))