class todo:
    id: int
    title: str
    description: str

    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description