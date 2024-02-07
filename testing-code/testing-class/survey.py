#class that helps administer anonymous surveys

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question): ##class starts with a question
        """Store a question, and prepare to store responses."""
        self.question = question 
        self.responses = [] ##empty list to store responses

    def show_question(self): ##method to show the question
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response): ##method to store a single response
        """Store a single response to the survey."""
        self.responses.append(new_response) ##append the response to the list of responses

    def show_results(self): ##method to show all the responses
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses: ##loop through the list of responses
            print(f"- {response}") ##print each response