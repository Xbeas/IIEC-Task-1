import os
import pyttsx3 as py


# This function will create a dictionary of start menu items with a key values.
#
def path_to_programs():
    root = [r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
            os.path.expandvars("%userprofile%") + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"]

    plist = {}
    for r in root:
        for path, subdirs, files in os.walk(r):
            for name in files:
                l = os.path.join(path, name)
                a = l.split("\\")
                i = a.index("Programs") + 1
                if "uninstall" in a[-1].split(".")[0].lower() or "help" in a[-1].split(".")[
                    # To filter out useless commands.
                    0].lower() or "documentation" in a[-1].split(".")[0].lower() or "url" in a[-1].split(".")[1]:
                    continue
                else:
                    if os.path.isfile("\\".join(a[:i + 1])):
                        b = {a[i].split(".")[0].lower(): l}
                    else:
                        if a[i].lower() not in b:
                            b = {a[i].lower(): {}}
                        b[a[i].lower()].update({a[-1].split(".")[0].lower(): l})

                plist.update(b)
    return plist


plist = path_to_programs()
keystr = list(plist.keys())

py.speak("Launching Project\n\n Please Tell me Your Name:")
u = input("\n[+]Input: ")
py.speak("Hello " + u + "! How Can i help You?")
print("You can print the Program names using input: print supported programs")
py.speak("You can print the Program names using input: print supported programs")
while True:

    u = input("\n[+]Input: ").lower()
    if "open" in u or "execute" in u or "run" in u or "launch" in u or "start" in u:
        if "notepad" in u or "editor" in u:
            py.speak("Opening Notepad")
            os.system("notepad")

        elif "chrome" in u or "browser" in u or "google" in u:
            py.speak("Opening Chrome")
            os.startfile(plist['google chrome'])

        else:
            c=0
            for k in keystr:
                if k in u:
                    if type(plist[k]) == dict:
                        tmp = list(plist[k].keys())
                        if len(tmp) == 1:
                            py.speak("Opening" + str(tmp[0]))
                            os.startfile(plist[k][tmp[0]])
                            c=1
                        else:
                            py.speak(
                                "There are " + str(len(tmp)) + "options available for" + k + ", Please choose one:")
                            while True:
                                for t in range(0, len(tmp)):
                                    py.speak(str(t + 1) + " for " + tmp[t])

                                t1 = int(input("\n[+]Input( press 0 to back): "))
                                if t1 == 0:
                                    break
                                elif t1 - 1 in range(0, len(tmp)):
                                    py.speak("Opening" + str(tmp[t1 - 1]))
                                    os.startfile(plist[k][tmp[t1 - 1]])
                                    c=1
                                else:
                                    py.speak("I don't get it, Try again")
                    else:
                        py.speak("Opening"+k)
                        os.startfile(plist[k])
                        c=1
            if c == 0:
                py.speak("I don't get the program, Can you Please Repeat.")
                continue
        py.speak("Anything Else?")

    elif "exit" in u or "close" in u or "bye" in u or "no" in u:
        py.speak("Have a Good day.")
        exit()
    elif "print supported programs" in u:
        print("\n[+]Supported:\n")
        for k in keystr:
            print(k)
        py.speak("I can help with these programs. Please give a input")
        continue
    else:
        py.speak("I don't get it, Can you Please Repeat.")
