class myError(Exception):
    pass

# raise - the cust msg is mentioned
try:
    raise myError("Something went wrong")


except myError as e:
    print("Caught error:", e)



# except block 
