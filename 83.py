
class MyOwnError():
    listik = []

    def error():
        a = input()
        while a != "stop":
            try:
                MyOwnError.listik.append(int(a))
                MyOwnError.error()
            except(ValueError):
                print("err")
                break
        print(MyOwnError.listik)

MyOwnError.error()
