import turtle

def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)

    if state == "INIT":
        state = "DOWN"
        t.setheading(270)  # Разворот вниз
        return state, turn
        
    if state == "DOWN":
        t.forward(10)
        if y <= -4:  
            state = "RIGHT"
            t.setheading(0)  
        return state, turn
        
    if state == "RIGHT":
        t.forward(10)
        if x >= turn * 3:  
            state = "UP"
            t.setheading(90)  # Разворот вверх
        return state, turn
        
    if state == "UP":
        t.forward(10)
        if y >= 0:
            state = "RIGHT2"  
            t.setheading(0)
        return state, turn
        
    if state == "RIGHT2":
        t.forward(10)
        if x >= turn * 3 + 2:
            state = "DOWN"
            t.setheading(270)  # Разворот вниз
            turn += 1  # Начало нового витка
        return state, turn
        
    if state == "STOP":
        return state, turn
        
    return state, turn

def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(8)
    turn = 1

    
    max_turns = 25  
    
    for _ in range(max_turns * 4):
        curr_state, turn = perform_switch_case(curr_state, t, turn)
        if turn > max_turns:
            break
            
    turtle.done()

if __name__ == "__main__":
    draw()
