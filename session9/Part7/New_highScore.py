Scores = [69, 32, 64, 128]
print("High scores: \n")
for i in range(len(Scores)+1):
    print("{}. {}".format(i+1, Scores[i]))
newScore = int(input("Enter your new score: "))
print("High scores: \n")
for i in range(len(Scores)+1):
    print("{}. {}".format(i+1, Scores[i]))