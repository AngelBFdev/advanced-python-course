# Demonstrate how to use dictionary comprehensions


def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    # this make the result the value of the dictionary
    # and the keys the original name
    tempDict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])

    # Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    # what's happening is this key value is going to get inserted
    # into this "team" dictionary, and it's going to get all the
    # keys and values from team1 and team2. Then we're gonna loop
    # over all of that and get the key and value to put into
    # "newTeam"
    newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)


if __name__ == "__main__":
    main()
