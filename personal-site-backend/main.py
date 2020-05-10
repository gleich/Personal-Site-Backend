import firestore


def main():
    """Main method for the program
    """
    database = firestore.connectToDatabase()


if __name__ == "__main__":
    main()
