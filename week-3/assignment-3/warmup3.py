print(not True and False)         # False: not binds tighter than and, so (not True) = False; False and False is False
print(True or False and False)    # True: and runs before or, so False and False = False; True or False is True
print(not (5 > 3))                # False: 5 > 3 is True, and not True is False
print(10 == 10 and 4 != 4)        # False: 10 == 10 is True, but 4 != 4 is False, so True and False is False
print(not False or not True)      # True: not False = True, so True or anything is True
