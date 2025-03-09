import spacy
import re
from collections import Counter

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
    
    "static": "The `static` keyword means that a member belongs to the class, not to any instance.\n\n```java\npublic class Example {\n    public static int count = 0;\n}\n```",
    "final": "The `final` keyword indicates that a variable's value cannot change, a method cannot be overridden, or a class cannot be extended.\n\n```java\nfinal int MAX = 100;\n```",
    "synchronized": "The `synchronized` keyword ensures that only one thread can access a method or block of code at a time.\n\n```java\npublic synchronized void increment() {\n    count++;\n}\n```",
    "volatile": "The `volatile` keyword indicates that a variable's value will be read from and written to main memory, ensuring visibility among threads.\n\n```java\nprivate volatile boolean active;\n```",
    
    "lambda": "Lambda expressions allow you to write anonymous functions in Java with a concise syntax.\n\n```java\nList<Integer> list = Arrays.asList(1, 2, 3, 4);\nlist.forEach(n -> System.out.println(n));\n```",
    "stream": "The Java Stream API provides a functional approach to processing collections.\n\n```java\nList<String> names = Arrays.asList(\"Alice\", \"Bob\", \"Charlie\");\nnames.stream()\n     .filter(name -> name.startsWith(\"A\"))\n     .forEach(System.out::println);\n```",
    "optional": "The `Optional` class is a container object which may or may not contain a non-null value, helping avoid `NullPointerException`.\n\n```java\nOptional<String> optionalName = Optional.ofNullable(name);\n```",
    "generic": "Generics allow classes and methods to operate on objects of various types while providing compile-time type safety.\n\n```java\npublic class Box<T> {\n    private T t;\n    public void set(T t) { this.t = t; }\n    public T get() { return t; }\n}\n```",
    "enum": "Enums define a fixed set of constants and can include methods and fields.\n\n```java\nenum Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }\n```",
    "package": "Packages group related classes, helping organize code and avoid naming conflicts.\n\n```java\npackage com.example.myapp;\n```",
    "import": "The `import` statement allows you to use classes and interfaces from other packages.\n\n```java\nimport java.util.List;\n```",
    "throw": "The `throw` keyword is used to explicitly throw an exception.\n\n```java\nthrow new IllegalArgumentException(\"Invalid argument\");\n```",
    "throws": "The `throws` keyword in a method signature indicates that the method may throw certain exceptions.\n\n```java\npublic void readFile() throws IOException {\n    // ...\n}\n```",
    "assert": "The `assert` keyword is used for debugging to test assumptions in code.\n\n```java\nassert x > 0 : \"x must be positive\";\n```",
    
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
    "string": ["string", "text", "characters"],
    
    "static": ["static"],
    "final": ["final"],
    "synchronized": ["synchronized", "sync"],
    "volatile": ["volatile"],
    
    "lambda": ["lambda", "anonymous function"],
    "stream": ["stream", "streams", "java stream"],
    "optional": ["optional", "option"],
    "generic": ["generic", "generics"],
    "enum": ["enum", "enumeration"],
    "package": ["package", "packages"],
    "import": ["import", "include"],
    "throw": ["throw", "raise"],
    "throws": ["throws"],
    "assert": ["assert", "assertion"]
}

def count_keywords(user_input):
    """Counts keyword occurrences using regex for phrases and lemmatized token matching."""
    counts = Counter()
    
    # Count occurrences using regex for full phrase matches
    for key, words in keywords_map.items():
        for word in words:
            # \b ensures whole-word matching
            if re.search(r'\b' + re.escape(word) + r'\b', user_input):
                counts[key] += 1

    # Count occurrences using spaCy token lemmatization
    doc = nlp(user_input)
    for token in doc:
        token_lemma = token.lemma_
        for key, words in keywords_map.items():
            if token_lemma in words:
                counts[key] += 1

    return counts

def earliest_occurrence(key, user_input):
    """Returns the earliest index where any keyword for a given key appears in user_input."""
    indices = []
    for word in keywords_map[key]:
        idx = user_input.find(word)
        if idx != -1:
            indices.append(idx)
    return min(indices) if indices else len(user_input)

def choose_best_keyword(user_input):
    """Selects the best matching keyword based on count and earliest occurrence."""
    counts = count_keywords(user_input)
    if not counts:
        return "default"
    # Sort candidates by highest count and then by earliest occurrence
    best_key = sorted(counts.items(), key=lambda item: (-item[1], earliest_occurrence(item[0], user_input)))[0][0]
    return best_key

def get_response(user_input):
    user_input = user_input.lower()
    best_key = choose_best_keyword(user_input)
    return responses.get(best_key, responses["default"])

def main():
    print("Chatbot: Hello! How can I help you today? Type 'bye', 'exit', or 'quit' to end the session.")
    while True:
        user_input = input("You: ").lower()
        
        # Check if user wants to exit (using whole-word matching)
        if any(re.search(r'\b' + re.escape(word) + r'\b', user_input) for word in keywords_map["bye"]):
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
