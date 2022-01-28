# Demonstrate how to customize logging output

import logging

extData = {'user': 'joem@example.com'}


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    # the last character is the type of var: s=string d=digit
    # %(asctime)s call with the datefmt in basicConfig
    # %(levelname)s is the level of the message of logging
    # %(funcName)s name of the function called
    # %(lineno)d number of line
    # %(name)s key name
    # %(message)s the string given in the log
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    # %m=month, %d=day, %Y=year.
    # %I=hour, %M=minutes, %S=seconds, %p=AM or PM
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        filemode="w",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    # with extra you can send a dictionary to fill missing keys
    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()


if __name__ == "__main__":
    main()
