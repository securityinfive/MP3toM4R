from pydub import AudioSegment
import os

def convertringtone(mp3_folder, convert_root):
    # Create ringtone folder if it doesn't exist
    os.makedirs(convert_root, exist_ok=True)
    convert_path = os.path.join(mp3_folder, convert_root)

    for filename in os.listdir(mp3_folder):
        if filename.lower().endswith('.mp3'):
            audio = AudioSegment.from_mp3(filename)
            
            # Trim to 40 seconds (iOS ringtone limit)
            max_duration_ms = 40 * 1000
            if len(audio) > max_duration_ms:
                audio = audio[:max_duration_ms]
                print("✂️ Trimmed to 40 seconds.")

            # Define output filename
            m4r_filename = os.path.splitext(os.path.basename(filename))[0] + ".m4r"
            m4r_path = os.path.join(convert_path, m4r_filename)

            # Export as M4R (AAC codec, with .m4r extension)
            audio.export(m4r_path, format="mp4", codec="aac")

            print(f"✅ Ringtone saved as: {m4r_path}")

# Start
current_dir = os.getcwd()
ringtone_dir = 'ringtones'            # Where to place ringtones

convertringtone(current_dir, ringtone_dir)