__author__ = 'Chris Johnson'



import matplotlib.pyplot as plt


class SinglePlotLine:
    def __init__(self, list_number_states_explored, terminal_solution_qualities, line_label, line_style, line_marker):
        self.x = list_number_states_explored
        self.y = terminal_solution_qualities
        self.label = line_label
        self.style = line_style
        self.marker = line_marker


class Graph:

    def __init__(self, domain, range, x_label, y_label, title, caption):
        self.domain = domain
        self.range = range
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.lines = []
        self.caption = caption


    def add_line(self, list_number_states_explored, terminal_solution_qualities, line_label, line_style, line_marker):
        self.lines.append(SinglePlotLine(list_number_states_explored, terminal_solution_qualities, line_label, line_style, line_marker))




    def graph(self):

        fig, ax = plt.subplots()

        plt.xlim(self.domain)
        plt.ylim(self.range)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        fig.text(.65, .28, self.caption)
        for line in self.lines:
            ax.plot(line.x, line.y, label=line.label, linewidth=2.0, marker=line.marker, linestyle=line.style)

        legend = ax.legend(loc='lower right', shadow=True)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')

        for label in legend.get_texts():
            label.set_fontsize('large')

        for label in legend.get_lines():
            label.set_linewidth(1.5)  # the legend line width



        plt.show()


