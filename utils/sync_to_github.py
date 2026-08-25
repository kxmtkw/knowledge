import subprocess


def shellrun(cmd: str):
	subprocess.run(
		cmd,
		shell=True,
		capture_output=False
	)


def pull():
	shellrun("git pull")


def add():
	shellrun("git add .")


def commit(): 
	shellrun("git commit -m 'sync'")


def push():
	shellrun("git push")


def main():
	pull()
	add()
	commit()
	push()


if __name__ == "__main__":
	main()