import pygal

# Sample data for demonstration
labels = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

# Pie Chart
pie_chart = pygal.Pie()
pie_chart.title = 'Pie Chart Example'
for i in range(len(labels)):
    pie_chart.add(labels[i], values[i])
pie_chart.render_to_file('pie_chart.svg')  # Save Pie Chart as SVG

# Bar Chart
bar_chart = pygal.Bar()
bar_chart.title = 'Bar Chart Example'
for i in range(len(labels)):
    bar_chart.add(labels[i], values[i])
bar_chart.render_to_file('bar_chart.svg')  # Save Bar Chart as SVG

# Line Graph
line_chart = pygal.Line()
line_chart.title = 'Line Graph Example'
line_chart.x_labels = labels
line_chart.add('Values', values)
line_chart.render_to_file('line_chart.svg')  # Save Line Graph as SVG

# Scatter Plot
scatter_plot = pygal.XY(stroke=True)
scatter_plot.title = 'Scatter Plot Example'
# (x, y) pairs
scatter_data = list(zip([1, 2, 3, 4], values))
scatter_plot.add('Data Points', scatter_data)
scatter_plot.render_to_file('scatter_plot.svg')  # Save Scatter Plot as SVG
