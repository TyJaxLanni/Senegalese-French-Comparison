


with open("corpus_sen.txt", "r",encoding="utf-8") as corpus, open("corpus_sen_cleaned.txt", "w",encoding="utf-8") as cleaned:

	count =0
	for line in corpus:
		if count >= 10000:
			break
		line = line.strip()
		#print(line)
		if len(line.strip()) == 0:
			print("empty")

		elif len(line.split()) < 2:
			print("not enough words: ", line)

		elif line[0].isupper() == False and line[0] != '"':
			print("bad line start: ", line)

		elif line[-1] != ".":
			print("bad period line: ", line)

		elif line[-2] in ["!", "?"]:
			print("needs edit: ", line)
			line = line[:-1]
			count += 1
			print(line, file=cleaned)

		else:
			count += 1
			print(line, file=cleaned)
	print(count)