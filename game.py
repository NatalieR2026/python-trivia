# List of trivia questions
trivia = [
            {
                'question': 'question body',
                'answer': 'correct',
                'options': ['option a', 'option b', 'correct']
            },
            {
                'question': '',
                'answer': '',
                'options': ['', '', '']
            },
            {
                'question': '',
                'answer': '',
                'options': ['', '', '']
            },
            {
                'question': '',
                'answer': '',
                'options': ['', '', '']
            }
]


# TO DO: Define functions to ask questions & compute score
def ask_q(questions, answer, options):
    is_correct = False
    # Display the question & options


    #for question, options in questions.items

    #for questions in trivia:
    #    print(question )
    
    # Take user input
    # Check if user input matches correct answer
    return is_correct


# GAME LOOP, call your functions below
def main():
    print("Starting a new Trivia game...")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

main()
