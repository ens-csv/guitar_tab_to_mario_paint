# guitar_tab_to_mario_paint
Guitar Tab to Mario Paint Composer Note Converter
-------------------------------------------------
This script parses standard ASCII guitar tablature and converts it into
Mario Paint Composer note letters (e.g. 'a' = C5, 'b' = B4, ..., 'o' = C3).

Usage:
    Run the script and it will print out each note with its time index.

Note:
    If a note falls outside the Mario Paint range, it is transposed up
    one or more octaves to fit.

Example:
    Guitar tab input:
        G|--4--5--7---------|
        D|--------5---------|
        E|-----3------------|

    Output:
        Time 2: g
        Time 4: m
        Time 5: f
        Time 8: d
        Time 8: g

License: MIT
