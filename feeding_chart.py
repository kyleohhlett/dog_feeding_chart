import matplotlib.pyplot as plt

cups_four_to_eight_months = [0.5, 0.75, 1.333, 2.25, 3, 3.75, 5.25, 6.25]
cups_eight_to_twelve_months = [0.5, 0.666, 1.25, 1.75, 2.333, 3, 4.25, 5]
weight = [3, 5, 10, 20, 30, 40, 60, 80]

fig, ax = plt.subplots()

four_to_eight_months_plot, = ax.plot(weight, cups_four_to_eight_months, label='4-8 months')
eight_to_twelve_months_plot, = ax.plot(weight, cups_eight_to_twelve_months, label='8-12 months')

ax.set(xlabel='Weight (Pounds)', ylabel='Cups', title='Feeding chart')
ax.grid()
ax.legend(handles=[four_to_eight_months_plot, eight_to_twelve_months_plot])

fig.savefig("feeding_chart.png")
plt.show()