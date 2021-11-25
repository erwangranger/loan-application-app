
def loan_approval(nm, LoanAmount, CreditHistory):
    #print("Hello from a function")
    # for key, value in kwargs.items():
    #     print("{0} = {1}".format(key, value))

    if CreditHistory == '1' :
        print ("approved")
        return 1
    else:
        if 'erwan' in nm:
            print ("exception for Erwan")
            return 1
        else:
            print ("denied")
            return 0



# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))

# greet_me(name="yasoob" , lname="granger")

# test1 = loan_approval(nm = "jim" , \
#                             LoanAmount = 10000, \
#                             CreditHistory = 0)
# test2 = loan_approval(nm = "erwan" , \
#                             LoanAmount = 10000, \
#                             CreditHistory = 0)
# test3 = loan_approval(nm = "tom" , \
#                             LoanAmount = 10000, \
#                             CreditHistory = 1)
# print (test1)
# print (test2)
# print (test3)

