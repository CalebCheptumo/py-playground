first_name = "caleb"
last_name = "cheptumo"
full_name = f"{first_name} {last_name}"
message = f"Hello {full_name.title()} what's up?"
print(message)

print(full_name.title())
print(full_name.upper())
print(full_name.lower())


quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(quote)


author = "Charlie Tahan once said , "
quote = "\"I don't try and be a competitive with auditions. When i go on one i do my best and leave it at that.\""
famous_quote= f"{author}{quote}"
print(famous_quote)


today = " Date:\n\t21/12/2023\nTime:\n\t1532hrs "
print(today)
print(today.lstrip())
print(today.rstrip())
print(today.strip())



filename = "python_notes.txt"
print(filename.removeprefix("python_"))
print(filename.removesuffix(".txt"))