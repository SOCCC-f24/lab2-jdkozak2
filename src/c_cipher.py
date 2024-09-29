import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

 # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1def encrypt(email="abc012"):

    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    A = email[:3]
    B = email[:3]
    anum_flag = A != 'abc' or B != '012' 

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
    email = "abc012"
    email_lst = list(email)
    print(email_lst)
        
    # TODO: complete line(s) below, convert EACH new element into a string
    for i in range(len(email_lst)):
    new_ascii = ord(email_lst[i]) + 3    # NOTE: here we extract and update element at 0 
    email_lst[i] = chr(new_ascii)        # NOTE: here we convert our ASCII into string

    print(email_lst)
        
    # TODO: fix line below, convert list into a string
   email_lst = ['d', 'b', 'c', '0', '1', '2'] 
    email_str = ''.join(email_lst)
    print(email_str)

   
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 
    The objective of this line is to reverse the encrytion process applied to email string. 
    Args:
        TODO: what arguments and data types are expected? (i.e., email)
        The decrypt function is going to use a single line argument with the name/data type being "email" which will be a string.  
    Returns:
        TODO: what varibale and data types are being returned?  
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
    first = 'def'
    second = '345'
    A = email[:3]
    B = email[:3]
    anum_flag = A != first or B != second 

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
