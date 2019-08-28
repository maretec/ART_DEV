import fileinput
import sys


def line_creator(file, parameter, value):
    file.write('{0:30}{1}'.format(parameter, ": " + value + "\n"))
    file.flush()
    file.close()

def date_to_mohid_date(date):
    mohid_date = str(date.year) + " " + str(date.month) + " " + str(date.day) + " " + str(0) + " " + \
                                                              str(0) + " " + str(0)
    return mohid_date


def modify_line(filepath, parameter, new_value):
    changed = False
    for line in fileinput.FileInput(filepath, inplace=True):
        if parameter in line:
            changed = True
            line = '{0:30}{1}'.format(parameter, ": " + new_value + "\n")
        sys.stdout.write(line)
    if not changed:
        line_creator(filepath, parameter, new_value)

def nomfinch_creator(workPath, parameters, values):
    file = open(workPath + "/exe/nomfinch.dat", 'w+')
    parameters = ["IN_BATIM", "ROOT", "ROOT_SRT", "SURF_DAT", "SURF_HDF", "DOMAIN", "IN_DAD3D", "OUT_DESF", "OUT_FIN",
                  "BOT_DAT", "BOT_HDF", "BOT_FIN", "AIRW_DAT", "AIRW_HDF", "AIRWFIN", "IN_MODEL", "IN_TIDES", "IN_TURB",
                  "TURBS_HDF", "DISPQUAL", "EUL_HDF", "EUL_FIN"]
    for parameter in parameters:
        line_creator(file, parameter, "1")
    file.close()
    return


