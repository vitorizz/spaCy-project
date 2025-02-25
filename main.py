import spacy

nlp = spacy.load("en_core_web_sm")

responses = {
    "greet": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "help": "I can answer your questions about Java programming concepts.",
    "if": "In Java, an if statement checks a condition and executes a block of code if the condition is true.",
    "else": "In Java, the else block executes if the if condition is false.",
    "else if": "In Java, else if allows you to check multiple conditions in sequence.",
    "for": "A for loop in Java is used for iterating over a range of values.",
    "while": "A while loop in Java repeatedly executes a block of code as long as a condition remains true.",
    "do": "A do-while loop in Java executes the block once before checking its condition.",
    "switch": "A switch statement in Java selects a block of code based on the value of an expression.",
    "case": "Case blocks in a switch statement define specific conditions to match.",
    "break": "The break statement in Java exits a loop or switch statement.",
    "continue": "The continue statement in Java skips the current iteration of a loop.",
    "method": "In Java, a method is a block of code that performs a specific task and can return a value.",
    "constructor": "A constructor in Java is used to initialize objects of a class.",
    "class": "A class in Java is a blueprint from which individual objects are created.",
    "object": "An object is an instance of a class in Java.",
    "inheritance": "Inheritance in Java allows one class to inherit fields and methods from another class.",
    "polymorphism": "Polymorphism in Java allows methods to behave differently based on the calling object.",
    "encapsulation": "Encapsulation in Java bundles data with methods that operate on that data.",
    "abstraction": "Abstraction in Java hides complex implementation details while exposing only the necessary features.",
    "interface": "An interface in Java can contain abstract methods and constants.",
    "exception": "An exception in Java is an event that disrupts the normal flow of a program.",
    "try": "A try block in Java is used to wrap code that might throw an exception.",
    "catch": "A catch block in Java handles the exception thrown by a try block.",
    "finally": "A finally block in Java executes after try and catch blocks.",
    "array": "An array in Java is a container that holds a fixed number of values.",
    "string": "A String in Java represents a sequence of characters.",
    "default": "I'm sorry, I didn't understand that. Could you rephrase?"
}

# Map response keys to lists of keywords
keywords_map = {
    "greet": ["hi", "hello", "hey", "greetings", "sup"],
    "bye": ["bye", "goodbye", "farewell", "see you"],
    "help": ["help", "info", "assist", "support"],
    "if": ["if"],
    "else": ["else"],
    "else if": ["else if", "elif"],
    "for": ["for"],
    "while": ["while"],
    "do": ["do"],
    "switch": ["switch"],
    "case": ["case"],
    "break": ["break"],
    "continue": ["continue"],
    "method": ["method", "function", "procedure"],
    "constructor": ["constructor"],
    "class": ["class", "blueprint"],
    "object": ["object", "instance"],
    "inheritance": ["inheritance", "extend"],
    "polymorphism": ["polymorphism", "overload", "override"],
    "encapsulation": ["encapsulation", "data hiding"],
    "abstraction": ["abstraction", "hide details"],
    "interface": ["interface"],
    "exception": ["exception", "error", "issue"],
    "try": ["try"],
    "catch": ["catch"],
    "finally": ["finally"],
    "array": ["array", "list"],
    "string": ["string", "text", "characters"]
}

def get_response(user_input):
    doc = nlp(user_input.lower())
    for token in doc:
        token_lemma = token.lemma_
        for key, words in keywords_map.items():
            if token_lemma in words:
                return responses[key]
    return responses["default"]

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot:", responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()