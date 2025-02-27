import csv

row = []
lW = []
lA = []
rA = []
rW = []

planeSeatingChart = [
    ["1", "A", "B", "C", "D"],
    ["2", "A", "B", "C", "D"],
    ["3", "A", "B", "C", "D"],
    ["4", "A", "B", "C", "D"],
    ["5", "A", "B", "C", "D"],
    ["6", "A", "B", "C", "D"],
    ["7", "A", "B", "C", "D"]
]

with open("collectionsAndLogic.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(planeSeatingChart)
    for i in range(len(row)):
        if i < len(row) - 1:
            writer.writerow([row[i], lW[i], lA[i], rA[i], rW[i]])
        else:
            csvfile.write(f"{row[i]},{lW[i]},{lA[i]},{rA[i]},{rW[i]}")