from Organizer import Organizer

def main():
    organizer = Organizer(
        origin = './from',
        destination = './to',
        preserve_original_files = True,
        rename_files = True
        )
    organizer.run()

if __name__ == "__main__":
    main()