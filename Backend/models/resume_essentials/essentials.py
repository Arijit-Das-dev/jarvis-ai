class ResumeEssentials:

    def __init__(self):
        
        self.Exp = []
        self.Edu = []
        self.Pro = []

    def experience(self, title, company, location, start_date, end_date, bullets):

        self.Exp.append({
            "title":title,
            "company":company,
            "location":location,
            "start_date":start_date,
            "end_date":end_date,
            "bullets":bullets
        })
        return self.Exp
    
    def education(self, degree, institution, location , start_date, end_date, gpa, relevant_courses):

        self.Edu.append({
            "degree":degree,
            "institution":institution,
            "location":location,
            "start_date":start_date,
            "end_date":end_date,
            "gpa":gpa,
            "relevant_courses":relevant_courses
        })
        return self.Edu
    
    def projects(self, name, tech_stack, link, bullets):

        self.Pro.append({
            "name":name,
            "tech_stack":tech_stack,
            "link":link,
            "bullets":bullets
        })
        return self.Pro

    def data(
            self, 
            name, 
            email, 
            phone, 
            location, 
            linkedin, 
            github,
            summary, 
            skills, 
            experience, 
            education, 
            projects, 
            certifications,
            achievements,
            languages):
        
        return {
        "name":           name,
        "email":          email,
        "phone":          phone,
        "location":       location,
        "linkedin":       linkedin,
        "github":         github,
        "summary":        summary,
        "skills":         skills,
        "experience":     experience,
        "education":      education,
        "projects":       projects,
        "certifications": certifications,
        "achievements":   achievements,
        "languages":languages
    }