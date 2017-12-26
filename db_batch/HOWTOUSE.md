This is a quick 'n' dirty Python3 script I made for a more automated approach to inserting entries in the database, so there's no need to enter each one individually
(yeah I'm essentially sick of that too, takes a lot of time and gets boring pretty quick).

Here's how to do it:

1. Create a new text file called `input.txt` in the same folder as the script is (wherever you decided to put it)
2. Open `TEMPLATE.txt` and copy-paste as much entries as you'd like
3. Add your entries normally, following the template (filling ALL fields as usual)
4. **Separate entries by a line break** (VERY important)
5. When you're done, **if there are any entry fields left unused, delete 'em** (also VERY important)
6. Save it and run the script -> `python3 convert.py`

This way, three files will be generated: `db_output.csv`, `log_output.txt` and `list_output.txt`. You can import `db_output.csv` to a separate spreadsheet so you
can copy-paste the cells directly to the database, `log_output.txt` will format all your entries for the CHANGELOG as well and `list_output.txt` will format all
your entries for the MISSINGLIST (just make sure to do the usual polish, like stated in [CONTRIBUTING.md](../CONTRIBUTING.md)).

Using this is completely optional, but I'm sure it will be of use for many of us ;)
