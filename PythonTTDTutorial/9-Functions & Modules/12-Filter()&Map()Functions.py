# filter(function, sequence)

# seq = [1,2,3,4]
# odd = lambda x : True if x % 2 !=0 else False
# filtered_output = filter(odd, seq)
# print(f"Filtered Object Output - {filtered_output}")
# print(f"Odd numbers in the above sequence - {list(filtered_output)}")

# seq = [1,2,3,4]
# filtered_output = filter(lambda x : True if x % 2 !=0 else False, seq)
# print(f"Filtered Object Output - {filtered_output}")
# print(f"Odd numbers in the above sequence - {list(filtered_output)}")


# map(function,sequence)
# seq = [1,2,3,4]
# mapped_output = map(lambda x : True if x % 2 !=0 else False, seq)
# print(f"Mapped Object Output - {mapped_output}")
# print(f"Odd numbers in the above sequence - {list(mapped_output)}")

seq = [1,2,3,4]
mapped_output = map(lambda x :  x ** 2, seq)
print(f"Mapped Object Output - {mapped_output}")
print(f"Square of the elements in the above sequence - {list(mapped_output)}")
