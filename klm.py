version = 0.3

import importlib
from kcli import K_CLI

needed_pkgs = ['time','random' ,'shutil' ,'os' ,'yt_dlp' , 'qrcode', 'shutil','requests' , 'datetime', 'functools', 'urllib' , 'subprocess']
not_installed_pkgs =[]

for id,pkg in enumerate(needed_pkgs):
    try:
        globals()[pkg] = importlib.import_module(pkg)
    except:
        not_installed_pkgs.append(pkg)
        pass
        
from functools import lru_cache


def asc_bw():
    binary = input("Enter binary:> ").split()

    text = ""
    for b in binary:
        text += chr(int(b, 2))

    return "KLM: The converted text is--> ", text
    

def asc_wb():
    text = input("Enter text:> ")

    binary = ""
    for char in text:
        binary += format(ord(char), '08b') + " "

    return "KLM: The binary form of this text is--> ", binary

async def sub_install_pkgs(needed_list):
    l = subprocess.check_output(["python","-m","pip","list"],text=True)
    
    needed_pkgs = str(needed_list)
    if needed_pkgs in l:
        slow("KLM: You already have all the packages installed!")
    else:
        slow(f"KLM: The following packages are not installed -> {not_installed_pkgs}\nKLM: Would you like to install those packages? (Y/n)")
        inputt = input('> ')
        while True:
            if inputt == "y":
                try:
                    for pkg in not_installed_pkgs:
                        subprocess.run(["pip3","install",f"{pkg}"])
                    slow(f"KLM: Sucessfully Installed {pkg}!")
                except Exception as e:
                    slow(f"KLM: Coudn't install the packages for some reason.\n{e}")
                    break
                break
            elif inputt == "n":
                slow(f"KLM: These packages are not going to be installed {not_installed_pkgs}")
                break
            else:
                slow("KLM: The input is invalid!\nKLM: Please input y for yes and n for no")
            break
            
    

def toss():
    ts = random.randint(1,2)
    if ts == 1:
        return "KLM: Its, Heads!"
    else:
        return "KLM: Its, Tails!"
    
@lru_cache
def datec():
    return f"KLM: Today is {datetime.date.today()}"
    
def timet():
      dt = datetime.datetime.now()
      l = str(dt)
      r = l.split(" " and ".")
      t = str(r)
      tr = t.split(" ")
      return tr[1]


rand = random.randint(1, 5)
def ow(t):
    for c in t:
        print(c, end="", flush=True)
        time.sleep(0.08)
    print()
def slow(t):
    for c in t:
        print(c, end="", flush=True)
        time.sleep(0.03)
    print()

commands = {'/date':datec , '/toss':toss,'/time':timet,'/w_t_b':asc_wb,'/b_t_w':asc_bw,'/cli':K_CLI}

print('''
██╗  ██╗██╗      ███╗   ███╗
██║ ██╔╝██║      ████╗ ████║
█████╔╝ ██║      ██╔████╔██║
██╔═██╗ ██║      ██║╚██╔╝██║
██║  ██╗███████  ██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝ ╚═╝     ╚═╝
''')
ow(f"Welcome to KLM -ai{version}")
print("starting.......")
time.sleep(2)
slow(f"\nKLM: Hi! i am an ai assistant KLM {version} made by Kash.")

os.makedirs("mem", exist_ok=True)

l = subprocess.check_output(["ls","mem"],text=True)
print(l)

if "api_key.txt" in l:
    f = open("mem/api_key.txt","r")
    AI_API_KEY = f.read()
    f.close()
if "api_key.txt" not in l:
    f = open("mem/api_key.txt","w")
    AI_API_KEY = input("Enter your pollinations api key: ")
    f.write(AI_API_KEY)
    f.close()
if "ai_model.txt" in l:
    with open("mem/ai_model.txt" , 'r') as f:
        AI_MODEL = f.read()
if "ai_model.txt" not in l:
    with open("mem/ai_model.txt" , 'w') as f:
        f.write(input("Enter the model you are going to use with the api key: "))

if "user_name.txt" in l and "api_key.txt" in l:
     f = open(f'mem/user_name.txt' , 'r')
     user_name = f.read()
     slow(f"KLM: Welcome! {user_name}")
     if rand == 3:
         slow(f"KLM: I am your personal assistant.(KLM-{version})")
     if rand == 1:
       slow(f"What do you want to do today?(type 'help' if dont know what to do.)")
     if rand == 2:
         slow("Want to do something fun today?(type help ;))")
     if rand == 4:
         slow("KLM: Hoping you are having a good day!")
     if rand == 5:
         slow("KLM: Tell me if you are bored we can play games together!")
     while True:
         ip = input("> ").lower()
         if ip == "help":
             print("type /date for getting date.\n/toss for a coin toss\n/sum for sum \n/clear_data for clearing ai data\n/time for time\n/calculate_death to calculate a fake death counter\n/w_t_b for word to binary conversion\n/b_t_w for binary to word or ASCII conversion\n/ytd for downloading videos from YouTube\n/gen_qr for generating a qr code from the given url \n/install_deps to install all dependencies\n/cli for a command line interface named k-cli\nMore coming soon in next update...")
         elif ip == "/clear_data":
             
             shutil.rmtree("mem")
             print("Program finished.")
             break
         elif ip in commands:
             slow(commands[ip]())
             
         elif ip == "/install_deps":
             install_pkgs(needed_pkgs)
           
         elif ip == "/gen_qr":
             
             url = input("Enter url: ").strip()
             file_path = input("Please enter file path for saving the qr code: ")
             qr = qrcode.QRCode()
             qr.add_data(url)
             img = qr.make_image()
             img.save(file_path)

         elif ip == "/sum":
             sumip = (input())
             slow(f"KLM: The answer is {eval(sumip)}")
         elif ip =="_cv":
             slow(f"KLM: my current version is {version}")
         elif ip == "/calculate_death":
             print("KLM: Rough estimate says you will die in " , random.randint(0,100), "years.")
         elif ip == "exit" or ip == "Exit" or ip == "exit()" or ip == "Exit()":
             slow("KLM: Byee 👋!")
             break
         elif ip == "What is your name" or ip == "what is your name" or ip == "What is your name?" or ip == "who are you?" or ip == "who are you" or ip == "what is your name?":
             slow("KLM: My name is KLM. 'KLM' stands for Kash's Language Model.")
         
         elif ip == "hi" or ip == "Hi" or ip == "hi!" or ip == "Hi!":
                 hiran = random.randint(1,5)
                 if hiran == 1:
                     slow(f"KLM: Hello! 👋 {user_name}")
                 elif hiran == 2:
                     slow(f"KLM: Hi!")
                 elif hiran == 3:
                     slow(f"KLM: Hi there {user_name}")
                 elif hiran == 4:
                     slow(f"KLM: Yoo what's up {user_name}")
                 elif hiran == 5:
                     slow("KLM: Hello! I am here with you at any time you want!")
         
         elif ip == "/ytd":
             
             
             download_path = "Download"

             url = input("KLM: Enter video URL--\n> ")

             def progress_hook(d):
                 if d['status'] == 'downloading':
                     print(f"\rDownloading... {d.get('_percent_str','')} at {d.get('_speed_str','')}", end="")
                 elif d['status'] == 'finished':
                     print("\nDownload completed!")

             ydl_opts = {
                  'format': 'best[height<=360]/best',  # ✅ no merging needed
                 'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                 'progress_hooks': [progress_hook],
}

             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                 ydl.download([url])
         elif ip == "lets play some games" or ip == "games" or ip == "play games" or ip == "lets play" or ip == "play" or ip == "lets play games" or ip == "lets games":
             slow("KLM: Sounds exellent! what kinds of games do you want to play? I know how to play rock paper scissor!\nKLM: rock , paper , scissor .... shoot!(Ten rounds)")
             from stone import rcp
             
             rocpapsci = 0
             klmrcpscore = 0
             userrcpscore = 0
             for rocpapsci in range(10):
                 rockpaperscip = rcp()
                 rocpapsci = rocpapsci + 1
                 
                 if rockpaperscip == "win":
                     userrcpscore += 1
                 if rockpaperscip == "tie":
                     pass
                 if rockpaperscip == "lose":
                     klmrcpscore += 1
                 print(f"score is {klmrcpscore}:{userrcpscore}")
             print("Match ended.")
         else:
                 
                 from urllib.parse import quote as qte
                 try:
                     prom = ip
                     prompt = qte(prom)
                     
                     ai = requests.get(f"https://gen.pollinations.ai/text/{prompt}?key={AI_API_KEY}&model={AI_MODEL}")
                     print(f"KLM: {ai.text}")
                     with open('mem/memory.txt','w') as f:
                         if type(ai.text) == type({}):
                             pass
                         else:
                             f.write(ai.text)
                 
                 except Exception as e:
                     slow(f"KLM: oops! Some error occurred!-->\n\n{e}")
             
else:
    slow("KLM: What is your name?")
    an = input("> ")
    with open('user_name.txt', 'w') as f:
        f.write(f'{an}')
    
    os.makedirs("mem", exist_ok=True)
    shutil.move("user_name.txt", f"mem/user_name.txt")
    print(f"(saved to memory)\nReopen KLM{version}")
