books = {}
borrowers = {}
checkouts = []

nextline = input().strip()
while nextline.find("Books") < 0:
    nextline = input().strip()

nextline = input().strip()
while nextline.find("Borrowers"):
    (accessionNumber, title) = nextline.split("~")
    books[accessionNumber] = title
    nextline = input().strip()

nextline = input().strip()
while nextline.find("Checkouts") < 0:
    (username, fullname) = nextline.split("~")
    borrowers[username] = fullname
    nextline = input().strip()

nextline = input().strip()
while nextline.find("EndOfInput") < 0:
    (username, accessionNumber, dueDate) = nextline.split("~")
    checkoutEntry = dueDate+"~"+borrowers[username]+"~"+accessionNumber+"~"+books[accessionNumber]
    checkouts.append(checkoutEntry)
    nextline = input().strip()

for i in sorted(checkouts):
    print(i)