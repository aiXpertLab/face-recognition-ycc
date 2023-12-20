first_name  =   "ada"
last_name   =   "lovelace"
full_name   =   first_name + " "+ last_name
name = f"{first_name} {last_name}"
message = f"     hello,\t\t\n {full_name.title()} !!!"
message_strip = message.strip()
print(message_strip)

nostarch_url = 'https://nostarch.com'
url = nostarch_url.removeprefix('https://')
print(url)