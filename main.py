

import subprocess
import os
import pathlib


global_username = os.getlogin()
global_minecraft_backup_directory = pathlib.Path("C:\\Users\\{}\\minecraft_backups".format(global_username))
global_minecraft_server_world = pathlib.Path("C:\\Users\\{}\\Desktop\\Minecraft Server\\world".format(global_username))

def world_restore():
    subprocess.run(["copy", global_minecraft_backup_directory,
                    global_minecraft_server_world], 
                    shell=True, 
                    capture_output=True)


def world_backup():
    subprocess.run(["copy", 
                    global_minecraft_server_world, 
                    global_minecraft_backup_directory], 
                    shell=True, 
                    capture_output=True)
    for data in global_minecraft_server_world.iterdir():
        data_list = str(data).split("\\")
        print(data_list[-1])  
        subprocess.run(["del", "{}\\{}".format(global_minecraft_server_world, data_list[-1])], shell=True)


def main():
    backup_option = input(""" 
    Please select from the following. \n\n1) Server Backup \n2) Server Restore 
\n>>  """)
    if backup_option == "1":
        backup_confirmation = input("\nAre you sure you want to backup current world? y/n ")
        if backup_confirmation == 'y' or 'Y':
            world_backup()
            print("\n[!] Creating backup!")
            print("[!] Backup creation successful.")
        elif backup_confirmation == 'n' or 'N':
            subprocess.run(["cls"], shell=True)
            main()
    elif backup_option == '2':
        restore_confirmation = input("\n Are you sure you want to restore your world? y/n ")
        if restore_confirmation == 'y' or 'Y':
            world_restore()
            print("\n[!] Restoring world!")
            print("[!] World restore successful.")
        elif restore_confirmation == 'n' or 'N':
            subprocess.run(["cls"], shell=True)
            exit()


if __name__ == "__main__":
    username = os.getlogin()
    minecraft_backup_directory = pathlib.Path("C:\\Users\\{}\\minecraft_backups".format(username))
    minecraft_dir_exists = minecraft_backup_directory.exists() 
    if minecraft_dir_exists == False:
        os.mkdir("{}".format(minecraft_backup_directory))
        main()
    elif minecraft_dir_exists == True:
        main()
