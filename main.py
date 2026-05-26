import subprocess

def main():
    choice = input("Type 1 for 'train' or 2 for 'predict': ")

    if choice == "1":
        subprocess.run(["python", "-m", "model.train"])

    elif choice == "2":
        subprocess.run(["python", "-m", "inference.predict"])

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()