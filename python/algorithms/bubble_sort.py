import pdb


class BubbleSort:

    def __init__(self, input_array):
        self.input_array = input_array
        self.sort_array = input_array[:]
        self.steps = []
        self.iteration = 0

    def sort(self, no_of_elements = None):
        self.iteration += 1
        if no_of_elements is None:
            no_of_elements = len(self.sort_array) - 1

        if no_of_elements == 1:
            return

        pass_output = []
        swapped = False

        for i in range(0, no_of_elements):
            # print(f"With i as {i}: comparing {self.sort_array[i]} and {self.sort_array[i+1]}")
            if self.sort_array[i] > self.sort_array[i + 1]:
                # print(f"Swapping {self.sort_array[i]} and {self.sort_array[i+1]}")
                # pdb.set_trace()
                pass_output.append(self.sort_array[:])
                # pdb.set_trace()
                self.sort_array[i], self.sort_array[i + 1] = self.sort_array[i + 1], self.sort_array[i]
                swapped = True
            else:
                pass_output.append(self.sort_array[:])

        self.steps.append(' -> '.join(str(pass_op) for pass_op in pass_output))
        if swapped:
            self.sort()
        else:
            return

