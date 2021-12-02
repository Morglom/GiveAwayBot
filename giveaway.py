class giveaway:
    name
    description
    # Unix timestamp for giveaway time and date
    time
    participants
    # Whether the giveaway has been announced
    public
    # Whether a participant can win multiple rounds
    repeats
    
    def __init__(self, name, description, time, date, participants, public, repeats)
        self.name = name
        self.description
        self.time = time
        self.participants = participants
        self.public = public
        self.repeats = repeats
    