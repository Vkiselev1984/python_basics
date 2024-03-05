"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

"""
    Format time into hours:minutes:seconds format
    Convert seconds to hours, minutes, and seconds.
    divmod(divident, divisor)
    tuple - кортеж вида (частное, остаток)
    Args:
        seconds (float): The number of seconds to convert.
    Returns:
        tuple: A tuple containing the hours, minutes, and seconds.
"""
def convert_seconds(seconds):
    """divmod(divident, divisor) -> (quotient, remainder)"""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

"""
    Format time into hours:minutes:seconds format
     Args:
            hours (float): The number of hours.
            minutes (float): The number of minutes.
            seconds (float): The number of seconds.
            format_time(hours, minutes, seconds) -> str: 
    """
def format_time(hours, minutes, seconds):
    return f"{hours:.1f}:{minutes:.2f}:{seconds:.2f}"
    


def main():
    """
    Main function of the program
    
    get input from user
    seconds = float(input(""))
    
    convert seconds to hours, minutes, and seconds
    hours, minutes, seconds = convert_seconds(seconds)
    
    format time and print
    formatted_time = format_time(hours, minutes, seconds)
    """
def main():
    seconds = float(input("ВВЕДИТЕ ВРЕМЯ В СЕКУНДАХ: "))
    hours, minutes, seconds = convert_seconds(seconds)
    formatted_time = format_time(hours, minutes, seconds)
    print(formatted_time.__doc__)
    print(f"ВРЕМЯ В НОВОМ ФОРМАТЕ: {formatted_time}")

if __name__ == '__main__':
    main()
    
 