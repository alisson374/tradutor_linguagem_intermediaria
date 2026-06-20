from parser import parser

source = """
var int zezinho;

 num = 0;
 while(cont < 10) {
    cont2 = 3.1415 * contador ^ 2;
    if (cont < 5) {
       num = num + cont2;
    }
    else {
       cont = 0;
    }
    cont = cont + 1;
 }
"""
result = parser.parse(source)
print(result)