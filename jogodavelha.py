matriz = [["", "", ""],["", "", ""],["", "", ""]]

co = 1
gameon = True
while gameon:
    
    vez = "x" if co % 2 == 1 else "o"
    turnx = int(input(f"your turn {vez}! position X: "))
    turny = int(input(f"your turn {vez}! position Y: "))
    if (turnx > 2) or (turny > 2):
        print("invalid position")
    else:
        if matriz[turnx][turny] == "":
            
            matriz[turnx][turny] = vez
        
            for c in range(len(matriz)):
                print(matriz[c])
                
            for i in range(len(matriz)):
                if matriz[i][0] == matriz[i][1] == matriz[i][2] == vez:
                    print(f"player {vez} wins!")
                    gameon = False
                if matriz[0][i] == matriz[1][i] == matriz[2][i] == vez:
                    print(f"player {vez} wins!")
                    gameon = False
                
                
                if "" not in (matriz[0] and matriz[1] and matriz[2]):
                    print("draw")
                    gameon = False
                    break
                
                co+=1
                        
        else:
            print('invalid')