"""
Week 08 INDIVIDUAL ASSIGNMENT -- Software Allowlist Audit
ITIA 1510 Cybersecurity Automation

Topic: reading and writing files, from Week 08, and everything before it.
No regular expressions.

The IT department keeps a list of approved programs. This program reads that
list and a list of the programs found on each lab computer. It finds every
program that is not approved, writes a report file, and adds one line to a
history file each time it runs.

THE FILES
   approved.txt    one approved program per line. Skip blank lines and
                   lines that start with #.
   inventory.txt   one line per program found: computer,program
                   Skip blank lines. Skip a line that does not have exactly
                   two parts, and count it.
   report.txt      written by this program. Replaced every run.
   history.log     written by this program. One line added every run.

THE STATUS
   PASS when 90% or more of the programs are approved, WARNING at 75% or
   more, FAIL below 75%.

Work through the 19 numbered TODOs in order. Each one is a few lines. One
function is finished and wrong, and fixing it is part of the job.

Every function shows its types. In
   def is_approved(program: str, approved: list[str]) -> bool:
program is a string, approved is a list of strings, and the function
returns True or False. Python does not check the types. They are there for
the person reading the code. They need Python 3.9 or newer.

Run the file before changing anything. It runs without an error, but it
prints nothing yet. The report is printed in TODO 18.
"""

APPROVED_FILE = "approved.txt"
INVENTORY_FILE = "inventory.txt"
REPORT_FILE = "report.txt"
HISTORY_FILE = "history.log"

# A computer with this many programs that are not approved, or more, is fixed first.
FIX_FIRST_LIMIT = 2


# ---------------------------------------------------------------------------
# Part 1: reading the files
# ---------------------------------------------------------------------------

def load_approved(path: str) -> list[str]:
    """Return a list of the approved programs in the file."""
    # TODO 1
    #   Start with an empty list. Open the file with:
    #      with open(path, "r") as f:
    #   Loop over f. Call strip() on each line. Skip a line that is empty
    #   or starts with "#". Append the rest. Return the list.
    return []


def load_inventory(path: str) -> list[dict]:
    """Return a list of dictionaries, one per program found, with the keys
    host and program."""
    # TODO 2
    #   Start with an empty list. Open the file with a with statement and
    #   loop over it. strip() each line. Skip the empty lines.
    #
    # TODO 3
    #   split(",") the line into parts. If there are not exactly 2 parts,
    #   skip the line. Otherwise append {"host": parts[0], "program": parts[1]}.
    return []


def count_bad_lines(path: str) -> int:
    """Return how many lines are not empty and do not have exactly 2 parts."""
    # TODO 4
    #   Read the file the same way as TODO 2. Count the lines that are not
    #   empty and do not split into exactly 2 parts.
    return 0


# ---------------------------------------------------------------------------
# Part 2: checking the programs
# ---------------------------------------------------------------------------

def is_approved(program: str, approved: list[str]) -> bool:
    """True when the program is on the approved list."""
    # TODO 5
    #   One line. Use the in operator.
    return False


def find_unapproved(inventory: list[dict], approved: list[str]) -> list[dict]:
    """Return the records whose program is not approved, in the same order."""
    # TODO 6
    #   Start with an empty list. Loop over inventory. Append every record
    #   whose program is not approved. Use is_approved().
    return []


def count_by_host(records: list[dict]) -> dict[str, int]:
    """Return a dictionary: each computer and how many records it has."""
    # TODO 7
    #   Start with an empty dictionary. For each record, add 1 to the count
    #   for its host. Use get() with a default of 0.
    return {}


def hosts_at_or_above(counts: dict[str, int], limit: int) -> list[str]:
    """Return a sorted list of the computers whose count is limit or more."""
    # TODO 8
    #   Loop over counts.items(). Keep each host whose count is limit or
    #   more. Exactly limit counts. Return the list sorted.
    return []


def unique_programs(records: list[dict]) -> list[str]:
    """Return a sorted list of the programs, each one only once."""
    # TODO 9
    #   Start with an empty list. For each record, append its program only
    #   if it is not in the list yet. Return the list sorted.
    return []


def percent_approved(total: int, not_approved: int) -> float:
    """Return the approved programs as a percent of total, rounded to 1 place."""
    # TODO 10
    #   If total is 0, return 0.0, because you cannot divide by 0.
    #   Otherwise it is (total - not_approved) / total * 100, rounded to
    #   1 decimal place with round().
    return 0.0


def audit_status(percent: float) -> str:
    """Return 'PASS' at 90 or more, 'WARNING' at 75 or more, 'FAIL' below 75."""
    # TODO 11
    #   if / elif / else. Test the highest number first.
    return "UNKNOWN"


# ---------------------------------------------------------------------------
# Part 3: writing the files
# ---------------------------------------------------------------------------

def write_report(path: str, lines: list[str]) -> None:
    """Write each string in lines to the file as one line. Replace what was there."""
    # TODO 12
    #   Open path in write mode, "w", with a with statement. Loop over lines
    #   and write each one. write() does not add a new line, so add "\n".
    pass


def append_history(path: str, line: str) -> None:
    """Add one line to the end of the history file. Keep what was there."""
    # TODO 13 -- DEBUG
    #   This function is finished and it is wrong. Run the program twice.
    #   history.log should have 2 lines, but it only ever has 1.
    #   Look at how the file is opened and fix it.
    with open(path, "w") as f:
        f.write(line + "\n")


# ---------------------------------------------------------------------------
# Part 4: the report
# ---------------------------------------------------------------------------

# The report runs only when this file is run directly, so the test file can
# import the functions above without the report running.
if __name__ == "__main__":
    approved = load_approved(APPROVED_FILE)
    inventory = load_inventory(INVENTORY_FILE)
    bad_lines = count_bad_lines(INVENTORY_FILE)
    unapproved = find_unapproved(inventory, approved)
    counts = count_by_host(unapproved)

    # Every line of the report goes into this list. It is written to
    # report.txt at the end.
    lines = []
    lines.append("SOFTWARE ALLOWLIST AUDIT")
    lines.append("=" * 40)
    lines.append("Approved programs:    " + str(len(approved)))
    lines.append("Inventory records:    " + str(len(inventory)))
    lines.append("Lines skipped:        " + str(bad_lines))
    lines.append("-" * 40)
    lines.append("NOT APPROVED")
    # TODO 14
    #   For each record in unapproved, append a line: 3 spaces, the host
    #   with .ljust(12), then the program. Like this:
    #      "   lab-01      uTorrent"

    lines.append("-" * 40)
    lines.append("NOT APPROVED PER COMPUTER")
    # TODO 15
    #   For each host in sorted(counts), append 3 spaces, the host with
    #   .ljust(12), then its count. The count needs str().

    # TODO 16
    #   Append these two lines. Use ", ".join() on the lists from
    #   hosts_at_or_above() and unique_programs().
    #      "Fix first:            lab-03, lab-06"
    #      "Programs to remove:   CCleaner, Steam, ..."

    lines.append("-" * 40)
    # TODO 17
    #   Work out the percent approved and the status. Then append:
    #      "Approved:             61.1%"
    #      "Status:               FAIL"
    percent = 0.0
    status = "UNKNOWN"
    lines.append("=" * 40)

    # TODO 18
    #   Call write_report() to save lines to REPORT_FILE. Then open
    #   REPORT_FILE in read mode, read() the whole file, and print it.
    #   This shows the report really was saved.

    append_history(HISTORY_FILE, str(len(inventory)) + " records, "
                   + str(len(unapproved)) + " not approved, " + status)

    # TODO 19
    #   Open HISTORY_FILE in read mode. readlines() gives a list with one
    #   string per line. Print "Runs recorded: " and how many lines there are.
