__verson__ = 0.1

Name =""
Desr =""
Gender =""
Race  =""

# Prompt user for defined information
Name = input('What is your Name?')
Desc = input('Describe yourself:')
Gender = input('What Gender are you? (male / female / unsure):')
Race = input('What fantacy Race are you? -(Pixie / Vulcan /Gelfling /Troll):')

# Output the character sheet
fancy_line = "_________________________________"
print("\n", fancy_line)
print("\t", Name)
print("\t", Race , Gender)
print("\t", Desc)
print(fancy_line, "\n")
