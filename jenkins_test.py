for i in range(10):
    print(i)
print("hello jenkins")

# bug_1
print(1/0)

# bug_2
a = "hahh"
print(a + 2)

narg=len(sys.argv)
if narg == 1:
    print('@Usage: input_filename nelements nintervals')
    break
