# Downloads Organiser

A Python program that automatically organises your Downloads folder by sorting files into folders based on their file extensions.

## Features

- **Automatic file sorting** – Categorises files into folders such as Documents, Images, Videos and Audio.
- **Dry-run preview** – Shows which files will be moved before making any changes.
- **User confirmation** – Requires confirmation before moving files.
- **Duplicate handling** – Prevents files from being overwritten by adding a number to duplicate filenames.
- **Customisable categories** – File extensions and their destination folders can be edited.

## Supported File Types

| Category | Extensions |
|---|---|
| Documents | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| Images | `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.avif`, `.jpe` |
| Installers & Compressed Files | `.exe`, `.msi`, `.zip` |
| Audio | `.mp3`, `.wav`, `.aif`, `.aiff`, `.flac`, `.m4a`, `.mid`, `.ogg` |
| Videos | `.mp4`, `.mov`, `.avi`, `.webm`, `.mkv`, `.wmv` |
| Mod Files | `.jar`, `.mrpack`, `.litematic`, `.schem` |

## Requirements

- Python 3
- No external libraries required (uses Python's standard library).

## How to Run

1. Clone or download this repository.
2. Make sure Python 3 is installed.
3. Run the program:

```bash
python main.py
```

The program will locate your Downloads folder automatically.

## Future Improvements

- Add support for more file extensions.
- Allow users to create their own categories.
- Add an undo feature.
- Improve error handling and logging.
