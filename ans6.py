st = "Create a list of the first letter of every word in this string"
# for word in st.split():
#     print(*list(word[0]))
l = [word[0] for word in st.split()]
print(*l,sep="\n")