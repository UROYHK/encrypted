hwllo there! my name is advaith and This is a fun little Python project I built to encrypt and decrypt messages using symbols instead of letters. Think of it like your own secret language we can use to talk with frinds .my main reson way fun so i hope you have some fun with this code.


>What It Does
This program has 2 functions:
-Encrypt any message by converting each letter into a special symbol.
- Decryptit back to the original message using the same symbol mapping.

>How It Works
There’s a symbol table in the code that maps each character (a–z, space, and `?`) to a unique set of symbols.
you can customize this values to your liking .
 note : make sure to not have duplacate values or captial values on the encription symbols side

symbol table structure :
symbol_map = {
    "a": ".",      "b": ":",      "c": ":.",     "d": "::",
    "e": "|",      "f": "|.",     "g": "|:",     "h": "|:.",
    "i": "|::",    "j": "||",     "k": "||.",    "l": "||:",
    "m": "||:.",   "n": "||::",   "o": "|||",    "p": "|||.",
    "q": "|||:",   "r": "|||:.",  "s": "|||::",  "t": "||||",
    "u": "||||.",  "v": "||||:",  "w": "||||:.", "x": "||||::",
    "y": "|||||",  "z": "|||||.", " ": "~",      "?": "qushion mark"
}

>Features
   Converts your text to encrypted symbols.
   Can also convert encrypted messages back to normal text.
   Handles unknown characters with a ? so you know something’s off.
   Keeps running until you type bye to exit.

>How to Run It
Make sure Python 3 is installed.
Run the script in your terminal or any Python environment:
python encryptor.py
Follow the prompts to encrypt or decrypt messages.
Type bye when you’re done.

>Behind the Scenes
There are two main functions:

encripter(text)
→ Converts normal text into symbols, adds spaces between them.

decripter(text)
→ Takes a string of space-separated symbols and converts them back into text.

A reversed map is used during decryption:
reversed_map = {v: k for k, v in symbol_map.items()}
This lets us look up the symbol and get the original letter back.
You don’t need to install anything this code only uses built-in Python functions.
