#to store data
#read data from file named text and display contents here
#read r
#write w
#append a
#step 1
#create file reference

#f=open("path","mode of operation")

f=open("text","r")
st=set()
for lines in f:
    st.add(lines.rstrip("\n"))
print(st)