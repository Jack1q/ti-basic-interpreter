# # # # # # # # # # # # # #
# TI-Basic Interpreter    #
# Built by Jack Donofrio  #
# Very limited right now  #
# # # # # # # # # # # # # # 

# If it doesn't work at first, don't give up
# This will definitely be a long-term project

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# TI-basic Variable Types and Everything I know about them  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Numerics -> Include A-Z (Only uppercase) + Theta

# I'm pretty sure every numeric var defaults to 0 if it is not initialized.
# So I can just make a dict of them all starting at 0
# I also think 'i' (sqrt -1) can be stored as a numeric... that's gonna be interesting.

numeric_variables = {}
for x in range(65,91):
    numeric_variables[chr(x)] = 0
# and then add Theta
numeric_variables['ϴ'] = 0
# print(numeric_variables)


# List - Include L1 -> L6
# Custom lists created by using tiny L - '∟' maybe this?
# Constructing lists begins with '{'
# Example-> :{1,2,3,4→∟MyList or :{1,4,A,Z→L1
# dim(list) returns list length (i think)

# Right now, I think the best course of action will just be to set aside
# L1 to L6 and have the interpreter make a special case for recognizing them.
# Seems a bit annoying with all the special characters - like L1 is recognized as 1 char in TI-Basic
# Max size = 999

list_variables = {'L1':[],'L2':[],'L3':[],'L4':[],'L5':[],'L6':[]}

# Matrices -> Built in = [A] -> [J]
# Construct beginning with '['
# Ex: :[[1,2,3][4,5,6→[A]

matrix_variables = {}
for x in range(65,75):
    matrix_variables[f'[{chr(x)}]'] = []
# print(matrix_variables)


# Strings -> Default Str1 -> Str0
# Construct beginning with "
# Ex: "HELLO→Str1

string_variables = {}
for x in range(10):
    string_variables[f'Str{x}'] = ''

numeric_stack = []
string_stack = []
list_stack = []
matrix_stack = []

##################################################################
# Actual code starts here

variables = {}

def evaluate(line):
    # handle lists
    if line[0]=='{':
        variables[line[line.index('→')+1:].strip()] = eval('['+line[1:line.index('→')]+']', variables)
        # print(eval('['+line[1:line.index('→')]+']', variables))
    # handle strings
    elif line[0] == '"':
        variables[line[line.index('→')+1:].strip()] = str(line[1:line.index('→')])
    # handle matrices
    elif line[0]=='[' and '→' in line:
        new = ''
        mat = line[1:line.index('→')]
        for i in range(len(mat)):
            if i < len(mat) -1 and mat[i] == ']' and mat[i+1] == '[':
                new += '],'
            else:
                new += mat[i]
        new += ']'
        variables[line[line.index('→') + 1:].strip()] = eval('['+new+']')
    elif '→' in line:
        variables[line[line.index('→') + 1:].strip()] = eval(line[:line.index('→')], variables)
    elif 'Disp' in line:
        val = eval(line[line.index('Disp') + 4:],variables)
        print(val)
        # if type(val) == str:
        #     print(val)
        # else:
        #     print(''.join([str(x) for x in val]))
    elif 'Input' in line:
        if line.startswith('Input'):
            if '",' in line:
                variables[line[line.index('",') + 2:].strip()] = eval(input(line[line.index('"')+1:line.rindex('"')]),variables)
            else:
                variables[line[line.index(' ') + 1:].strip()] = eval(input('?'),variables)

def compiler(src:str):
    lines = src.split(':')
    for line in lines:
        evaluate(line)


# src = '''
# :Input "X1=",A
# :Input "Y1=",B
# :Input "X2=",C
# :Input "Y2=",D
# :Input "Z1=",E
# :Input "Z2=",F
# :Disp "DIST=",pow(pow(A-C,2) + pow(B-D,2) + pow(E-F,2), 0.5)
# '''
# src = '''

# :5→A
# :(2+2+A)*5→B
# :Disp A + B
# :Input C
# :Disp A + B + C
#'''


src='''
:"HELLO→A
:Disp A
'''
compiler(src)


# a = '[1,1,1][2,2,3][5,1,5]'
# new = ''
# for i in range(len(a)):
#     if i < len(a) -1 and a[i] == ']' and a[i+1] == '[':
#         new += '],'
#     else:
#         new += a[i]

# print(eval('['+new+']'))
