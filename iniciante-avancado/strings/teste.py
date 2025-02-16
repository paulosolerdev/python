def convert_time_to_seconds(days, hours, minutes, seconds):
    """Converts time components into total seconds."""
    return seconds + (minutes * 60) + (hours * 3600) + (days * 86400)

def celsius_to_fahrenheit(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return (9 * celsius) / 5 + 32

def calculate_phone_bill(minutes):
    """Calculates the phone bill based on minutes used."""
    if minutes < 200:
        price_per_minute = 0.20
    elif minutes < 400:
        price_per_minute = 0.18
    else:
        price_per_minute = 0.15
    return minutes * price_per_minute

if __name__ == "__main__":
    # Example usage:
    # Time conversion
    days = int(input('Digite o número de dias: '))
    hours = int(input('Digite o número de horas: '))
    minutes = int(input('Digite o número de minutos: '))
    seconds = int(input('Digite o número de segundos: '))
    total_seconds = convert_time_to_seconds(days, hours, minutes, seconds)
    print(f'Total em segundos: {total_seconds}')

    # Temperature conversion
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f'A temperatura em Fahrenheit é: {fahrenheit}')

    # Phone bill calculation
    minutes_used = int(input('Quantos minutos você utilizou este mês?: '))
    bill = calculate_phone_bill(minutes_used)
    print(f'Você vai pagar R${bill:6.2f} este mês.')
