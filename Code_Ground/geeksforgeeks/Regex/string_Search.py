import re

# All single character strings satisfies the condition that they start and end with the same character.
# The regex for a string with only 1 character will be-
regex_Single = r'^[a-z]$'

#Here we need to check whether the first and the last character is same or not.
# We do this using \1.
regex_Multiple = r'^([a-z]).*\1$'

def string_single_search(string):

   if(re.search(regex_Single, string)):
       print('Valid')
   else:
       print('Invalid')



def string_multiple_search(string):

   if(re.search(regex_Multiple, string)):
       print('Valid')
   else:
       print('Invalid')


sample1 = "abccba"
sample2 = "a"
sample3 = "abcd"

string_multiple_search(sample1)
string_single_search(sample2)
string_multiple_search(sample3)