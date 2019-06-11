import subprocess

def main():
	cmd = "adb shell uiautomator dump"
	subprocess.check_output(cmd.split(' '))
	cmd = "adb shell cat /sdcard/window_dump.xml"
	result = subprocess.check_output(cmd.split(" "))
	print(result)
	'''
	f = open("prova.txt", "w")
	f.write(result)
	print("ok")
	'''

if __name__ == "__main__":
	main()
	