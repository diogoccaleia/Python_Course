name = "Diogo"

count = 1

def another():
    color = "orange"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
        print(name)

    greeting("Dave")
another()

