import sys

randomlist = ['a', 0.2]

for entry in randomlist:
    try:
        print("The entry is: ", entry)
        r = 1 / int(entry)
        break
    except:
        print("Oops", sys.exc_info()[0], "occured")
        print("next entry")
    # except Exception as e:
    #     print("Oops", e.__class__, "occured")
    # except(ValueError, ZeroDivisionError):
    #     print("An error occured")
