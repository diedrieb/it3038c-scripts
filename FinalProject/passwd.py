#importing the random module for generating random characters 
import random
#Importing the string module will allow for us combine our variables into a single string (The generated password)
import string 
#Importing the pyqrcode module will allow for us to create a unique QR code that will take us to a specific webpage once it is scanned from our phone's camera
import pyqrcode
#Importing the png module will allow us to get a custom QR code in PNG image format within our File Explorer. This allows for quick and easy access to our code via Windows. 
import png

#This section of the project will allow for the user to input a unqiue username of their choice that will be used later in the authentication function. 
username = input("Please Enter A Username For Your Account:")
print("Remember To Write This Username Down:" + username)

#Description of the Password Generator 
print("You Are Now Utilizing The Epic Password Generator!")

#This is a list of adjectives that will be pulled in order to generate our unqiue, complex password. 
adjective = ['alive', 'annoyed', 'blue', 'green', 'bored', 'charming',

                    'clean', 'defiant', 'doubtful', 'expensive', 'fair',
                    
                    'funny', 'good', 'hungry', 'important', 'jolly', 'lazy', 
                    
                    'nice', 'real', 'repulsive', 'scary', 'super', 'terrible', 
                    
                    'upset', 'wicked', 'wild', 'worried']

#This is a list of nouns that will be pulled in order to generate our unqiue, complex password. 
noun = ['lawyer', 'city', 'street', 'giraffe', 'bear', 'shoe', 'basketball', 

                    'faucet', 'lion', 'actor', 'ice', 'insurance', 'river', 
                    
                    'boy', 'island', 'battery', 'library', 'train', 'machine', 
                    
                    'vegetable', 'wall', 'yacht', 'orange', 'garden', 'ghost']

#These 4 variables set below are used to pull random collections of characters that we will use to concatenate into a full generated password.  
passwd_adj = random.choice(adjective)
passwd_noun = random.choice(noun)

passwd_number = random.randrange(0, 1000)
passwd_specialchar = random.choice(string.punctuation)

#This line of code will create our password variable that we will use later for authentication. This line concatenates the previous variables into a final password.
new_passwd = passwd_adj + passwd_noun + str(passwd_number) + passwd_specialchar

#This line will print us off our random generated password that is set for us. 
print("Your Generated Password is: %s" % new_passwd)

#This login function will allow for us to run an authentication test within the terminal and test whether our credentials will work or not.
def login():
    print("Welcome To The Login Page!")
    login_username = input("Please Enter Your Username:")
    login_password = input("Please Enter Your New Generated Password:")

    if login_username == username and login_password == new_passwd:
        print("Login Successful!")
    else:
        print("Login Not Authenticated.")

login()


# A QR code will be created here that will take you to a informative web page with tips for creating strong passwords. This can be found in the same folder the VS Code file is saved.
link = "https://edu.gcfglobal.org/en/techsavvy/password-tips/1/"
qrcode = pyqrcode.create(link)
qrcode.png("gcfglobal.png", scale=6)
