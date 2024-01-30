#Custom Exception
class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass

number = 10
while True:
    try: 
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Value is too small")
    except ValueTooLargeError:
        print("Value is too large")
    finally:
        print("Finally")