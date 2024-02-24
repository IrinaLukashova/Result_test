import Note

class Service:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []


    def load_notes(self):
        try:
            with open(self.filename, "r") as f:
                notes_json = f.read()
                self.notes = [Note.from_json(note_json) for note_json in notes_json.split("\n") if note_json]
        except FileNotFoundError:
            pass


    def save_notes(self):
        with open(self.filename, "w") as f:
            f.write("\n".join([note.to_json() for note in self.notes]))


    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()


    def get_note(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None


    def update_note(self, note):
        for i, n in enumerate(self.notes):
            if n.id == note.id:
                self.notes[i] = note
                self.save_notes()
                return
        raise ValueError("Note not found")


    def delete_note(self, id):
        for i, n in enumerate(self.notes):
            if n.id == id:
                del self.notes[i]
                self.save_notes()
                return
        raise ValueError("Note not found")
