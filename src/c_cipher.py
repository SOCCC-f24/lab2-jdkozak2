import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    TODO: What is the objective? 
    The objective is to encrypt the email by changing the email message and 
    then being able to decrpyt the changed message. 
    Args:
        TODO: what arguments and data types are expected? (i.e., email)
        A string should be used for the encryption of the email function. 
    Returns:
        TODO: what variable and data types are being returned?  
        It should return a string with the encrypted email that has been changed.
    """
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    email = 'abc012'    # DEFINES THE CHARACTER STRING
    A = email[:3]       # SPLITS EMAIL INTO TWO SEPERATE PARTS AND CHECKS THE FIRST HALF
    B = email[3:]       # SPLITS EMAIL INTO TWO SEPERATE PARTS AND CHECKS THE SECOND HALF
    anum_flag = (A != 'abc') or (B != '012') # DETERMINES IF THE BOOLEAN VARIBALE IS TRUE OR FALSE

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email = 'abc012'        # DEFINES THE CHARACTER STRING
    email_lst = lst(email)  # CONVERTS THE STRING INTO A LIST
    print(email_lst)        # OUTPUTS THE RESULTS
    
    # TODO: complete line(s) below, convert EACH new element into a string
    email = 'abc012'                # DEFINES CHARACTER STRING
    for 0 in range(len(email)):
    new_ascii = ord(email[0]) + 3   # NOTE: here we extract and update element at 0 
    email[0] = chr(new_ascii)       # NOTE: here we convert our ASCII into string
    print(email)                    # OUTPUTS THE RESULTS
    
    # TODO: fix line below, convert list into a string
    email_lst = ['d', 'b', 'c', '0', '1', '2'] # DEFINES THE CHARACTER LIST
    email_str = ''.join(email_lst)             # CONVERTS THE LIST INTO A STRING
    print(email_str)                           # OUTPUTS THE RESULTS 
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
   """TODO: What is the objective? 
    The objective of this line is to reverse the encrytion process applied to email string. 
    Args:
        TODO: what arguments and data types are expected? (i.e., email)
        The decrypt function is going to use a single line argument with the name/data type being "email" which will be a string.  
    Returns:
        TODO: what variable and data types are being returned?  
        A string, bool, and int data types. 
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    email = 'def345'    # DEFINES THE CHARACTER STRING
    A = email[:3]       # SPLITS EMAIL INTO TWO SEPERATE PARTS AND CHECKS THE FIRST HALF
    B = email[3:]       # SPLITS EMAIL INTO TWO SEPERATE PARTS AND CHECKS THE SECOND HALF
    anum_flag = (A != 'def') or (B != '345') # DETERMIENS IF BOLENA VARIABLE IS TRUE OR FALSE.
    print(anum_flag)    # OUTPUTS THE RESULTS 

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO: apply the encrypt pseudocode but shift down 3
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = "aef345"
    return retVal
