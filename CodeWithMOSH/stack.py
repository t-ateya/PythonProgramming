browswing_session = []
browswing_session.append(1)
browswing_session.append(3)
browswing_session.append(5)
browswing_session.append(9)
print(browswing_session)

last = browswing_session.pop()
print(last)
print(browswing_session)
if not browswing_session:
    browswing_session[-1]
print("redirect: ", browswing_session[-1])
