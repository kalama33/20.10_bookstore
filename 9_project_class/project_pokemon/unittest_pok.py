import unittest
from pokemon import AttackSkill, Pokemon

# proof methods attack and show status
# creation of 2 instances
# implementation method learn.....
class TestPokemon(unittest.TestCase):
    def test_attack(self):
        lightning = AttackSkill("Lightning", 25, 25)
        pikachu = Pokemon("Pikachu", 100, 100)
        pikachu.learn_attack_skill(lightning)

        opponent = Pokemon("Opponent", 100, 100) #creation instance opponent
        pikachu.attack("Lightning", opponent) # method attack

        self.assertEqual(pikachu.counter, 1) # verify if counter got the expected values
        self.assertEqual(opponent.health, 75)
        self.assertEqual(pikachu.magic, 75)

    def test_show_status(self):
        pikachu = Pokemon("Pikachu", 100, 100)
        pikachu.counter = 4 ### 

        captured_output = self._captured_output(pikachu.show_status) #### capture output
        expected_output = "Pikachu: Health: 100, Magic: 100\nPikachu has won the battle!\n\n"
        self.assertEqual(captured_output, expected_output) ###


        """_
        This _captured_output method is used to capture the printed output 
        of a function or method. It takes a function or method as an argument 
        and redirects the standard output to a StringIO object to capture it. 
        It then returns the captured contents as a string.
        """
    
    def _captured_output(self, func):
        import io   # op in/out
        from contextlib import redirect_stdout # painpoint allows you to redirect the standard output
                                               # (what is printed on the console) to a specific object
        captured_output = io.StringIO()        # create empty object that simulate a file in the memory, store a str.
       
        """
        This line sets the standard output redirection to the captured_output object. 
        Anything printed during this with block will be stored in captured_output instead 
        of being displayed in the console.
        """
       
        with redirect_stdout(captured_output): # se guarda en la funcion, no se imprime
            func()                             # funcion arriba

        return captured_output.getvalue() # captured_output as a str.

if __name__ == '__main__':
    unittest.main()