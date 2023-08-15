#!/usr/bin/env python3
# line above says this is python3 file
#
# This file is from
#  https://github.com/byjosh/starter-python-file
# licensed under https://www.gnu.org/licenses/gpl-3.0.html
# technically if you want to build a big software project and distribute
# the code of the project without giving others right to reuse it
# do not start with this file as license imposes gives right of reuse
# but if you are coding anything big you will learn how to recreate this file from
# your general knowledge of how Python works and its documentation
# you will not need to copy this file at that point - you'll write your own



import logging

# if filename='example.log' was included before encoding='utf-8' on next line of code
# then the log would go to a file
# The logging.level has various levels - FATAL is for very serious stuff
# so set to a level so serious it will not show anything unless you use logging.fatal("the fatal message")
# instead of logging.FATAL below you could try logging.DEBUG or logging.INFO etc.
logging.basicConfig(encoding='utf-8', level=logging.FATAL)

#================================================
# put your code below this
# leave what is above this in place and you get
# the logging
#================================================
def hello():
    """Prints hello world"""
    print("Hello world")
    for i in "123":
        logging.debug('If we have set level to logging.DEBUG above we will see number {} logged - which is n \n \
                      and see all the messages for the less detailed levels of logging (info, warning, error etc.)'.format(i))
        for n in {"a": [1, 2], "b": [3, 4]}:
            logging.info('Info is slightly less detailed than debug \n \
            perhaps for showing progress like:- outer loop value is {} and n is {}'.format(i, n))

    logging.warning('A warning is what you should be warned about - so even less detailed level than info')
    logging.error('errors are signs something is really wrong - not just warning of potential issue - so again less detailed')

# add more function definitions or variables or data structures like lists and dictionaries
# below this line - add more space as needed


#=======================
# leave the next line alone so it can tell if this file run as a script from commandline
if __name__ == "__main__":
    # line above checks if this is being run as a script on the command line
    # rather than imported into another file or into the interpreter
    # if the interpreter in the same folder as the file
    # use cd in terminal to change to same folder and then run python3 or python3.exe
    # is the easiest way for beginner to allow
    # import name_of_this_file
    # to work
    #
    # run in the interpreter
    # import importlib # just once  then
    # imp.reload(name_of_this_file) # every time you change the file
    # and want changes available in  interpreter
    # FUNCTIONS BELOW THIS LINE ONLY RUN AS SCRIPT
    # pass statement below will allow you to comment out hello() line without giving an error
    pass

    hello()
    # TODO: to use this file

