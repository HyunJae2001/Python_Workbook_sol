BASE_CHARGE = 15
SUPPORT_911 = 0.44
AIR_TIME = 0.25
TEXT_MESSAGE = 0.15
TAX = 0.05

air_time = int(input('Enter the number of minutes: '))
text_messages = int(input('Enter the number of text messages: '))
total = BASE_CHARGE + SUPPORT_911

print(f'Base charge: {BASE_CHARGE}')

if air_time > 50:
    additional_minutes = (air_time - 50) * AIR_TIME
    total += additional_minutes
    print(f'Additional minutes charge: {additional_minutes}')
if text_messages > 50:
    additional_messages = (text_messages - 50) * TEXT_MESSAGE
    total += additional_messages
    print(f'Additional text message: {additional_messages}')

tax = total * TAX
total += tax

print(f'911 fee: {SUPPORT_911}')
print(f'Tax: {tax:.2f}')
print(f'Total bill amount: {total:.2f}')