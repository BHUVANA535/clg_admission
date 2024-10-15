import re

class AdmissionBot:
    def __init__(self):
        self.context = {
            'procedure': "The admission procedure involves filling out an online application form and submitting required documents.",
            'requirement': "The admission requirements include a high school diploma or equivalent, standardized test scores, and letters of recommendation.",
            'deadline': "The admission deadline for the upcoming semester is March 15th."
        }
    
    def respond(self, user_input):
        response = ""
        # Check if the user input contains keywords to identify the query type
        if re.search(r'\b(admission|procedure|requirement|deadline)\b', user_input, re.IGNORECASE):
            response = self.handle_admission_query(user_input)
        elif re.search(r'\b(thank you|thanks)\b', user_input, re.IGNORECASE):
            response = "You're welcome!"
        else:
            response = "I'm sorry, I didn't understand that. Could you please rephrase your question?"
        return response
    
    def handle_admission_query(self, user_input):
        for key, value in self.context.items():
            if re.search(r'\b' + key + r'\b', user_input, re.IGNORECASE):
                return value
        return "I'm sorry, I don't have the information for that. Could you please specify your query further?"
    
    def chat(self):
        print("Welcome to the College Admission Bot. How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                confirm_exit = input("Are you sure you want to exit? (yes/no): ")
                if confirm_exit.lower() == 'yes':
                    print("Thank you for using the College Admission Bot. Goodbye!")
                    break
            response = self.respond(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    bot = AdmissionBot()
    bot.chat()
