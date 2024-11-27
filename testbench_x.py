from graficos import XBarChart


samples = [
    [4.1, 4.3, 4.2, 4.0],
    [4.2, 4.5, 4.3, 4.1],
    [4.0, 4.1, 3.9, 4.2],
    [4.3, 4.4, 4.5, 4.2],
    [4.1, 4.3, 4.2, 4.4]
]

samples2 = [
    [5.2, 5.0, 5.3, 5.1],
    [5.1, 4.9, 5.2, 5.0],
    [5.3, 5.1, 5.4, 5.2],
    [4.9, 5.0, 5.1, 4.8],
    [5.2, 5.1, 5.3, 5.0]
]

A2 = 0.577 #para 5 amostras
D3 = 0.0
D4 = 2.114

xbar_chart = XBarChart(samples, A2)
xbar_chart.calculate_means_and_ranges()
xbar_chart.calculate_control_limits()
xbar_chart.plot()