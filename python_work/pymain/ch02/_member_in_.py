database = [
    ['albert', '1234'],
    ['dilbert', '2323'],
    ['smith', '7543']
]

username = input('User name: ')
pin = input('PIN code:')

if [username, pin] in database: print('Access Granted')
