
import os
class Utils:
   
   def show_disk_space():
      print(os.system('df -h'))
   def show_memory_usage():
         print(os.system('free -h'))
   def show_cpu_usage():
            print(os.system('lscpu'))
   def show_ram_usage():
            print(os.system('free -h'))
   def show_gpu_usage():
            print(os.system('nvidia-smi'))
   def show_os_version():
            print(os.system('uname -a'))
    
machine_a = Utils()
Utils.show_disk_space()
Utils.show_memory_usage()