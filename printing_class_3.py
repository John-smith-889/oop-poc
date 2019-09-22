class Printing_class_03(Printing_class_01):

    # A constructor with one new field defining
    def __init__(self, field_03, **kwargs):
        self.field_03 = field_03
        super().__init__(**kwargs)
	
    def print_03_boost(self):
        # Create variable with the longest lala
        longest_lala = 3*(self.print_03())+self.field_03
        
        # print the longest lala
        print(longest_lala)

# As we can see there is no need to define constructor, 
# because it is inherited from parent class
