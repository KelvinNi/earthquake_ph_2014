import heatmap
import random
import csv

f = open("results.csv", 'rt')
rows = []

try:
  reader = csv.reader(f)

  for row in reader:
    rows.append(row)

  # rows = rows[1:3]

  points = [(float(row[1]), float(row[2])) for row in rows]

  hm = heatmap.Heatmap()
  img = hm.heatmap(points)
  img.save("classic.png")
finally:
    f.close()