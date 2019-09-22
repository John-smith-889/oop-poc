class Printing_class_01:
    """
    Class for printing. 
    """

    # Constructor method
    def __init__(self, field_01, field_02, **kwargs):
	# **kwargs enable to pass new argument in further child classes
	
        # Store value to field field_01 in the object
        self.field_01 = field_01
        self.field_02 = field_02 

    # print_01 method
    def print_01(self):
        """ Print  """
        print(self.field_01)
        print(self.field_02)
     
    # print_02 method   
    def print_02(self):
        """ Print double  """
        x = 2*(self.field_01)
        y = 2*(self.field_02)
        print(x)
        print(y)

    # print_03 method for passing computed parameters without printing
    def print_03(self):
        """ Printing parameters pass  """
        x = 2*(self.field_01)
        y = 2*(self.field_02)
        
        # returning variable x
        return x