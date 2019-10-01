Scores = [69, 32, 64, 128,35]

print("High scores: \n")
for i in range(len(Scores)):
    print("{}. {}".format(i+1, Scores[i]))

newScore = int(input("Enter your new score: "))

Scores.append(newScore)

print("High scores: \n")
Scores.sort(reverse=True)
for i in range(5):
    print("{}. {}".format(i+1, Scores[i]))
