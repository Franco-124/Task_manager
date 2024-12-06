import logging

def log_function_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling the function {func.__name__} with arguments {args}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        
        return result
    return wrapper

