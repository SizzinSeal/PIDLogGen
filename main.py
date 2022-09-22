# this program generates a logging file function
# I would just write it myself, but writing a
# function this large is going to take hours to
# write and debug due to simple mistakes.

# Does a more elegant solution exist? Not that
# I know of

# At least this way, new aspects to the logging file can
# be added relatively easily by anyone

########################################################
########################################################
########################################################

# list of variables, just add more to generate
vars = [
    'kA', 'kF', 'kJ', 'kP', 'kI', 'kD', 'kB', 'kG', 'firstRun', 'log',
    'logSpeed', 'target', 'input', 'error', 'totalError', 'derivative',
    'prevError', 'prevDerivative', 'targetAccel', 'output'
]

firstRun = True
## output line
output = ''
tab = '    '

# first if statement
output += tab + 'if (input.substr(0, name.length()) == name + ".") {\n'
output += tab + tab + 'input.erase(0, name.length());\n'

## main loop
for x in vars:
    if firstRun:
        output += tab + tab + 'if (input.substr(0, ' + str(
            len(x)) + ') == "' + x + '") {\n'
        firstRun = False
    else:
        output += tab + tab + '} else if (input.substr(0, ' + str(
            len(x)) + ') == "' + x + '") {\n'
    output += tab + tab + tab + 'input.erase(0, ' + str(len(x)) + ');\n'
    output += tab + tab + tab + 'if (input == "") {\n'
    output += tab + tab + tab + tab + 'mainMutex.take(TIMEOUT_MAX);\n'
    output += tab + tab + tab + tab + 'std::cout << "' + x + ':" << ' + x + ' << std::endl;\n'
    output += tab + tab + tab + tab + 'mainMutex.give();\n'
    output += tab + tab + tab + '} else {\n'
    output += tab + tab + tab + tab + 'if (input.find_first_not_of("0123456789.") == std::string::npos) {\n'
    output += tab + tab + tab + tab + tab + 'mainMutex.take(TIMEOUT_MAX);\n'
    output += tab + tab + tab + tab + tab + x + ' = std::stof(input);\n'
    output += tab + tab + tab + tab + tab + 'std::cout << "' + x + ' set to "' + ' << ' + x + ' <<' + ' std::endl;\n'
    output += tab + tab + tab + tab + tab + 'mainMutex.give();\n'
    output += tab + tab + tab + tab + '} else {\n'
    output += tab + tab + tab + tab + tab + 'std::cout << "invalid input" << std::endl;\n'
    output += tab + tab + tab + tab + '}\n'
    output += tab + tab + tab + '}\n'
output += tab + tab + '}\n'
output += tab + '}\n'

print(output)
