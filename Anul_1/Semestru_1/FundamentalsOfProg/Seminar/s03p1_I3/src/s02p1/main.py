'''


@author: radu


Write an application which manages the students of a faculty. 
Each student has a unique id, a name and a grade. The application should 
allow to:

F1: print all students 
F2: add students
F3: delete students
F4: show students whose grades are >= a given value
F5: find a student with the maximal grade
F6_: split the application into modules (main, ui, domain, util)
F7_: validate input data
F8_: student_id is unique - validation in add, delete etc.
F9: find all students whose name contain a string t (the match should not be
    case sensitive)  
F10: undo
F11: remove all students with the grade smaller than 5 (using TDD)
F12: sort students according to their grade (descending)  (using TDD)
F13: given an integer 'nr', find the top nr students according 
     to their grade  (using TDD)
F14: compute the average grade of all students having the grade >= 5 (using TDD)
F15: sort all students according to their grade and alphabetically (using TDD). 
------------

I1: F1, F2, F3, F4, F5
I2: F6_, F7_
I3: F8_, F9
I4: F10
I5: F11, F12, F13, F14, F15
'''

from s02p1.ui.console import run_app



if __name__ == '__main__':
    
    run_app()
    
    print("Bye")
    
    
    
    
