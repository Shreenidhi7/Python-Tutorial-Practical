scores = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]
print(f"Length of the list - {len(scores)}")

# # Finding Total -> Traditional Way
# total = 0
# for score in scores:
#     total = total + score
# print(f"Total runs scored {total}")

# # Finding Total -> Using Sum
# total = sum(scores)
# print(f"Total - {total}")

###################################

# Finding Highest
# highest = scores[0]
# for score in scores:
#     if highest < score:
#         highest = score
# print(f"Highest score - {highest}")

# highest = max(scores)
# print(f"Highest value - {highest}")

#######################################

# Finding Lowest

# lowest = scores[0]
# for score in scores:
#     if score < lowest:
#         lowest = score
# print(f"The lowest score is {lowest}")

lowest = min(scores)
print(f"Lowest value - {lowest}")