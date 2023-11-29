

fh = open('id.txt')
fh2 = open('random.txt', 'w')
count = 0

with fh as f:
    for oid in f:
        count += 1
        if count % 4 == 0:
            fh2.write(oid)
