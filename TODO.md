### TASKS

* Use QString on (almost) everything to remove duplicate type conversions to/fromStdString (yeah it's pretty much a mess down there)

### BUGS

* MainMenu::CheckTotalSize(): Total size of operation is not completely accurate (may miss by a margin of a couple MB from what was tested)

### SUGGESTIONS

* Filter list - possible methods:
  * Using Steam's own library categories (libraryfolders.vdf) - easier, no changing in database, but not sure if it's possible
  * Fixed filters (by size, genre, publisher/developer, year, name, etc.) - would require changing database structure
* Clean up if backup process is manually cancelled (restore might be way more complicated)
* Find a way to optionally compress content (which format?)
* Prep up a CLI version if demand skyrockets
