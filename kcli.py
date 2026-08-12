import subprocess
def K_CLI():
    running = True
    while running:
        input_cli = input("[K-CLI]> ")
        if " " in input_cli:
            try:
                input_cli = input_cli.split(" ")
                subprocess.run(input_cli)
                print("\n")
            except Exception as e:
                print("\n",e,"\n")
                continue
        elif input_cli == "exit":
            running = False
        
        else:
            try:
                subprocess.run([input_cli])
                print("\n")
            except Exception as e:
                print("\n",e,"\n")
                continue

