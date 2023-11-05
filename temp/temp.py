# Define a Result type
enum Result<T, E> {
    Ok(T),
    Err(E),
}

# Example pure functions
function divide(x, y):
    if y == 0:
        return Err("Division by zero")
    return Ok(x / y)

function squareRoot(x):
    if x < 0:
        return Err("Negative number")
    return Ok(Math.sqrt(x))

# Using Result pattern
let result1 = divide(10, 5)
let result2 = divide(10, 0)

let finalResult = result1
    .map(squareRoot)
    .map(value => value * 2)
    .map(value => value + 1)

# Handle the final result
match finalResult {
    case Ok(value):
        print("Result: " + value)
    case Err(error):
        print("Error: " + error)
}
