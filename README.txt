web application that checks texts for plagiarism
plagiarism is the appropriation of someone else's work in a certain area without the permission of the author or without links to the original text
that is, the essence of the project is to find out how much one text is similar to another
we will use the concept of vectors, namely the TF-IDF (TF-IDF is a measure of originality of a word by comparing the number of times a word appears in a doc with the number of docs the word appears in). we will also use a Cosine Similrity. it shows how similar vectors are.
principle of work - we upload files, read them, check for plagiarism and show whether it is plagiarism
there are two files in this project - one (plagiarism_checker_template.py) with the logic of the program, the second (streamlit.py) is a web part
run the file streamlit.py in the terminal in this way: streamlit  run streamlit.py
we get two url links. we follow any link and we get our small web application. we can upload text files, view their content and check them for plagiarism. as a result, we get a graph (table), where each text is compared with another and the coefficient of their similarity is written