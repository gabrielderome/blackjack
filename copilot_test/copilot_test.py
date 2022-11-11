#create an interactive graph of the distribution of 6000 dice rolls
import plotly.graph_objects as go
dice_roll_num = 0

while (dice_roll_num <= 6000):
    dice_roll_num = dice_roll_num + 1
    dice_roll = [random.randint(1,6) for i in range(6000)]
    fig.add_trace(go.Histogram(x=dice_roll))
