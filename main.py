from openai import OpenAI  # pip install OpenAI
from tkinter import *
from tkinter import scrolledtext

# main code for API call
# YOU HAVE TO SIGN UP FOR YOUR OWN API KEY @ https://platform.openai.com/docs/overview
client = OpenAI(api_key="ENTER YOUR API KEY HERE")  # <<< VERY IMPORTANT
def chat_with_gpt(prompt, chat_display):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    response_content = response.choices[0].message.content.strip()
    chat_display.insert(END, f"\nYou:\n\n{prompt}\n\n{response_content}\n\n\n")

def submit_user_input(event=None):  # event is a tkinter thing that is used to detect when a button is clicked (<Return> in this case, see line 53)
    user_input = user_input_entry.get()
    if user_input.lower() in ["q", "quit", "exit", "bye", "thanks"]:  # quit commands via the user input text box
        root.destroy()
    else:
        chat_with_gpt(user_input, chat_display)
        user_input_entry.delete(0, END)

# Defining some colors so I can adjust them in 1 place as needed
color_darkBG = "#1c1c1c"
color_lightBG = "#232323"
color_mainText = "#ffffff"
color_altText = "#42f56f"
color_buttonText = "#000000"
color_buttonBG = "#42f56f"

# tkinter main GUI styling
root = Tk()
root.title("GPT Language Interpreting Assistant") 
root.configure(background=color_darkBG)  # sets main window color
root.geometry("600x800")  # sets the initial size of the window
root.grid_rowconfigure(1, weight=1)  # allows for proportional resizing of the row
root.grid_columnconfigure(0, weight=1)  # allows for proportional resizing of the column

# chat log display / history
chat_display_label = Label(root, text="GLIA Chat", font=("Helvetica", 16), background=color_darkBG, foreground=color_altText)
chat_display_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

chat_display = scrolledtext.ScrolledText(root, width=50, height=20, font=("Helvetica", 12), background=color_lightBG, foreground=color_mainText)
chat_display.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

# user input box
user_input_label = Label(root, text="User Input", font=("Helvetica", 14), background=color_darkBG, foreground=color_altText)
user_input_label.grid(row=2, column=0, padx=20, sticky="ew")

user_input_entry = Entry(root, width=40, font=("Helvetica", 14), background=color_lightBG, foreground=color_mainText)
user_input_entry.grid(row=3, column=0, padx=20, sticky="ew")
user_input_entry.bind("<Return>", submit_user_input)  # Bind Enter key

# submit button for user input box to be submitted
submit_button = Button(root, text="Ask", padx=10, pady=5, command=submit_user_input, background=color_buttonBG, foreground=color_buttonText)
submit_button.grid(row=3, column=1, pady=20, padx=20, sticky="e")

root.mainloop()