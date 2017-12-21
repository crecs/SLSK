### TASKS (FOR 1.2.0)

* Use QString on (almost) everything to remove duplicate type conversions to/fromStdString (yeah it's pretty much a mess down there)
* Make a better UI (not sure how but we'll get there)
* Clean up if backup process is manually cancelled

### BUGS

* MainMenu::CheckTotalSize(): Total size of operation is not completely accurate (may miss by a margin of a couple MB from what was tested)

### SUGGESTIONS

* Filter list - possible methods:
  * Fixed filters (by size, genre, publisher/developer, year, name, etc.) - would require changing database structure
* Find a way to optionally compress content (which format?)
* Prep up a CLI version if demand skyrockets
