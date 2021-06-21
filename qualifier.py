from typing import List, Any, Optional

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    if not labels:
      # No labels, only one column.
      # Finding the max len of every item. Every item is converted to a string before len().
      length = max([len(str(*rows[i])) for i in range(0,len(rows))]) + 2 # Finds the max length of labels, col 0
      print("┌" + "─" * (length) + "┐")
      
      # Loop through the list to make the walls
      # Length - (3 +len(row_item)) = number of spaces needed
      for i in range(0, len(rows)):
          if len(str(*rows[i])) == length-2: print("│", *rows[i], "│")
          else: print("│", *rows[i], " "*(length-(3 + len(str(*rows[i])))), "│")

      print("└" + "─" * (length) + "┘")
    else:
      # Finding the max length in labels and row.
      length = max([len(str(labels[i])) for i in range(0,len(labels))])
      for i in range(0, len(labels)):
        for n in range(0, len(rows[i])):
          length = max(len(str(rows[i][n])), length)
      length += 2

      # Labels
      print("┌", end="")
      for i in range(0, len(labels)-1):
        print("─" * length + "┬", end="")
      print("─" * length + "┐")

      # Bottom row for labels
      for i in range(0, len(labels)):
        print("│", labels[i], " "*(length-(2 + len(str(labels[i])))), end="")
      print("│")
      

      # Top for rows
      print("├", end="")
      for i in range(0, len(labels)-1):
        print("─" * length + "┼", end="")
      print("─" * length + "┤")

      for i in range(0, len(rows)):
        for n in range(0, len(labels)):
          print("│", rows[i][n], " "*(length-(2 + len(str(rows[i][n])))), end="")
        print("│")
      
      print("└", end="")
      for i in range(0, len(labels)-1):
        print("─" * length + "┴", end="")
      print("─" * length + "┘")
        


table = make_table(
     rows=[
         ["Lemon", 18_3285, "Owner"],
         ["Sebastiaan", 18_3285.1, "Owner"],
         ["KutieKatj", 15_000, "Admin"],
         ["Jake", "MoreThanU", "Helper"],
         ["Joe", -12, "Idk Tbh"]
     ],
     labels=["User", "Messages", "Role"]
 )
