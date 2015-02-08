import re

with open("data.txt") as f:
  lines = f.readlines()

print "Date, Latitude, Longitude, Depth, Magnitude"

for line in lines:
  line = re.sub(' +', ' ', line)
  line_array = line.split(' ')

  # print line_array
  try:
    # print ' '.join(line_array[0:6])
    # print line_array[6]
    # print line_array[7]
    # print line_array[8]
    # print line_array[9]

    print "%s,%s,%s,%s,%s" % (' '.join(line_array[0:6]),
      line_array[6],
      line_array[7],
      line_array[8],
      line_array[9])
  except:
    pass