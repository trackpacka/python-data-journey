clubs = ["Real Madrid","Slavia Praha","Manchaster United","Benfika Lisabon","TJ Zemas Hovorany"]
print(clubs)
print(clubs[0])
print(clubs[-1])
clubs.append("TJ Sokol Čížová")
print(clubs)
for i in range(len(clubs)):
    print(f"Club: {clubs[i]}")
print(len(clubs))
clubs_sorted=sorted(clubs)
print(clubs_sorted[0])
print(clubs_sorted[-1])
for i in range(len(clubs)):
    print(f"{i+1}. {clubs[i]}")
