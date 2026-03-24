

doc_list = ["The Learn Python Challenge Casino.", 
            "They bought a car;", "Casinoville,"]
			
keyword = "casino"
indices=[]
for i, doc in enumerate(doc_list):
    # spilt the string into alist of word
	splitted_docs = doc.split()
	for np in splitted_docs:
	#remove the punctuations
		np = np.rstrip('.,;')
		np=np.lower()
	if keyword.lower()in np:
		indices.append(i)
		print(i,doc)