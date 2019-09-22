#####################
# Printing_class_01 #
#####################

# Create object  "printing_object_01"
printing_object_01 = Printing_class_01('la','lala')

# Run print_01 method
printing_object_01.print_01()

# Run print_02 method
printing_object_01.print_02()


#####################
# Printing_class_02 #
#####################

# Create object  "printing_object_02"
printing_object_02 = Printing_class_02('la','lala')

# Run "print_03_boost" method
printing_object_02.print_03_boost()


#####################
# Printing_class_03 #
#####################

# * Added new argument in child class constructor *

# Create object  "printing_object_02"
printing_object_03 = Printing_class_03(field_01='la',field_02='lala',
                                       field_03='x')

# Run "print_03_boost" method
printing_object_03.print_03_boost()
