# https://docs.python.org/3/tutorial/inputoutput.html
# Fancier Output Formatting
# IT WILL WORK ON PYTHON 3.6 OR ABOVE
name = "haaland"
print(f"hello {name} this is cool")

 # CREATE A SET
names = {"kilyon", "ronaldo", "rashford", "kilyon"} # no duplicate valud
for name in names:
    print("Name from set: ",name)

msg = "Hi there, " + " this is cool " + " The end. "
for i in names:
    msg += f" name: {i}, "

print("Adding message to name: ",msg)
name = ""
template = """Hello there,
    {name} this is an amazing way to do
    subbming my cool items. 
"""

print(template)
print(template.format(name= "Joao Fleix"))
print(template.replace('Hello', "hi"))

print("http://localhost:5000")
file_directory_win = "C:\\\\localdisk"  # first two slash to scape next two slash
print("Windows file directory: ",file_directory_win)


template_replace = "{name} is cool, Include {} to include curly brackets use {{}}".format( "empty replace", name="Martinez")
print("Template replacement: ",template_replace)

print(f"F string: {template}")

pi = 3.37483656
f_str = f"{pi}"
print("{}".format(pi))
print("{:f}".format(pi))
print("{:f}".format(23))
print("{:.2f}".format(pi))
print("{:.4f}".format(pi))
print(format(pi, ".2f"))
print(pi* 10)
print(format(pi, ".2f") * 3)



