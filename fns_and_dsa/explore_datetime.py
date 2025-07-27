from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    
    return current_date
display_current_datetime()
    
days = int(input("Enter the number of days to add to the current date: "))
current_date = datetime.today().date()

def calculate_future_date():
    delta = timedelta(days=days)
    future_date = delta + current_date
    future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")
    
    return future_date
calculate_future_date()
    
    