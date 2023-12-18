from typing import Any, Callable
from functools import wraps
from time import perf_counter


"""DECORATOR FACTORIES OR PARAMETERIZED DECORATORS"""


def function_timer(num_of_reps: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:  # Returns a decorator
    """Decorator factory"""
    def _function_timer(a_func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Decorator function. Returns a closure that, when called,
        will print on the screen the function call representation
        and the time it took to run.
        """
        @wraps(a_func)
        def inner(*args, **kwargs) -> Any:
            # Start with zero time and with a result pointing to None
            total_elapsed: float = 0
            result: Any = None

            # Loop n times (n is free variable passed to function_timer)
            for i in range(num_of_reps):
                start: float = perf_counter()
                # Store the return from the wrapped function
                result = a_func(*args, **kwargs)
                # Add the elapsed time to the total_elapsed free variable
                total_elapsed += perf_counter() - start

            # Calculating the average time
            avg_elapsed_time: float = total_elapsed / 10

            # Capture args and kwargs in a string
            _args: list[str] = list(args)
            _args.extend([f"{k}={v}" for k, v in kwargs.items()])
            _args_description = str(args)
            func_call_str = f"{a_func.__name__}{_args_description}"

            # Print calling information
            print(f"{func_call_str} ran {num_of_reps} times")
            print(f"{func_call_str} took in average {avg_elapsed_time:.6f}s")

            # Return result from calling wrapped function
            return result

        # Returning decorated function
        return inner

    # Returning decorator function
    return _function_timer


@function_timer(10000000)  # Same as => add = function_timer(10000)(add)
def add(x: int, y: int) -> int:
    return x + y


print(add.__code__.co_freevars)  
# 'a_func', 'num_of_reps')
print(add.__closure__)  
# (<cell to function>, <cell to int>)
add(10, 20)
# add(10, 20) ran 100000 times
# add(10, 20) took in average 0.011496s
