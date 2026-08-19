from pathlib import Path

IGNORE_DIRS = ["utils"]

def depth_filter(header: str, depth: int) -> str:
	match depth % 3:
		case 0:
			return f"# {header}"
		case 1:
			return f"## {header}"
		case _:
			return f"### `{header}`"
		

def generate_index(md: list[str] = [], directory: Path = Path("."), depth=1) -> list[str]:

	if depth == 1: md.append("# Index")

	sub_directories = []
	files = []

	for item in directory.iterdir():

		if item.name.startswith("."):
			continue

		if item.is_file():
			files.append(item)

		if item.is_dir() and item.name not in IGNORE_DIRS:
			sub_directories.append(item)

	files.sort()
	for file in files:
		md.append(f"+ [{file.name}]({file})")

	sub_directories.sort()
	for dir in sub_directories:
		md.append(depth_filter(dir.name.title(), depth))
		generate_index(md, dir, depth + 1)


	return md


def write_index(md: list[str]):
	with open("index.md", "w") as file:
		file.write("\n".join(md))


def main():
	md = generate_index()
	write_index(md)


if __name__ == "__main__":
	main()