# Scenario 1
# ctrl+f or grep PHONE_NUMBER FILENAME

## dummy code
# def check_one-time_route:
#     file = open("route-costs-10", "r")
#     for line in file:
#         # Check whether
#     file.close()


# Scenario 2
# 1.
# try to match by Binary Search: O(n*log(n))
# if not match, chop off the last digit: O(k*p*log(n))
# n=100k route list, p=1000numbers, k=# digits
# or
# 2.
# linear search: O(n*p)

# Scenario 3
# 1. hash for number and carrer (2 hash tables). It's fast but doesn't work well or more complicated when thinking about one carrer has 415 (0.3)and 415568(0.87), second carrer has 415 (0.4), you cannot choose 1st carrer's 415.
# 2. trie
