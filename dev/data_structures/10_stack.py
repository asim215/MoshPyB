# Stack implementation
browsing_session = []
# Add address of current web site
# Add to stack
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
# Print stack
print("current stack ", browsing_session)

# Remove last from stack
last = browsing_session.pop()
print("pop ", last)
# Print current state
print("current stack ", browsing_session)
print("redirect", browsing_session[-1])


def read_elem(browsing_session):
    # Check on empty stack to action
    # [] - falsy
    if not browsing_session:
        print("disable back button. stack is empty")
    else:
        print("redirect", browsing_session[-1])


# if stack:
#     # true
#     read_element[-1]
# else:
#     # false
#     "stack is empty"
