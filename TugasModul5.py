while True:
    n = int(input("input banyak data n : "))
    x_values = []
    fx_values = []
    gx_values = []
    hx_values = []

    for i in range (n):
        x = float(input(f"input x ke-{i+1} : "))
        x_values.append(x)

        if x==0:
            fx = 0
        elif x>0:
            fx = 4*x**3+7*x-5
        else:
            fx = 3*x**2-5*x+1
        fx_values.append(fx)

        gx = fx**2-fx
        gx_values.append(gx)

        hx = fx*gx
        hx_values.append(hx)

    print("\nOutput : ")
    print(f"{'No':<5}{'x':<10}{'f(x)':<15}{'g(x)':<15}{'h(x)':<15}")
    for i in range(n):
        print(f"{i+1:<5}{x_values[i]:<10}{fx_values[i]:<15}{gx_values[i]:<15}{hx_values[i]:<15}")
    
    lagi = input("\nInput nilai x lagi Y/N? ").upper()
    if lagi != 'Y':
        break