### Document factory

class Resume:                             # represent a resume doc.
    def __init__(self, name, experience): # init instances variable of resume
        self.name = name
        self.experience = experience
        
class CoverLetter:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        
def create_resume(name, experience): # creates an instance of the class and returning it
    return Resume(name, experience)

def create_cover_letter(name, company): #idem
    return CoverLetter(name, company)

"""Implement the DocumentFactory() function that takes a document_type parameter. 
Inside the factory function, use a dictionary mapping the document types to their 
corresponding document functions (create_resume and create_cover_letter)."""
"""The DocumentFactory() function should return the document function based on the provided document_type. 
If the document_type is not found in the dictionary, the factory should raise a ValueError.""" 


def DocumentFactory(document_type): # create a dict that maps the supported doc types to their doc. cration func.
    document_types = {
        "resume": create_resume,
        "cover_letter": create_cover_letter        
    }

    if document_type  in document_types:
        return document_types[document_type] # paramenter found on dict.?
    else:
        raise ValueError("Invalida document type")
         
# Test the implementation
factory = DocumentFactory("resume")                     # create a factory calling the funtion above with resume as arg.
resume = factory("John Doe", "5 years of experience")   # factory variable now holds the create_resume func to create instances of resumes

factory = DocumentFactory("cover_letter") # idem
cover_letter = factory("John Doe", "ABC Company")

print(resume.name, resume.experience)  # Output: John Doe 5 years of experience
print(cover_letter.name, cover_letter.company)  # Output: John Doe ABC Company    