from factories.folder_factory import FolderFactory
from factories.image_factory import ImageFactory
from factories.organizer_factory import OrganizerFactory


def main():
    image_factory = ImageFactory()
    folder_factory = FolderFactory(image_factory)
    organizer_factory = OrganizerFactory(folder_factory)

    organizer = organizer_factory.create("./example-of-origin-folder", "./example-of-destination-folder", True, True)
    organizer.run()

    print("Done!")


if __name__ == "__main__":
    main()
