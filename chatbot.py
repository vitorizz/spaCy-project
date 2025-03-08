import spacy

nlp = spacy.load("en_core_web_sm")

responses = {
    "greet": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "help": "I can answer your questions about Java programming concepts. Try asking about control structures, loops, OOP principles, exceptions, or arrays.",

    "if": "In Java, an `if` statement is used for decision-making. It executes a block of code if the condition is `true`.\n\n```java\nif (x > 0) {\n    System.out.println(\"Positive number\");\n}\n```",

    "else": "The `else` statement in Java provides an alternative path when the `if` condition is `false`.\n\n```java\nif (x > 0) {\n    System.out.println(\"Positive\");\n} else {\n    System.out.println(\"Not positive\");\n}\n```",

    "else if": "The `else if` statement allows checking multiple conditions in sequence.\n\n```java\nif (x > 0) {\n    System.out.println(\"Positive\");\n} else if (x == 0) {\n    System.out.println(\"Zero\");\n} else {\n    System.out.println(\"Negative\");\n}\n```",

    "for": "A `for` loop in Java is used for repeated execution based on a counter.\n\n```java\nfor (int i = 0; i < 5; i++) {\n    System.out.println(\"Iteration: \" + i);\n}\n```",

    "while": "A `while` loop executes a block of code **as long as** a condition remains `true`.\n\n```java\nint i = 0;\nwhile (i < 5) {\n    System.out.println(\"Iteration: \" + i);\n    i++;\n}\n```",

    "do": "A `do-while` loop executes the block **at least once**, then checks the condition.\n\n```java\ndo {\n    System.out.println(\"Executed at least once!\");\n} while (false);\n```",

    "switch": "A `switch` statement selects a block of code based on a variable’s value.\n\n```java\nint day = 3;\nswitch (day) {\n    case 1:\n        System.out.println(\"Monday\");\n        break;\n    case 2:\n        System.out.println(\"Tuesday\");\n        break;\n    default:\n        System.out.println(\"Another day\");\n}\n```",

    "case": "Each `case` in a `switch` statement represents a possible value of the switch variable.",

    "break": "The `break` statement **exits** a loop or `switch` statement immediately.",

    "continue": "The `continue` statement **skips** the current iteration of a loop and moves to the next one.",

    "method": "A **method** in Java is a reusable block of code that performs a specific task.\n\n```java\npublic int add(int a, int b) {\n    return a + b;\n}\n```",

    "constructor": "A **constructor** is a special method that initializes objects.\n\n```java\npublic class Car {\n    String model;\n    public Car(String model) {\n        this.model = model;\n    }\n}\n```",

    "class": "A **class** in Java defines a blueprint for creating objects.\n\n```java\npublic class Car {\n    String model;\n}\n```",

    "object": "An **object** is an instance of a class.\n\n```java\nCar myCar = new Car(\"Toyota\");\n```",

    "inheritance": "**Inheritance** allows a class to inherit methods and attributes from another class.\n\n```java\nclass Animal {\n    void makeSound() {\n        System.out.println(\"Animal makes a sound\");\n    }\n}\n\nclass Dog extends Animal {\n    void bark() {\n        System.out.println(\"Dog barks\");\n    }\n}\n```",

    "polymorphism": "**Polymorphism** allows a method to behave differently based on the object that calls it.\n\n```java\nclass Animal {\n    void makeSound() {\n        System.out.println(\"Animal sound\");\n    }\n}\n\nclass Dog extends Animal {\n    void makeSound() {\n        System.out.println(\"Dog barks\");\n    }\n}\n```",

    "encapsulation": "**Encapsulation** restricts direct access to fields and methods in a class.\n\n```java\nclass Person {\n    private String name;\n    public void setName(String name) {\n        this.name = name;\n    }\n}\n```",

    "abstraction": "**Abstraction** hides implementation details and exposes only essential features.\n\n```java\nabstract class Animal {\n    abstract void makeSound();\n}\n\nclass Dog extends Animal {\n    void makeSound() {\n        System.out.println(\"Dog barks\");\n    }\n}\n```",

    "interface": "An **interface** in Java defines a contract that classes must follow.\n\n```java\ninterface Animal {\n    void makeSound();\n}\n```",

    "exception": "An **exception** in Java is an event that disrupts normal program flow.",

    "try": "A **try** block in Java contains code that might throw an exception.\n\n```java\ntry {\n    int x = 5 / 0;\n} catch (Exception e) {\n    System.out.println(\"Error: \" + e.getMessage());\n}\n```",

    "catch": "A **catch** block handles exceptions thrown by a `try` block.",

    "finally": "A **finally** block always executes, regardless of whether an exception occurred or not.",

    "array": "An **array** is a fixed-size data structure that holds multiple values of the same type.\n\n```java\nint[] numbers = {1, 2, 3, 4};\n```",

    "string": "A **String** in Java represents a sequence of characters.\n\n```java\nString name = \"John\";\nSystem.out.println(name.length());\n```",

    "default": "I'm sorry, I didn't understand that. Could you rephrase?"
}


keywords_map = {
    "greet": ["hi", "hello", "hey", "greetings", "sup"],
    "bye": ["bye", "goodbye", "farewell", "see you", "exit", "quit", "stop", "end session"],
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
    user_input = user_input.lower()
    doc = nlp(user_input)

    # Prioritize multi-word matches first (like "else if")
    for key in sorted(keywords_map.keys(), key=lambda k: -len(k)):  # Sort keys by length (longest first)
        for word in keywords_map[key]:
            if word in user_input:
                return responses[key]

    # If no full phrase is found, check individual words
    for token in doc:
        token_lemma = token.lemma_
        for key, words in keywords_map.items():
            if token_lemma in words:
                return responses[key]

    return responses["default"]

def main():
    print("Chatbot: Hello! How can I help you today? Type 'bye', 'exit', or 'quit' to end the session.")
    while True:
        user_input = input("You: ").lower()
        
        # Check if user wants to exit
        if any(word in user_input for word in keywords_map["bye"]):
            print("Chatbot: Goodbye! Have a great day!")
            break  # Ends the chatbot session
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()