# ITIA 1510 Week 07: Software Allowlist Audit

Individual assignment. Topic: **reading and writing files**, from Week 07, and
everything before it. No regular expressions.

The IT department keeps a list of the programs it allows on lab computers.
Your program reads that list and a list of the programs found on each
computer. It finds the programs that are not allowed, saves a report to a
file, and adds one line to a history file every time it runs.

Open `allowlist_audit.py` and work through the 19 numbered TODOs in order.
Each one is a few lines. One function is finished and wrong, and fixing it is
part of the job.

Every function has type hints, such as `list[str]` and `-> bool`. They need
Python 3.9 or newer. Check with `python --version`.

## The files

| File            | What is in it                                                        |
|-----------------|----------------------------------------------------------------------|
| `approved.txt`  | One approved program per line. Skip blank lines and lines that start with `#`. |
| `inventory.txt` | One line per program found: `computer,program`. Skip blank lines. Skip and count any line that does not have exactly two parts. |
| `report.txt`    | Made by your program. Replaced every run.                            |
| `history.log`   | Made by your program. One line added every run.                      |

The status is **PASS** when 90% or more of the programs are approved,
**WARNING** at 75% or more, and **FAIL** below 75%.

## Get your own copy

1. On this repository's GitHub page, click **Use this template**, then
   **Create a new repository**.
2. Set **Owner** to your own account and name the repository
   `ITIA1510-Software-Allowlist-Audit`. Choose **Public**, then click
   **Create repository**.
3. Clone your new repository, not this one:

   ```
   git clone <your repository url>
   cd ITIA1510-Software-Allowlist-Audit
   ```

## Do the work on a branch

Do all of the git work with git commands from the command line. Do not edit,
upload or merge files in the GitHub web interface.

4. Create the branch before you change anything:

   ```
   git checkout -b week07-software-allowlist-audit
   ```

5. Write the code. Commit as you go:

   ```
   git add allowlist_audit.py
   git commit -m "Describe what you just finished"
   ```

6. Push the branch:

   ```
   git push -u origin week07-software-allowlist-audit
   ```

## Demonstrate, then merge

7. **Demonstrate the program to your instructor** from the branch you just
   pushed. The demonstration is required: it is worth half the grade, and an
   assignment that is never demonstrated earns no points.
8. After the demonstration, merge into main and push:

   ```
   git checkout main
   git merge week07-software-allowlist-audit
   git push origin main
   ```

9. Submit the link to your repository in Canvas.

If it is not finished at 8:55 PM, keep working, or demonstrate what you have,
then commit, push, merge and submit it for partial credit.

## Check your work

Run the program from this folder, so it can find the two text files. With the
files in this repository, a finished program gives these answers.

| Question               | Answer                                               |
|------------------------|------------------------------------------------------|
| Approved programs      | 9                                                    |
| Inventory records      | 18                                                   |
| Lines skipped          | 1                                                    |
| Programs not approved  | 7                                                    |
| Fix first              | lab-03, lab-06                                       |
| Programs to remove     | CCleaner, Steam, TeamViewer, Tor Browser, uTorrent   |
| Approved               | 61.1%                                                |
| Status                 | FAIL                                                 |

Run it a second time. `report.txt` should look the same as after the first
run. The last line should say `Runs recorded: 2`.

The tests in `test_allowlist_audit.py` cover TODO 1 through TODO 13. Run them
from this folder:

```
python -m unittest test_allowlist_audit -v
```

22 of the 29 fail before you start, and all 29 pass when those functions are
right. The report TODOs, 14 through 19, are checked against the table above.
