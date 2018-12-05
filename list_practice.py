#make a list of people, then print one of their names using the list
friends=['jacob brugger', 'jamie dearmas', 'justin houston']
print(friends[0].title())

#print a message to one of the people on the list
print(friends[0].title()+", how are you?")

#print a message about a list regarding each item on the list
dragon_ball=["dragon ball", "dragon ball z", "Dragon Ball GT", "dragon ball super"]
print("While " +
dragon_ball[0].title() +
" started the series, "+dragon_ball[1].title() +
" was the mainstay of the series. Years later, "+dragon_ball[2] +
" and " +
dragon_ball[-1].title() +
" were released.")