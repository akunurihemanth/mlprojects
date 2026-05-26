import sys

# create a function to show how the message should look like inside the file with respect to custom exception

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #exception details which file which line we are facing the error
    file_name=exc_tb.tb_frame.f_code.co_filename #custom exception handling in python documentation 
    error_message="Error occured in python script name [{0}] line numebr [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

#created a custom exception class which is inheriting from the exception, 

class CustomException(Exception):

#Overriding the __init__ method    

    def __init__(self,error_message,error_detail:sys):
#initialize the init function using the error_message here and inherit the exception class
        super.__init__(error_message) 
#  created an error message variable which is getting populated from the function
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

#finally when we print it, we get the error message
    def _str_(self):
        return self.error_message
    