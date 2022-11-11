#create an interactive graph of the distribution of 6000 dice rolls
import random
import plotly.graph_objects as go
dice_roll_num = 0

fig = go.Figure()
fig.show()
#update the graph every 10 dice rolls
while (dice_roll_num <= 6000):
    dice_roll_num += 1
    dice_roll = random.randint(1,6)
    fig.add_trace(go.Histogram(x=[dice_roll], name="Dice Roll"))
    if dice_roll_num % 10 == 0:
        fig.update_layout(barmode='overlay')
        fig.update_traces(opacity=0.75)
        fig.show()