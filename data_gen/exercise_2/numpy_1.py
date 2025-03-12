import numpy as np
from data_gen.main import np_city                
'''needed absolute import like above line to run the code and
code to run this script as a module :prabin_linux@prabin:~/ai/datacamp_intro_to_python$ python3 -m data_gen.exercise_2.numpy_1
errors encountered:
- absolute import inside a sub-folder, one of the soln: run the script as a  module
- if __name__ == '__main__': ;;; used this and had np_city inside which caused the error !!  
'''
# Create np_height_in from np_baseball
np_height_in = np_city[:,0]
print(np_city)
# Print out the mean of np_height_in
print(np.mean(np_height_in[:]))

# Print out the median of np_height_in
print(np.median(np_height_in[:]))