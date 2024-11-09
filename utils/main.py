import utils
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Select a file in the file explorer.")
        utils.main()
        sys.exit(1)

    elif (sys.argv[1] == ""):
        print("Select a file in the file explorer.")
        utils.main()
        sys.exit(1)

    else:
        file_path = sys.argv[1]
        print(f"Processing file: {file_path}")
        utils.main(file_path)