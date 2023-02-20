for i in range(10):
    print(i)
print("hello jenkins")

# bug_1
print(1/0)

# bug_2
a = "hahh"
print(a + 2)

# bug_3
narg=len(sys.argv)
if narg == 1:
    print('@Usage: input_filename nelements nintervals')
    break

# bug_4
def adder(n):
     num = 0
     while num < n:
         yield num
         num += 1
     return num  #Noncompliant

# bug_5
exec 'print 1' # Noncompliant
