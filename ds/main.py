import pandas as pd
                                            # Omar Zakaria & Mohamed Osama
busesSheet = pd.read_csv(r'last.csv')
lines = list(busesSheet.Road)               # Bus Lines
linesNumbers = list(busesSheet.lineNum)     # Bus line numbers

routeListOfLists = []                       # Routes of all Bus lines

for line in lines:
    lineRoute = []                          # Bus line root
    lineStations = line.split("–")          # Bus line stations

    for station in enumerate(lineStations, 1):
        lineRoute.append(station)           # Route is tuple of a line's ordered stations

    routeListOfLists.append(lineRoute)      # Routes of all Buses lines
    print(routeListOfLists)

routesDictionary = {}
lineNumber = 0

for route in routeListOfLists:
    routesDictionary.update({lineNumber: route})
    lineNumber += 1

print(routesDictionary)
