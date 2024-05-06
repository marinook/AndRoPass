import os
import sys

from argparse import ArgumentParser

from utils.ColorPrint import ColorPrint as cp
from utils.APKFile import APKFile
from utils.RequirementCheck import RequirementCheck
from utils.Compiler import Compiler

DES = """
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██████╗  █████╗ ███████╗███████╗
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██████╔╝███████║███████╗███████╗
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██╔═══╝ ██╔══██║╚════██║╚════██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║     ██║  ██║███████║███████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
https://github.com/hojatsajadinia/AndRoPass                 
"""




def argument_catcher():
    my_parser = ArgumentParser(
        prog='AndRoPass', description='Android Root and Emulator Detection Bypass Tool')
    my_parser.add_argument('--apk', '-a',
                           type=str,
                           required=True,
                           help='APK full path')
    return my_parser.parse_args().apk


def main():
    cp.pr('blue', DES)
    apk_file_path = argument_catcher()
    apk_file = APKFile(apk_file_path)
    
    if not apk_file.exist():
        cp.pr("red", "[ERROR] APK file not found.")
    cp.pr("info", "[INFO] Checking AndRoPass requirements")
    requirement_check = RequirementCheck()
    if not (requirement_check.check()):
        sys.exit(0)
    
    compiler = Compiler(requirement_check.apktool_path, apk_file_path)
    decompile_out_with_resource , decompile_out_without_resource = compiler.decompile()
    


if __name__ == "__main__":
    main()
