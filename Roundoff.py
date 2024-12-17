class Average:
    def __init__(self, input_value):
        self.input_value = input_value
        self.output_value = []

    def get_round_off(self, value):

        """
        Rounds off the provided value to the nearest multiple of 0.05. If the value
        is less than 0.025, it returns 0.00. Otherwise, the value is rounded as
        per the nearest step of 0.05.

        :param value: A float or integer representing the number to be rounded off.
        :return: The rounded-off value as a float.
        """
        if value < 0.025:
            return 0.00
        else:
            round_off = round(value * 20)/20
            return round(round_off ,2)

    def get_input(self):
        """
        Input value is passed if input value is not given then it will print as No input data provided else it will passes the value to the get_round_off function.
        :return output value from the round off function:
        """
        if not self.input_value:
            print("No input data provided.")
            self.output_value = []
            return
        self.output_value = [self.get_round_off(value) for value in self.input_value]

    def get_output(self):
       return self.output_value

if __name__ == "__main__":

    custom_input = [0.21, 0.22, 0.226, 0.23, 0.241, 0.25, 1.1 , 1.2, 1.23, 1.42, 7.57, 7.58, 11.33 ,15.33]

    input_val = Average(custom_input)
    print(f"The input before rounding off value is {input_val}")
    input_val.get_input()
    print("The rounded off value is ", input_val.get_output())
