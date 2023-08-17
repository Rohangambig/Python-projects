class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NotesApp:
    def __init__(self):
        self.notes = []

    def create_note(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        note = Note(title, content)
        self.notes.append(note)
        print("Note created successfully.")

    def list_notes(self):
        if not self.notes:
            print("No notes.")
            return

        print("Notes:")
        for idx, note in enumerate(self.notes, start=1):
            print(f"{idx}. {note.title}")

    def view_note(self, index):
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            print(f"Title: {note.title}\nContent: {note.content}")
        else:
            print("Invalid note index.")

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            print("Note deleted.")
        else:
            print("Invalid note index.")

def main():
    notes_app = NotesApp()

    while True:
        print("\nNotes App")
        print("1. Create Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            notes_app.create_note()
        elif choice == "2":
            notes_app.list_notes()
        elif choice == "3":
            index = int(input("Enter note index to view: "))
            notes_app.view_note(index)
        elif choice == "4":
            index = int(input("Enter note index to delete: "))
            notes_app.delete_note(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
