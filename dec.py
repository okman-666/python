def decor(func):
    def wrap():
        print ("======================")
        func()
        print ("======================")
    return wrap
@decor
def  print_text():
    print("HelloWorld!")
print_text()
