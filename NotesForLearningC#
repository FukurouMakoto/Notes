Variables are done similarly to C++
    Strings = string variableName
    Integers = int variableName
    Characters = char variableName (Can only be used for single alphabet character)
    Booleans = bool variableName
    C# has three different number types for handling integers, ranging from most accurate to least accurate. For most use cases Double should be good enough but if you are working with something like money than you would want to use Decimals. 
    float, double, decimal
    Floats = float variableName
    Double = double variableName
    Decimals = decimal variableName

String methods
    .Length
        returns length of string, similarly to lens()
    .ToUpper
        C# equivalent of .upper()
    .ToLower
        C# equivalent of .lower()
    .Contains()
        searches string for parameter substring. Return bool.
    string[0]
        strings in C# accepts index locations just like in Python.
    .IndexOf
        searches string for parameter substring and if true returns its index value.
    .Substring
        accepts a index value, and returns the substring located at that value.

Integers
    num++, num--
        Increments numbers just like in C++
    +, -, *, /, %
        All work in exactly the same way and syntax as Python.
    Math
        Math Class provides constants and string methods for trigonometric, logarithmic, and other common mathematical functions. 
    Math.abs()
        returns the absolute value of the number passed thru.
    Math.Pow(num1, num2)
        returns the value of num1 taken to the power of num2.
    Math.Sqrt()
        returns the square root of the number passed thru.
    Math.Max()
        returns whichever number passed thru is the biggest. 
    Math.Min()
        returns whichever number passed thru is the smallest.
    Math.Round()
        returns the rounded version of number passed thru.
    
Console.ReadLine()
    the C# equivalent of input(). Keep in mind that even though it works very similarly to Python you will still need to declare the variable type before hand. 
    Ex:
        name = input("Please enter name")
        string name = Console.ReadLine()
    Also keep in mind that the Line part has it write to a new line. If you want to have the user enter their name on the same line as the prompt, you would just use Console.Write(). 
    Also keep in mind that ReadLine() does not take parameters. If you would like to have a message before where the user types, you will need to include a Console.WriteLine before it.


Convert
    The convert function allows to convert variables to different types; they are similar to str() or int().
    With this you can use Convert to convert a variable into various types with its methods like Convert.ToInt32 for numbers or Convert.ToString for strings.


Arrays
    Arrays work similarly to how they do in C++. 
    First, declare the variable types that will be in the array. Next, include [], which will tell C# that the object is an array. Then give the array its name, and next we use curly brackets to hold its values in. 
    Ex:
        int[] luckyNumbers = {}
    You can access the items in the array in the same way you would a list in Python.
    Ex:
        Console.WriteLine(luckyNumbers[1])
    You can also update values in a list in the same way you would in Python:
    Ex:
        luckyNumbers[1] = 900;
    You can also create an empty array, but keep in mind that when you do so, you will need to tell C# what is the upper limit of items that array can hold. 
        string[] friends = new string[5];
    It needs to be noted however that the items in an array must all be of the same type. You cannot have integers mixed in with strings like you can in Python.

Methods
    For some reason in C# Functions are usually only reffered to as Methods. Haven't found out exactly why. 
    To create a function you must first define it outside of the main function. Then you type the keyword static, followed by the return value of the function such as int, string or void. Next you type the name of the function (C# conventions is CapsCase), followed by parenthesis to place in your arguments, and curly braces to hold the code for that function. 
    You can then call the function in the exact same way that you would call a function in Python.

Return Statements
    return is used the exact same way as in Python.
     
    void
        returns no value
    int 
        returns a interger
    string
        returns a string
    double
        returns a double
    array of doubles    
        can do this with double[]
    
    Pretty much you can return any kind of object you can think of.

Comparison Operators
    && = And
    || = Or 
    == = Is equal to
    isTall = True statement (like in Python)
    !isTall = False statement
    >= <= < > 
        All work exactly the same as in Python.
    

If Statements
    If statements work very similarly to how they do in JS and C++ in terms of syntax.
    if(condition)
    {
        do this;
    } else if(condition)
    {

    } else 
    {
        do this;
    }
    One interesting thing to note about if statements. You absolutely MUST program a else statement in order for the program to compile correctly. If you include if and else if statements without one, the program will return a "Not all code paths return a value" error message. This is a huge difference from Python.

Switch Statements
    C# also has switch statements just like C++ and JS.

    switch(value)
    {
        case 0:
            code;
            break;
        case 1:
            code;
            break;
        case 2:
            code;
            break;
    }

    You can also include code that handles situations that don't match your cases. 

    default:
        code;
        break;

While Loops
    They work somewhat similarly to JS.

    while (condition) 
    {
        code;
    }
    C# also has something special called do while loops, in which you can specify code to be run even if the condition evaluates to false. 
    Ex.
    int index = 6;
    do
    {
        Console.WriteLine(index);
        index++;
    } while (index <= 5);

    In this case, even though normally this while loop would never execute, because we have a do statement there, it executes at least once. They are mostly used for fringe cases.

For Loops
    For loops work the same way as in C++
    for(int i = 1; i <= 5; i++)
    {
        Console.WriteLine(index);
    }
    First argument = initialize a variable that controls the loop.
    Second argument = condition to break out of for loop.
    Third argument = Last part of the code to be done before the condition is checked. 
    In this example, this code will print out the value of index, which starts at 1, increment i as shown in the third arguement, and then check the condition of the second argument. 
    Unfortunately it's the same confusing stuff that we have in c++.

    int[] luckyNumbers = {bunch of random numbers}
    for (int i = 0, i < luckyNumbers.Length(), i++){
        Console.WriteLine(luckyNumbers[i])
    }
    The above code can be used to print out each item in the list luckyNumbers. You will probably need to play around with for loops in order to understand them.

2D Arrays
    2D Arrays are basically the same as a list of lists in Python. They are created similarly to regular arrays

    int[,,,] numberGrid = {
        {1,2},
        {3,4},
        {5,6},
    }
    Note that the comma in our brackets denote that this list will contain lists; the more arrays you want in your array, the more commas you put, int[,,,] for example. 
    In order to call items in your array, you do them similarly to Python except you do not use multiple brackets, but instead multiple commas.
    numberGrid[2,1] will return 6 in this case. 

Exception Handling
    Exception Handling works similarly to Python just with some different vernacular; instead Try/Except/Finally, it's Try/Catch/Finally.
    try
    {
        risky code
    }
    catch()
    {
        How to handle error
    }
    finally
    {

    }
    In catch you can also pass in a parameter to display the exception, and then use the variable in your catch statement. For example if you wanted to print the kind of exception thrown:
    catch(Exception e)
    {
        Console.WriteLine(e.Message);
    }
    You can also pass in specific Exceptions you want to catch:
    catch(DivideByZeroException e)
    {
        Console.WriteLine(e.Message);
    }

    Classes & Objects
        Convention dictates that Classes should be named in Uppercase.
        When creating a program you create it in a seperate file much like you would in Python. 

        namespace ProjectName
        {
            class Book
            {
                public string title; #These are your class attributes.
                public string author;
                public int pages;
            }
        }

    To create a new Object 
        Book book1 = new Book();
        book1.title = "Harry Potter";
        book1.author = "JK Rowling";
        book1.pages = 400; 
    
    Constructor Methods
    Constructor Methods are basically what their name implies; they are methods we can use with our classes when constructing them. This method will be called everytime that we create a new instance of our class. 
    Syntax:
    class Book
            {
                public string title; #These are your class attributes.
                public string author;
                public int pages;
            }

            public Book()
            {
                 
            }
    You can also pass parameters into your constructor in the same way you would say in Python (self.name, self.date for example)

            public Book(string title, string author, int pages)
            {
                title = title;
                author = author;
                pages = pages;
            }
    
    Object Methods  
        Object Methods work similarly to Python, except there is no need to reference self as a argument. 
        public bool HasHonors()
        {
            if(gpa >= 3.5)
            {
                return true;
            }
            return false;
        }
        These methods are then called in the same dot notation that Python uses. 

        Console.WriteLine(student1.HasHonors()); 

    Getters & Setters 
        C# also features Getters & Setters just like C++. Getters & Setters are a security feature primarily, designed for objects to make sure that the information entered for them are correct. They are methods that ensure proper input.
        Lets say for example that we are writing a movie application and are creating a movie object. We give it a string value for title, and a string value for director. Now we also want to put the rating, but the problem with making it a string is that if we do that, anyone can type literally anything they want and it will work, whereas we know there's only handful of actual ratings. how can we make sure that the rating entered is a viable rating?
        First we would need to make the rating attribute private. This means that unlike the rest of the values which are public and can be modified anywhere, only code within the Class itself can modify it. 

        class Movie 
        {
            public string Title;
            public string Director;
            private string Rating;
        }

        Next we would need to create a Getter and a Setter, which will allow outside code to both get the information about the property and set the information as well. 
        Note that per convention, you should name the method after the property it is modifying, but with a uppercase instead. 
        
        public string Rating
        {
            get { return rating; } #allows you to get the property
            set #allows you to set the property 
            {
                if(value == "G" ||value == "PG" ||value == "PG-13" ||value == "R")
                {
                    rating = value;
                }
                else {
                    rating = "NR";
                }
            }
        }

        Note that it is not necessary for you to always have getters and setters in your classes; they are merely there to make your program more secure. That being said you might have to look into general coding convention and see if it’s considered good coding practice like isinstance in Python. 

Static Class Attributes
    A static class attribute, much like the name implies is a attribute that all instances of that class share, and that they all have in common. 
    They are created in much the same way as a regular class attribute
        Class Song
        {
            public string title;
            public string artist;
            public int duration;
            public static int songCount = 0;
        }
    Note that you can initialize it with a default value. In this case, every Song object will be created initially with a songCount variable equal to 0.
    The main thing to remember when it comes to static class attributes is that they return information about the class itself, not the individual objects of that class type. 

Static Methods & Classes
    A static methods is a method that is attached to the class itself rather than any instance of a class. This means that you can use that method without ever actually creating an instance of the class. 
    Note that this is different from other methods in that they are neither tied to a specific instance of that class nor just a free flowing method. 
    An example of this is the Sqrt() function in the Math class. This method, while being part of the Math class, does not actually need a Math object in order to be used. This is an example of a Static Method. 
    Static methods do not require any kind of special syntax to create; simply create the class, and define the method within that class. This looks essentially like just a module in python with a class of nothing but methods.
    A static class is a class that does not produce instances of it; you cannot create an object that is an instance of that class. While there are certainly many cases where you will want to create a class from which you can create instances, there are many times where you will not want to do so. 
    To create a static class, simply label it as such. 
    Non-static class:
        class Program{}
    Static class:
        static class Program{}

Inheritance
    Syntax for inheritance
    class <superclass> : <subclass>{}
    class <childclass> : <parentclass>{}
    class ItalianChef : Chef{}
    
    You can also create subclass-specific function by simply defining the function within the scope of the subclass.
    Note that if you would like to have a method defined in the parent class that can be overwritten by a child class, you must label it with the virtual keyword in the parent class, and the override keyword in the child class
    Public virtual <returntype> <functionname>(){}
    public virtual void MakeSpecialDish(){}
    public override void MakeSpecialDish(){}
REMEMBER
    virtual in the parent class
    override in the child class
