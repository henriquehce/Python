temperature = int(input('Digite a temperatura da carne: '))
if 48 <= temperature <= 53:
    print('Carne selada')
if 54 <= temperature <= 59:
    print('Carne ao ponto menos')
if 60 <= temperature <= 64:
    print('Carne ao ponto')
if 65 <= temperature <= 70:
    print('Carne ao ponto mais')
if temperature > 71:
    print('Carne bem passada')

# ----------------------------------------------------------------

temperatura = int(input('Digite a temperatura da sua carne: '))
if temperatura <= 48:
    print('Carne selada')
elif temperatura in range(49, 59):
    print('Carne ao ponto menos')
elif temperatura in range(60, 64):
    print('Carne ao ponto')
elif temperatura in range(65, 70):
    print('Carne ao ponto mais')
elif temperatura >= 71:
    print('Carne bem passada')
