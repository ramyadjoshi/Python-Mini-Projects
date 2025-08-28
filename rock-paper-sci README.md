✂️ Rock Paper Scissors Game
An interactive and animated Rock Paper Scissors game built with Python and Tkinter. Features a modern dark-themed GUI with hover effects, animations, and score tracking for an engaging gaming experience.
📋 Features

Interactive GUI: Modern dark-themed interface with attractive styling
Animated Buttons: Hover effects and click animations for enhanced user experience
Score Tracking: Keep track of wins for both player and computer
Random Computer Opponent: Computer makes random choices for fair gameplay
Visual Feedback: Clear display of choices and results
Emoji Integration: Fun emojis for each choice (🪨, 📄, ✂️)
Responsive Design: Well-organized layout with proper spacing

🛠️ Technologies Used

Python 3.6+
Tkinter: GUI framework for interface design
Random Module: For computer's random choice generation
Event Handling: Mouse hover and click effects

📦 Installation & Setup
Prerequisites

Python 3.6 or higher
Tkinter (included with Python standard library)

Running the Game

Download the rock_paper_sci.py file
Run the game:
bashpython rock_paper_sci.py


🎯 How to Play
Game Rules

Rock 🪨 beats Scissors ✂️
Scissors ✂️ beats Paper 📄
Paper 📄 beats Rock 🪨
Same choices result in a Draw

Playing the Game

Launch: Run the script to open the game window
Make Choice: Click on Rock, Paper, or Scissors button
View Results: See both your choice and computer's choice
Check Score: Track wins in the score display
Play Again: Continue clicking buttons for more rounds
Exit: Click "Exit Game" to close

Example Gameplay

You choose Rock 🪨
Computer chooses Scissors ✂️
Result: You Win! 🎉
Your score increases by 1

🎨 Design Features
Visual Elements

Dark Theme: Modern #222831 background color
Gold Accents: #FFD700 for titles and highlights
Teal Buttons: #00ADB5 for interactive elements
Red Exit Button: #FF5722 for clear exit option

Animation Effects
pythondef on_hover(event):
    event.widget.config(bg="#FFD700")  # Gold on hover

def on_leave(event):
    event.widget.config(bg="#00ADB5")  # Reset to teal

def on_click(event):
    # Button shrink and expand animation
    event.widget.config(width=11, height=1)
    root.after(150, lambda: event.widget.config(width=12, height=2))
Layout Structure
┌─────────────────────────────────┐
│     Rock Paper Scissors         │
├─────────────────────────────────┤
│        Your Score: 0            │
│      Computer Score: 0          │
├─────────────────────────────────┤
│  [ROCK 🪨] [PAPER 📄] [SCISSORS ✂️] │
├─────────────────────────────────┤
│          [Exit Game]            │
└─────────────────────────────────┘
🧩 Code Structure
Key Components
Game Logic
pythonchoices = ["ROCK", "PAPER", "SCISSORS"]
win_conditions = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
Score Management
pythonuser_score = 0
computer_score = 0
Main Functions
play_game(user_choice)

Generates random computer choice
Compares choices using win conditions
Updates scores and displays results
Shows result popup with choices and outcome

Animation Functions

on_hover(event): Changes button color on mouse enter
on_leave(event): Resets button color on mouse leave
on_click(event): Creates click animation effect

Game Flow

User clicks a choice button
Computer generates random choice
System compares choices using win conditions dictionary
Scores are updated based on result
Result popup displays both choices and winner
Game continues until user exits

🔧 Customization Options
Color Schemes
python# Dark theme colors
bg_color = "#222831"      # Dark gray background
accent_color = "#FFD700"   # Gold accents
button_color = "#00ADB5"   # Teal buttons
exit_color = "#FF5722"     # Red exit button
text_color = "white"       # White text
Button Styling
python# Modify button appearance
button = tk.Button(
    text="ROCK 🪨",
    font=("Arial", 14),
    bg="#00ADB5",
    fg="white",
    width=15,
    height=2
)
Animation Timing
python# Adjust animation duration
root.after(150, lambda: event.widget.config(width=12, height=2))
#        ↑ Change this value for different animation speed
📚 Learning Concepts
This project demonstrates:
Programming Concepts

Dictionary Usage: Win conditions mapping
Random Generation: Computer choice selection
Event Handling: Mouse events and callbacks
GUI Programming: Advanced Tkinter features
Lambda Functions: Inline function definitions

Game Development

Game State Management: Score tracking
User Interface Design: Modern, responsive layouts
Animation Programming: Smooth visual effects
User Experience: Intuitive controls and feedback

Python Features

Global Variables: Score management across functions
String Manipulation: Choice processing and display
Control Flow: Conditional game logic
Module Integration: Random and Tkinter libraries

🚀 Possible Enhancements
Gameplay Features

Best of N Rounds: Set target score to win
Player vs Player: Two human players mode
Tournament Mode: Multiple rounds with brackets
Difficulty Levels: AI with different strategies
Game Statistics: Win/loss ratios and streaks

Visual Enhancements

Custom Icons: Replace text with images
Sound Effects: Audio feedback for actions
Animations: Smooth transitions between states
Themes: Multiple color schemes
Particle Effects: Celebration animations for wins

Advanced Features

Online Multiplayer: Network-based gameplay
AI Opponent: Machine learning-based computer player
Game History: Save and replay previous games
Leaderboards: Global or local high scores
Mobile Version: Touch-friendly interface

🎯 Difficulty Level
Beginner to Intermediate: Great for learning:

GUI development with Tkinter
Event-driven programming
Animation and visual effects
Game logic implementation
State management

💡 Development Tips
Code Organization
python# Separate concerns into functions
def play_game(choice):    # Game logic
def on_hover(event):      # UI animations  
def setup_gui():          # Interface creation
def main():               # Program entry point
Debugging Strategies

Print Statements: Debug choice comparisons
Event Logging: Track user interactions
Score Validation: Verify score calculations
Visual Testing: Check all button states

Performance Optimization

Event Unbinding: Clean up unused event handlers
Memory Management: Proper widget cleanup
Animation Efficiency: Minimize redraw operations

🐛 Troubleshooting
Common Issues
Buttons Not Responding

Check Event Binding: Ensure events are properly bound
Lambda Functions: Verify lambda syntax for command callbacks

Animation Problems

Timing Issues: Adjust root.after() delay values
Event Conflicts: Ensure events don't interfere with each other

Score Display Issues

Global Variables: Verify global keyword usage
Label Updates: Check config() method calls

🔍 Code Evolution
The project includes multiple versions showing progression:
Version 1: Basic Console
python# Simple text-based version with basic if-else logic
Version 2: Simple GUI
python# Basic Tkinter interface with messagebox results
Version 3: Enhanced GUI
python# Score tracking and better visual design
Version 4: Animated Version (Final)
python# Full animations, modern styling, and advanced features
📊 Win Conditions Logic
Traditional Rules Implementation
pythonwin_conditions = {
    "ROCK": "SCISSORS",    # Rock crushes Scissors
    "PAPER": "ROCK",       # Paper covers Rock
    "SCISSORS": "PAPER"    # Scissors cuts Paper
}

# Game logic
if user_choice == computer_choice:
    result = "DRAW"
elif win_conditions[user_choice] == computer_choice:
    result = "USER WINS"
else:
    result = "COMPUTER WINS"
📝 Requirements File
# No external requirements
# Uses Python standard library only
📝 License
This project is part of the Python Practice Projects collection and is available for educational use.

Rock on and may the best choice win! 🎸🎮
