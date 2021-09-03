# 1. Consider the following Python function. 

def mystery(l):
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])

# What does mystery([22,34,18,57,92,45]) return?

# Ans: [45, 92, 57, 18, 34, 22]


# 2. What is the value of pairs after the following assignment? 

pairs = [ (x,y) for x in range(5,1,-1) for y in range(4,1,-1) if (x+y)%3 == 0 ]

# Ans: [(5, 4), (4, 2), (3, 3), (2, 4)]


# 3. Consider the following dictionary. 

wickets = {"Tests":{"Ishant":[3,5,2,3],"Shami":[4,4,1,0],"Bumrah":[2,1,7,4]},"ODI":{"Ishant":[2,0],"Shami":[1,2]}}

# Which of the following statements does not generate an error?
# Options:-
    # wickets["ODI"]["Bumrah"][0:] = [4,4]
    # wickets["ODI"]["Bumrah"].extend([4,4])
    # wickets["ODI"]["Bumrah"] = [4,4]
    # wickets["ODI"]["Bumrah"] = wickets["ODI"]["Bumrah"] + [4,4] 

# Ans: wickets["ODI"]["Bumrah"] = [4,4]


# 4. Assume that hundreds has been initialized as an empty dictionary: 

hundreds = {}

# Which of the following generates an error?
# Options:-
    # hundreds["Tendulkar, international"] = 100
    # hundreds["Tendulkar"] = {"international":100}
    # hundreds[("Tendulkar","international")] = 100
    # hundreds[["Tendulkar","international"]] = 100 

# Ans: hundreds[["Tendulkar","international"]] = 100 