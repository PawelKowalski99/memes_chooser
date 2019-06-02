# memes_chooser

## Description
Dark times have come. Article 13 has been passed almost 2 years ago. Memes are illegal. People use USB sticks to store and sell them
for caps. Every meme is identified by a size, given in MiB, and its market price. xXxDankScavengerxXx sells memes as his way of 
earning a living. Help him by writing function ​ calculate(usb_size, memes) thatcalculates the best set of memes, so that he can sell
the USB stick for the highest price. 

  Example input:<br>
  `usb_size = 1 memes = [ ('rollsafe.jpg', 205, 6),
  ('sad_pepe_compilation.gif', 410, 10),
  ('yodeling_kid.avi', 605, 12) ]`<br>
  Should return:<br>
  `(22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'}) `

## Solution explanation
Problem is solved by a bottom-up approach to the difficulty. This means that results are stored in two dimensional(amount of memes, usb_size)
lists. Solution is stored in the last index of 2d list. Complexity of algorithm is dependent on size of table O(amount_of_memes*usb_size)

## Installation

Firstly clone the repository. When you have got it cloned install all requirements.
    
    pip install -r /path/to/requirements.txt
Function is inside main.py folder.<br>
If you want to download tests just install:
    
    pip install -r /path/to/requirements_test.txt
    
## Performance test

I used cProfile to test performance
For a given input
    
    usb_size = 1
    memes_list = [('Dick_butt.jpg', 205, 6),
                                  ('do_you_even_lift?.gif', 410, 10),
                                  ('Deal_With_It.avi', 126, 11),
                                  ('Ricardo_Milos.gif', 584, 20),
                                  ('homophobic_seal.gif', 320, 25),
                                  ('delete_sys32.avi', 175, 16),
                                  ('fus_ro_dah.jpg', 105, 10),
                                  ('it_is_over_9000.gif', 210, 19),
                                  ('Leeroy_jenkins.avi', 105, 14),
                                  ('The_cake_is_a_lie.jpg', 265, 9),
                                  ('swag.gif', 320, 15),
                                  ('duck_face.avi', 635, 11)]
 
 The performance is:
      
       Ordered by: standard name

        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.021    0.021 main.py:1(<module>)
            1    0.018    0.018    0.021    0.021 main.py:1(calculate)
            1    0.000    0.000    0.001    0.001 main.py:11(<listcomp>)
            1    0.000    0.000    0.001    0.001 main.py:12(<listcomp>)
            1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
         8840    0.002    0.000    0.002    0.000 {built-in method builtins.max}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
            1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
            
            
## Description for first problem
 
Zaimplementuj funkcję o nazwie: merge, która przyjmuje dwa argumenty: persons_file i visits_file. Funkcja łączy dane z dwóch plików podanych jako argumenty wywołania. persons_file to obiekt plikowy CSV zawierający dane użytkownika w formie: id, name, surname. visits_file to obiekt plikowy CSV, który zawiera dane w formie: id, person_id, site, gdzie person_id to id danego użytkownika.
### Solution for first problem

    import csv


    def merge(persons_file, visits_file):
        dict_users = {}
        pf_reader = csv.reader(persons_file, delimiter=',')
        next(pf_reader)
        for row in pf_reader:
            user = {
                row[0]: {
                    "id": row[0],
                    "name": row[1],
                    "surname": row[2],
                    "visits": 0,
                }
            }
            dict_users.update(user)
        vf_reader = csv.reader(visits_file, delimiter=',')
        next(vf_reader)
        for row in vf_reader:
            if row[1] in dict_users.keys():
                dict_users[row[1]]['visits'] += 1
        return list(dict_users.values())
