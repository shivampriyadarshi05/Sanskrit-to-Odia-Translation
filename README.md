# Sanskrit-to-Odia-Translation 

A command-line Python application that translates Sanskrit and Hindi words and sentences into Odia. The tool also performs basic grammatical analysis — identifying plurals, verbs, and normal words — and displays results word by word with their grammatical category.

# How It Works
The project is divided into four core modules:
1. Dictionary (dictionary)
A Python dictionary mapping Sanskrit/Hindi words (keys) to their Odia equivalents (values).
2. Parsing Module (parse_input)
Takes a sentence as input, strips punctuation characters (।, ,, ., !, ?) using regular expressions, and splits the cleaned text into individual words.
3. Grammar Handling (check_grammar)
Inspects the ending of each word to detect its grammatical form:

i)Words ending in एं or ओं → Plural (बहुवचन).
ii)Words ending in ति → Verb (क्रिया).
iii)All other words → Normal.

4. Translation Logic (translate)
For each word:

i)Applies grammar rules to determine base form and any suffix to append.
ii)Looks up the base word in the dictionary.
iii)Returns the Odia translation with appropriate grammatical modification.
iv)Marks unknown words as [unknown: word]


Here I use basic programing knowledge in python to develop the application.
