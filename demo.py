from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file and a track
midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)

# Set tempo (85 BPM)
tempo = 60000000 // 85  # Microseconds per beat
track.append(Message('meta', type='set_tempo', tempo=tempo))

# Function to add a note
def add_note(track, note, start_time, duration, velocity=64, channel=0):
    track.append(Message('note_on', note=note, velocity=velocity, time=start_time, channel=channel))
    track.append(Message('note_off', note=note, velocity=0, time=duration, channel=channel))

# Generate atmospheric, sci-fi, ambient tones
time = 0
for i in range(0, 180, 6):  # Spread notes over 3 minutes (180 seconds)
    # Add deep bass tones
    add_note(track, note=36, start_time=time, duration=480, velocity=50)  # C2
    # Add mid-range melodic tones
    add_note(track, note=60 + (i % 12), start_time=240, duration=480, velocity=70)  # C4 and variations
    # Add high shimmering tones
    if i % 12 == 0:
        add_note(track, note=72 + (i % 5), start_time=240, duration=960, velocity=40)  # C5 variations
    time += 960

# Save the file
midi_path = '/mnt/data/Ambient_SciFi_Cinematic_85bpm.mid'
midi_file.save(midi_path)
midi_path
