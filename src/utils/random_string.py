__all__ = ['generate_random_string']
import string
import random
def generate_random_string(length, all_characters=string.ascii_letters + string.digits):
  '''
  Generate a random string of given length using given characters.
  :param length: Length of the string to generate.
  :param all_characters: Characters to use for generating the string.
  :return: Random string of given length.

  Example:
  >>> generate_random_string(5)
  'bYq3A'
  '''
  return ''.join(random.choice(all_characters) for i in range(length))
