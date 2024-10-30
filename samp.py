import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aigberuan6@gmail.com', 'ebbipubecvdmzeam')
    print("Successfully connected to the SMTP server.")
    server.quit()
except Exception as e:
    print(f"Failed to connect: {e}")
