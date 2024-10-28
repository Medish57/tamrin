def equation(x):
    return x**2 - 2  

def equation_derivative(x):
    return 2*x  

def find_root(initial_guess, epsilon, max_iter):
    current_guess = initial_guess
    for iteration in range(max_iter):
        deriv_value = equation_derivative(current_guess)
        
        if deriv_value == 0:
            raise ValueError("Moshtagh sefr ast, mohasebat motavaqef mishavad")
        
        next_guess = current_guess - equation(current_guess) / deriv_value
        
        print(f"Iteration {iteration + 1}: current_guess = {current_guess:.6f}, next_guess = {next_guess:.6f}, equation(current_guess) = {equation(current_guess):.6f}")
        
        if abs(next_guess - current_guess) < epsilon:
            return next_guess 
        
        current_guess = next_guess
    
    raise ValueError("Hadaksar tedad tekrarha be payan resid")
initial_estimate = 1.0
epsilon = 1e-7  
max_iterations = 100  

try:
    root_value = find_root(initial_estimate, epsilon, max_iterations)
    print(f"Rishe taqriban {root_value:.6f}")
    equation_value = equation(root_value)
    print(f"Maqdar-e tab'e dar rishe: {equation_value:.6f}")
    
    if abs(equation_value) < epsilon:
        print("Rishe sahih ast")
    else:
        print("Rishe momken ast sahih nabashad")
        
except ValueError as e:
    print(e)