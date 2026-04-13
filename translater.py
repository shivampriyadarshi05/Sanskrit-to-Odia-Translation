import re

# TASK 1: DICTIONARY

dictionary = {

    # Greetings
    "नमः":      "ନମସ୍କାର",
    "नमस्ते":   "ନମସ୍କାର",
    "धन्यवाद":  "ଧନ୍ୟବାଦ",
    "शुभ":      "ଶୁଭ",
    "प्रणाम":   "ପ୍ରଣାମ",
    "हाँ":      "ହଁ",
    "नहीं":     "ନା",

    # Family
    "माता":     "ମାତା",
    "पिता":     "ପିତା",
    "गुरु":     "ଗୁରୁ",
    "भाई":      "ଭାଇ",
    "बहन":      "ଭଉଣୀ",
    "पुत्र":    "ପୁତ୍ର",
    "पुत्री":   "ପୁତ୍ରୀ",
    "मित्र":    "ବନ୍ଧୁ",
    "राजा":     "ରାଜା",

    # Nature
    "जल":       "ଜଳ",
    "अग्नि":    "ଅଗ୍ନି",
    "वायु":     "ବାୟୁ",
    "पृथ्वी":   "ପୃଥ୍ବୀ",
    "आकाश":     "ଆକାଶ",
    "सूर्य":    "ସୂର୍ଯ୍ୟ",
    "चन्द्र":   "ଚନ୍ଦ୍ର",
    "नदी":      "ନଦୀ",
    "वन":       "ବଣ",
    "फूल":      "ଫୁଲ",
    "फल":       "ଫଳ",

    # Body
    "हाथ":      "ହାତ",
    "नेत्र":    "ନୟନ",
    "मुख":      "ମୁଖ",
    "हृदय":     "ହୃଦୟ",

    # Verbs
    "जाति":     "ଯାଏ",
    "आगच्छति":  "ଆସେ",
    "खादति":    "ଖାଏ",
    "पिबति":    "ପିଏ",
    "पठति":     "ପଢ଼େ",
    "लिखति":    "ଲେଖେ",
    "वदति":     "କୁହେ",
    "करोति":    "କରେ",

    # Adjectives
    "सुन्दर":   "ସୁନ୍ଦର",
    "महान":     "ମହାନ",
    "प्रिय":    "ପ୍ରିୟ",
    "नवीन":     "ନୂତନ",

    # Numbers
    "एक":       "ଏକ",
    "द्वि":     "ଦ୍ୱି",
    "त्रि":     "ତ୍ରି",
    "पञ्च":     "ପଞ୍ଚ",

    # Spiritual
    "ईश्वर":    "ଈଶ୍ୱର",
    "भगवान":    "ଭଗବାନ",
    "धर्म":     "ଧର୍ମ",
    "कर्म":     "କର୍ମ",
    "आत्मा":    "ଆତ୍ମା",
    "शान्ति":   "ଶାନ୍ତି",
    "सत्य":     "ସତ୍ୟ",
    "ज्ञान":    "ଜ୍ଞାନ",
    "भक्ति":    "ଭକ୍ତି",
    "देव":      "ଦେବ",
    "देवी":     "ଦେବୀ",
}

#  TASK 2: PARSING MODULE

def parse_input(sentence):

    sentence = re.sub(r'[।,\.!?]', ' ', sentence)
    words = re.findall(r'\S+', sentence)
    return words


# TASK 4: GRAMMAR HANDLING

def check_grammar(word):
    if word.endswith("एं"):
        return word[:-2], "Plural (बहुवचन)", " ମାନେ"
    elif word.endswith("ओं"):
        return word[:-2], "Plural (बहुवचन)", " ମାନେ"

    elif word.endswith("ति"):
        return word, "Verb (क्रिया)", ""

    elif word.endswith("तु"):
        return word, "Command Verb", ""

    else:
        return word, "Normal", ""



# TASK 3: TRANSLATION LOGIC
# Translates each word using the dictionary

def translate(words):
    results = []

    for word in words:

        # Step 1: Check if word is plural (ends with "एं" or "ओं")
        if word.endswith("एं") or word.endswith("ओं"):
            base_word = word[:-2]        # remove last 2 characters
            grammar = "Plural"
            extra = " ମାନେ"             # Odia plural suffix

        # Step 2: Check if word is a verb (ends with "ति")
        elif word.endswith("ति"):
            base_word = word             # keep word as it is
            grammar = "Verb"
            extra = ""

        # Step 3: Normal word - no grammar rule
        else:
            base_word = word             # keep word as it is
            grammar = "Normal"
            extra = ""

        # Step 4: Search base_word in dictionary
        if base_word in dictionary:
            odia = dictionary[base_word] + extra
        else:
            odia = "[unknown: " + word + "]"
            grammar = "Not Found"

        # Step 5: Save the result
        results.append((word, grammar, odia))

    return results


# user interface command-line program

print("=" * 55)
print("   Sanskrit/Hindi to Odia Translator")
print("=" * 55)
print("  Commands:")
print("  - Type a word or sentence in Hindi/Sanskrit")
print("  - Type 'dict' to see all dictionary words")
print("  - Type 'exit' to quit")
print("=" * 55)

while True:
    print()
    user_input = input("Enter text: ").strip()

    # Exit
    if user_input == "exit":
        print("Thank you! Goodbye.")
        break

    # Show dictionary
    elif user_input == "dict":
        print("-" * 40)
        print(f"{'Hindi/Sanskrit':<20} {'Odia'}")
        print("-" * 40)
        for hindi, odia in dictionary.items():
            print(f"{hindi:<20} {odia}")
        print("-" * 40)

    # Empty input
    elif user_input == "":
        print("Please enter something!")

    # Translate
    else:
        # Step 1: Parse into words
        words = parse_input(user_input)

        # Step 2: Translate
        results = translate(words)

        # Step 3: Full Odia sentence
        full_odia = " ".join([odia for (_, _, odia) in results])

        # Step 4: Show output
        print()
        print("Input  :", user_input)
        print("Output :", full_odia)
        print()

        # Step 5: Word by word table
        print("-" * 55)
        print(f"{'Sanskrit Word':<20} {'Grammar':<15} {'Odia Meaning'}")
        print("-" * 55)
        for (word, grammar, odia) in results:
            print(f"{word:<20} {grammar:<15} {odia}")
        print("-" * 55)

    # Ask to continue
    print()
    again = input("Translate another? (yes/no): ").strip().lower()
    if again == "no":
        print("Thank you! Goodbye.")
        break