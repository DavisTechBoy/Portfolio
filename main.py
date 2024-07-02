import subprocess as sb

tasks = []

def main():
    print('TO - DO - A way to keep track of your life')
    print('1. ADD TASK | 2. Show Task | 3. Remove Task | 4.EXIT')
    while True:
        try:
            choice = input('Enter Your Choice: ')
        
            if choice == '1':
                tsk = input('Enter Your Task: ')
                tasks.append(tsk)

            elif choice == '2':
                for i in tasks:
                    print(i)
            elif choice == '3':
                print(tasks)
                h = input('Task: ')
                tasks.remove(h)
            elif choice == '4':
                print('Thank You')
                break
             
        except(ValueError):
            print('Invalid Input')
            pass






main()