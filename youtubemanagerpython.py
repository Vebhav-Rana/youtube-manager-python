import json

FILENAME = "youtubeself.txt"


def load_videos():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_videos(videos):
    with open(FILENAME, "w") as file:
        json.dump(videos, file, indent=4)


def list_all_videos(videos):
    if videos:
        print("-" * 50)
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']} | {video['duration']} | {video['author']}")
        print("-" * 50)
    else:
        print("No videos available.")


def add_video(videos):
    name = input("Enter video name: ")
    duration = input("Enter video duration: ")
    author = input("Enter video author: ")

    videos.append({
        "name": name,
        "duration": duration,
        "author": author
    })

    save_videos(videos)
    print("Video added successfully.")


def delete_video(videos):
    if not videos:
        print("No videos to delete.")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the index of the video to delete: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_videos(videos)
            print("Video deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def update_video(videos):
    if not videos:
        print("No videos to update.")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the index of the video to update: "))
        if 1 <= index <= len(videos):
            new_name = input("Enter new video name: ")
            new_duration = input("Enter new video duration: ")
            new_author = input("Enter new video author: ")

            videos[index - 1] = {
                "name": new_name,
                "duration": new_duration,
                "author": new_author
            }

            save_videos(videos)
            print("Video updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    videos = load_videos()

    while True:
        print("\nChoose an option:")
        print("1. Add a video")
        print("2. Delete a video")
        print("3. Update a video")
        print("4. List all videos")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                add_video(videos)
            case 2:
                delete_video(videos)
            case 3:
                update_video(videos)
            case 4:
                list_all_videos(videos)
            case 5:
                print("Exiting program...")
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
