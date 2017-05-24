import src.trash as trash
import commands.remove_command
import src.dividing
import os

testing_trash = trash.Trash("123")
remove_command = commands.remove_command.RFCommand(testing_trash)

res = src.dividing.parallel_dividing(os.listdir(os.curdir))
print res