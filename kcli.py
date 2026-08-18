import subprocess
import datetime
def K_CLI(name):
    time = datetime.datetime.now()
    
    running = True
    while running:
        pwd = subprocess.check_output("pwd",text=True)
        input_cli = input(f'''╭─[User-{name}]─[{time:%Hh-%Mm-%Ss}]
├─[{pwd}]
╰─❯''')
        if " " in input_cli:
            try:
                input_cli = input_cli.split(" ")
                subprocess.run(input_cli)
                
            except Exception as e:
                print("\n",e,"\n")
                continue
        elif input_cli == "exit":
            running = False
            break
        
        else:
            try:
                subprocess.run([input_cli])
                
            except Exception as e:
                print("\n",e,"\n")
                continue

if __name__ == "__main__":
    K_CLI("kk")