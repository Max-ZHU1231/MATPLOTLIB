from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die(10)

results = []
max_result = die_1.num_sides + die_2.num_sides
min_result = 2

times = 10000
for roll_num in range(times):
    result = die_1.roll()+ die_2.roll()
    results.append(result)

frequencies = []
possible_results = range(min_result,max_result+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency/times)

title = "Results of Rolling a D6 and a D10 10000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick = 1)

fig.show()