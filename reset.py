import os

dir_path = r"C:\ProgramData\AnyDesk"

service_file_path = os.path.join(dir_path, "service.conf")
if os.path.exists(service_file_path):
    os.remove(service_file_path)

system_file_path = os.path.join(dir_path, "system.conf")
if os.path.exists(system_file_path):
    os.remove(system_file_path)
