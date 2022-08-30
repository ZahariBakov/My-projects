print("Welcome to Mad Lips game\n"
      "     Have fun!!!\n"
      "")
print("                        THE MAGIC COMPUTERS        ")
print()

noun = input("Choose a noun: ")
plural_noun = input("Choose a plural noun: ")
verb = input("Choose a verb (presents tense): ")
second_verb = input("Choose a verb (presents tense): ")
body_part = input("Choose a part of body (plural): ")
adjective = input("Choose a adjective: ")
second_plural_noun = input("Choose a plural noun: ")
second_adjective = input("Choose a adjective: ")

print()
print(f"Today, every student has a computer small enough to fit into his \n"
      f"\033[91m{noun.upper()}\033[0m. He can solve any math problem by simply \n"
      f"pushing the computer's little \033[91m{plural_noun.upper()}\033[0m. Computers \n"
      f"can add, multiply, divide, and \033[91m{verb.upper()}\033[0m. They \n"
      f"can also \033[91m{second_verb.upper()}\033[0m better than a human. Some \n"
      f"computers are \033[91m{body_part.upper()}\033[0m. Others have an \n"
      f"\033[91m{adjective.upper()}\033[0m screen that shows all kinds of \033[91m{second_plural_noun.upper()}\033[0m \n"
      f"and \033[91m{second_adjective.upper()}\033[0m figures.")
print()
print("Did you have fun?")
command = input("Do you want to continue? y/n: ")

if command.lower() == "n":
      print("Bye!")
      exit()
else:
      print("                             SNEAKERS           ")
      print()

      adjective = input("Choose a adjective: ")
      invention = input("Choose an invention: ")
      food = input("Choose a food: ")
      second_adjective = input("Choose a adjective: ")
      body_part = input("Choose a part of body (plural): ")
      third_adjective = input("Choose a adjective: ")
      plural_noun = input("Choose a plural noun: ")
      second_plural_noun = input("Choose a plural noun: ")

      print()
      print(f"I would lika to say a few \033[91m{adjective.upper()}\033[0m word about the \n"
            f"most important invention of the twentieth century. I am not \n"
            f"referring to \033[91m{invention.upper()}\033[0m or even to the discovery of \n"
            f"\033[91m{food.upper()}\033[0m. The most \033[91m{second_adjective.upper()}\033[0m invention, \n"
            f"in my opinion, is the sneaker. If it were not for sneakers, our \n"
            f"\033[91m{body_part.upper()}\033[0m would be dirty, cold, and \n"
            f"\033[91m{third_adjective.upper()}\033[0m. Sneakers keep me from skidding if the \n"
            f"\033[91m{plural_noun.upper()}\033[0m are slippery, and when I run, they keep me \n"
            f"from stubbing my \033[91m{second_plural_noun.upper()}\033[0m.")
