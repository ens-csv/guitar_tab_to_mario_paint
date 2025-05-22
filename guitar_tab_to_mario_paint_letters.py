# guitar_tab_to_mario_paint_letters.py

NOTE_TO_MARIO = {
    'C5': 'a', 'B4': 'b', 'A4': 'c', 'G4': 'd',
    'F4': 'e', 'E4': 'f', 'D4': 'g', 'C4': 'h',
    'B3': 'i', 'A3': 'j', 'G3': 'k', 'F3': 'l',
    'E3': 'm', 'D3': 'n', 'C3': 'o'
}

NOTE_ORDER = ['C', 'C#', 'D', 'D#', 'E', 'F',
              'F#', 'G', 'G#', 'A', 'A#', 'B']

STRING_TUNING = {
    'e': 'E4',
    'B': 'B3',
    'G': 'G3',
    'D': 'D3',
    'A': 'A2',
    'E': 'E2',
}

def note_from_string_fret(tuning_note, fret):
    base_note = tuning_note[:-1]
    base_octave = int(tuning_note[-1])
    semitone_offset = NOTE_ORDER.index(base_note) + fret
    note_name = NOTE_ORDER[semitone_offset % 12]
    octave = base_octave + (semitone_offset // 12)
    return f"{note_name}{octave}"

def parse_tab(tab_lines):
    lines = [line.strip() for line in tab_lines if '|' in line]
    string_notes = {}
    for line in lines:
        string_id = line[0]
        content = line[2:]  # Skip string name and '|'
        string_notes[string_id] = list(content)

    max_len = max(len(v) for v in string_notes.values())
    events = []

    i = 0
    while i < max_len:
        for string, notes in string_notes.items():
            if i >= len(notes):
                continue
            char = notes[i]
            if char.isdigit():
                # Check for multi-digit fret numbers
                next_char = notes[i+1] if i+1 < len(notes) else ''
                if next_char.isdigit():
                    fret = int(char + next_char)
                    notes[i+1] = ''  # Consume the second digit
                else:
                    fret = int(char)
                full_note = note_from_string_fret(STRING_TUNING[string], fret)
                letter = NOTE_TO_MARIO.get(full_note)
                if letter:
                    events.append((i, letter))
                else:
                    print(f"Note {full_note} not in Mario Paint range")
        i += 1
    return sorted(events)

def print_events(events):
    for time, note in events:
        print(f"Time {time}: {note}")

# Example usage
if __name__ == "__main__":
    tab = [
        "e|------------------|",
        "B|------------------|",
        "G|--4--5--7---------|",
        "D|------------------|",
        "A|------------------|",
        "E|------------------|"
    ]
    events = parse_tab(tab)
    print_events(events)
