import pyotp

# generate a current OTP
secret_key = 'SECRET_KEY' # do not share your secret key with anyone!!
otp_code = pyotp.TOTP(secret_key)

# print token
print(otp_code.now())