class Document:
    def Print(self):
        print("Print the doc")


class PDF(Document):
    def Print(self):
        print("Print the PDF", end=' ')


class Word(Document):
    def Print(self):
        print("Print the word", end=' ')


def new_doc(all):  # method overriding- creating our own class
    # to fetch overall value or result
    for Document in all:
        Document.Print()
        print()


new_doc([PDF(), Word()])

#
# class Doc:
#
#     def print(self):
#         print("priting doc")
#
#
# class PDF(Doc):
#     def print(self):
#         print("priting PDF")
#
#
# class Word(Doc):
#     def print(self):
#         print("priting Word")
#
#
#
# def print_docs(alldocs):
#     for doc in alldocs:
#         doc.print()
#
#
# print_docs([PDF(),PDF(),Word()])
