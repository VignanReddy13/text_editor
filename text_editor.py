class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def insert(self, new_text):
        self.undo_stack.append(self.text)  # save current state
        self.text += new_text
        self.redo_stack.clear()            # clear redo after new action

    def delete(self, count):
        self.undo_stack.append(self.text)
        self.text = self.text[:-count]
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:                # if there is something to undo
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:                # if there is something to redo
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def show(self):
        print("Current Text:", self.text)
editor = TextEditor()
editor.insert("Hello")
editor.show()        # Current Text: Hello

editor.insert(" World")
editor.show()        # Current Text: Hello World

editor.undo()
editor.show()        # Current Text: Hello

editor.redo()
editor.show()        # Current Text: Hello World

editor.delete(6)
editor.show()        # Current Text: Hello

editor.undo()
editor.show()        # Current Text: Hello World