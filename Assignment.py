import re

#small Dfa

def is_identifier(token):#Starts with a letter or underscore, followed by letters, digits, or underscores
    return re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", token) is not None

def is_integer(token): #Whole number only (e.g., 10)
    return re.fullmatch(r"\d+", token) is not None

def is_float(token):#Decimal numbers (e.g., 10.5)
    return re.fullmatch(r"\d+\.\d+", token) is not None

def is_char(token):#Single character enclosed in single quotes
    return re.fullmatch(r"'(?:\\.|[^\\'])'", token) is not None

def is_string(token):#Sequence of characters enclosed in double quotes
    return re.fullmatch(r'"(?:\\.|[^"\\])*"', token) is not None

def is_operator(token):#String enclosed in double quotes
    return token in ['+', '-', '*', '/']

#Helper function
def is_operand(token): #Operand can be identifier, number, char, or string
    return (
        is_identifier(token) or
        is_integer(token) or
        is_float(token) or
        is_char(token) or
        is_string(token)
    )

def operand_type(token):#Type of operand
    if is_string(token):
        return 'string'
    if is_char(token):
        return 'char'
    if is_float(token) or is_integer(token):
        return 'number'
    if is_identifier(token):
        return 'identifier'
    return 'unknown'

#Big Dfa

def is_valid_assignment(statement, strict_mode=False):
    statement = statement.strip()
    if not statement.endswith(";"):
        return False
    stmt = statement[:-1]  

  #Tokenizer
    token_pattern = re.compile(
        r"'(?:\\.|[^\\'])'|\"(?:\\.|[^\"\\])*\"|\d+\.\d+|\d+|[A-Za-z_][A-Za-z0-9_]*|[+\-*/=]"
    )
    tokens = []
    pos = 0
    length = len(stmt)

    while pos < length:
        if stmt[pos].isspace():
            pos += 1
            continue
        m = token_pattern.match(stmt, pos)
        if not m:
            return False  
        tokens.append(m.group())
        pos = m.end()

    if len(tokens) < 3:
        return False
    if not is_identifier(tokens[0]) or tokens[1] != '=':
        return False

    rhs = tokens[2:]
    expecting_operand = True
    types_present = set()

    for token in rhs:
        if expecting_operand:
            if not is_operand(token):
                return False
            t = operand_type(token)
            if t != 'identifier' and t != 'unknown':
                types_present.add(t)
            expecting_operand = False
        else:
            if not is_operator(token):
                return False
            expecting_operand = True

    if expecting_operand:
        return False

    #reject mixing of strings/chars with numbers
    if strict_mode:
        has_number = 'number' in types_present
        has_string = 'string' in types_present
        has_char = 'char' in types_present

        if has_number:
            if has_string or has_char:
                return False

    return True


tests = [
    # Valid - Simple Assignment
    "num1 = num2;",
    "num1 = 10;",
    "num1 = 10.50;",
    "myChar = 'a';",
    #Invalid - Simple Assignment
    "1num = num2;",
    "num1 = 10",                 
    "num1 = 10a;",               
    "num1 = 10.50.50;",         
    "myChar = \"a\"",
    #Valid - Expanded Assignment
    "num1 = 10.50 + num2;",
    "num2 = 10.50 + num1 * 10 / 18.5;", 
    "num3 = 10.50 + num1 * 10 / 18.5;",
    #Invalid - Expanded Assignment
    "num1 = + 10.50 + num2;", 
    "num2 = 10.50 + num1 * 10 /;", 
    "num3 = 10.50 + num1 * + 10 / 18.5;",
    #Test cases
    "str1 = \"hello\";",
    "x = y + 5;",
    "result = num1 - num2 + 100;",
    "total = price * quantity / 2;",
    "average = sum / count;",
    "name = \"Ivann\";",
    "letter = 'z';",
    "num = 10.5 + 2.5 - 3;",
    "finalScore = score1 + score2 * 0.5;",
    "text = \"hello\" + \"world\";",
    "value = 10..5;",            
    "char = 'ab';",              
    "str = 'hello;",             
    "total = + + 10;",           
    "num = 10 +;",               
    "result = price * / quantity;",  
    "val = num1 + num2 * num3 - num4;", 
    "ans = 3.5 + 4.2 * 2.1 - 1;", 
    "data = value + input / 3.0;", 
    "grade = score + 5;", 
    "bonus = salary + 1000.50;", 
    "discount = price - 20.75;", 
    "speed = distance / time;", 
    "area = length * width;",
    #Invalid cases 
    "num1 = 10 + ;", 
    "num1 = *;", 
    "num1 = * num2;", 
    "num1 = 10 / * num2;", 
    "num1 = 10 * num2/;", 
    "num1 = 10 + num2/;", 
    "num1 = 10 +/ num2;", 
    "num1 = + + 10;", 
    "num1 = - 10;", 
    "num1 = 10.50.50 + num2;", 
    "num1 = num2 + 10.5.5;", 
    "x = -10 + 5;", 
    "y = +20.5 - 3;"
]


for case in tests:
    result = is_valid_assignment(case)
    if result:
        print(f"{case:<40} -> Valid")
    else:
        print(f"{case:<40} -> Invalid")

for case in tests:
    result = is_valid_assignment(case, strict_mode=True)
    if result:
        print(f"{case:<40} -> Valid")
    else:
        print(f"{case:<40} -> Invalid")